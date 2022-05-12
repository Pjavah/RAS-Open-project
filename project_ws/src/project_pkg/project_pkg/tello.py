#! /usr/bin/python
import base64
import cv2 as cv
import numpy as np
import time
import rclpy
from rclpy.node import Node
import sys
from sensor_msgs.msg import Image
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

desired_aruco_dictionary = cv.aruco.DICT_4X4_50
this_aruco_dictionary = cv.aruco.Dictionary_get(desired_aruco_dictionary)
this_aruco_parameters = cv.aruco.DetectorParameters_create()

class Tello(Node):

    
    def __init__(self):
        super().__init__('tello')

        #jetId is a flag which tells whether jetbot found the correct cube or not
        self.jetId=0
        self.cnt = 0
        #takenoff is a boolean to know if there has been a take off command
        self.takenoff = False
        self.found = False #checks if the jetbot has found the correct id

        self.image_sub = self.create_subscription(Image, "/camera",self.cam_callback, 10)
        self.qr_subber = self.create_subscription(Int16, "/found", self.color_sub, 10)
        self.cmdvel_publisher = self.create_publisher(Twist, '/control', 10)
        self.found_publisher = self.create_publisher(Int16, "/command", 10)
        self.takeoff_subber = self.create_subscription(Empty, '/takeoff',self.takeoff_sub, 10)


    def cam_callback(self,msg):
        self.cnt += 1
        if(self.cnt % 5 == 0):
            cv2_img = self.imgmsg_to_cv2(msg)




            #Aruco detection, prints found id. 
            #ids = array of arrays
            (corners, ids, rejected) = cv.aruco.detectMarkers(
                cv2_img, this_aruco_dictionary, parameters=this_aruco_parameters)
            
            #if tello has sent taken off, go up for 10 seconds
            if self.takenoff:
                end_time = time.time()+10
                msg = Twist()
                msg.linear.z = 16.0
                msg.angular.z = 0.0
                self.takenoff=0
                while(time.time() < end_time):
                    self.cmdvel_publisher.publish(msg)
                    time.sleep(0.2)

            #If no ids are visible, the drone spins until it finds one. 
            if ids == None:
                msg = Twist()
                msg.angular.z = 20.0
                msg.linear.x = 0.0
                msg.linear.z = 0.0
                self.cmdvel_publisher.publish(msg)
            

            #When the drone finds an id
            if ids is not None:
                #checking that there's only one id and stare at that for now
                if len(ids) == 1:
                    msg = Twist()
                    msg.angular.z = 0.0
                    msg.linear.x = 0.0
                    msg.linear.z = 0.0
                    self.cmdvel_publisher.publish(msg)

                    #publish the id for the jetbot
                    msg2 = Int16()
                    msg2.data = int(ids[0][0])
                    self.found_publisher.publish(msg2)

                    #wait until jetbot finds it
                    if self.jetId == ids[0][0]:
                        #set found variable to true
                        self.found = True
                        end_time = time.time()+3
                        #Staying here for 3 seconds to show that we actually found it!
                        while(time.time() < end_time):
                            self.found = False
                            time.sleep(0.2)

                            #after three seconds, start spinning without subscribing for five seconds
                            #this is so that the tello really has lost the previous id
                            end_time2 = time.time()+5
                            msg3 = Twist()
                            msg3.angular.z = 20.0
                            msg3.linear.x = 0.0
                            msg3.linear.z = 0.0
                            
                            while(time.time() < end_time2):
                                self.cmdvel_publisher.publish(msg3)
                                time.sleep(0.2)



    def color_sub(self, msg):
        #/found topic
        self.jetId = msg.data
        

    def takeoff_sub(self, msg):
        if msg:
            self.takenoff = True
            print(self.takenoff)

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
    tello = Tello()

    rclpy.spin(tello)

    tello.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()