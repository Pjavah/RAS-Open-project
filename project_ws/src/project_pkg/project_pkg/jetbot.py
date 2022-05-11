#! /usr/bin/python
import base64
import cv2 as cv
import numpy as np
import time
import rclpy
from rclpy.node import Node
import sys
from gettingcontours import contourSquares
from sensor_msgs.msg import Image
from std_msgs.msg import Empty
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

class Jetbot(Node):
    
    def __init__(self):
        super().__init__('jetbot')
        self.cnt = 0
        self.takeoff, self.land = 0, 0
        self.id = 0
        self.wait = 0  # This is a flag that tells when to wait next id from Tello
        self.found_cubes = []
        self.recent_value , self.current_value= 0,0
        self.image_sub = self.create_subscription(Image, "/Image_PubSubTopic",self.cam_callback, 10)
        self.takeoff_publisher = self.create_publisher(Empty, '/takeoff', 10)
        self.land_publisher = self.create_publisher(Empty, '/land', 10)
        self.move_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.found_publisher = self.create_publisher(Int16, '/found', 10)
        self.command_sub = self.create_subscription(Int16,'/command',self.command_callback, 10)

    #Receive the found id that Tello has read from aruco
    def command_callback(self,msg):
        self.current_value = msg.data

    #All the functioning is happening in the cam_callback
    def cam_callback(self,msg):
        self.cnt += 1

        #At the beginning of the execution, send a takeoff command to Tello
        if self.takeoff == 0:
            msg = Empty()
            self.takeoff_publisher.publish(msg)
            time.sleep(2)
            self.takeoff = 1
        
        #Jetbot is subscribing a topic where Tello is continuously sending the found id. 
        #The wait flag tells when Jetbot needs to wait new id from Tello. 
        #Wait flag is activated only when Tello has found a different id. 
        if self.current_value != self.recent_value:
            self.id = self.current_value
            self.wait = 0
        self.recent_value = self.current_value

        #When wait flag is zero, Jetbot will begin to search the coloured cube corresponding to given id
        if self.wait == 0:
            if(self.cnt % 2 == 0):
                cv2_img = self.imgmsg_to_cv2(msg)
                cv.imwrite('camera_image.jpeg'.format(self.cnt), cv2_img)
                if self.id != 0:
                    found = contourSquares(cv2_img, self.id)
                    #Publish to a topic that the wanted cube is found and wait for the next id
                    if found != 0:
                        msg = Int16()
                        msg.data = found
                        self.found_publisher.publish(msg)
                        self.wait = 1

                        #Append found cube in the array of found cubes. All the colours needs to be found once. 
                        #No duplicates to the array. 
                        if self.id not in self.found_cubes:
                            self.found_cubes.append(self.id)
                        

                        #When all four blocks have been found, send a land command to Tello and set Jetbot in a wait mode
                        if len(self.found_cubes) == 4: 
                            msg = Empty()
                            self.land_publisher.publish(msg)
                            self.wait = 1

                    #When jetbot doesn't detect the correct cube, it continues the searching
                    if found == 0:
                        msg = Twist()
                        msg.angular.z = 0.25
                        self.move_publisher.publish(msg)
                        time.sleep(1)
                        msg = Twist()
                        msg.angular.z = 0.0
                        self.move_publisher.publish(msg)


    def imgmsg_to_cv2(self, img_msg):
        n_channels = len(img_msg.data) // (img_msg.height * img_msg.width)
        dtype = np.uint8

        img_buf = np.asarray(img_msg.data, dtype=dtype) if isinstance(img_msg.data, list) else img_msg.data

        if n_channels == 1:
            cv2_img = np.ndarray(shape=(img_msg.height, img_msg.width),
                            dtype=dtype, buffer=img_buf)
        else:
            cv2_img = np.ndarray(shape=(img_msg.height, img_msg.width, n_channels),
                            dtype=dtype, buffer=img_buf)

        if img_msg.is_bigendian == (sys.byteorder == 'little'):
            cv2_img = cv2_img.byteswap().newbyteorder()

        return cv2_img

def main():
    rclpy.init()
    jetbot = Jetbot()

    rclpy.spin(jetbot)

    jetbot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()