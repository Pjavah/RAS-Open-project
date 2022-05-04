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
        self.id = 0
        self.image_sub = self.create_subscription(Image, "/Image_PubSubTopic",self.cam_callback, 10)
        self.takeoff_publisher = self.create_publisher(Empty, '/takeoff', 10)
        self.land_publisher = self.create_publisher(Empty, '/land', 10)
        self.move_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.found_publisher = self.create_publisher(Int16, '/found', 10)
        self.image_sub = self.create_subscription(Int16,'/command',self.command_callback, 10)


    def command_callback(self,msg):
        self.id = msg

    def cam_callback(self,msg):
        self.cnt += 1
        if(self.cnt % 5 == 0):
            cv2_img = self.imgmsg_to_cv2(msg)
            cv.imwrite('camera_image.jpeg'.format(self.cnt), cv2_img)

            #This is for launching the tello. This should come from the jetbot. 
            if self.cnt == 1:
                msg = Int16
                self.takeoff_publisher.publish(msg)
            #    time.sleep(2)
            #    print("nousi")
            self.id = 4
            if self.id != 0:
                true = contourSquares(cv2_img, self.id)
                msg = Int16()
                msg.data = true
                self.found_publisher.publish(msg)
                if true == 0:
                    msg = Twist()
                    msg.angular.z = 0.25
                    self.move_publisher.publish(msg)
                    time.sleep(2)
                    msg = Twist()
                    msg.angular.z = 0.0
                    self.move_publisher.publish(msg)
                    

                print(true)
                #self.found_publisher.publish(msg)
            #cv.imshow("Result",frame)
            #cv.waitKey(1)

            #This is for landing the tello. This should be come from the jetbot. 
            #if self.cnt == 2:
            #    msg = Empty()
            #    self.land_publisher.publish(msg)
            #    print("laski")
            #    self.cnt = 3
            #    #value = 1

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