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
from std_msgs.msg import String

desired_aruco_dictionary = cv.aruco.DICT_4X4_50
this_aruco_dictionary = cv.aruco.Dictionary_get(desired_aruco_dictionary)
this_aruco_parameters = cv.aruco.DetectorParameters_create()

class Tello(Node):

    
    def __init__(self):
        super().__init__('tello')
        self.jetId=0
        self.cnt = 0
        self.image_sub = self.create_subscription(Image, "/camera",self.cam_callback, 10)
        self.qr_sub = self.create_subscription()#QRKOODI, "/QRKAMERA", self.qr_callback, 10 )
        self.cmdvel_publisher = self.create_publisher(Twist, '/control', 10)
        self.found_publisher = self.create_publisher(String, "/command", 10)

        #TAKEOFF AND LAND NOT REQUIRED, JETBOT PUBLISHES THESE
        #self.takeoff_publisher = self.create_publisher(Empty, '/takeoff', 10)
        #self.land_publisher = self.create_publisher(Empty, '/land', 10)

    def cam_callback(self,msg):
        self.cnt += 1
        if(self.cnt % 5 == 0):
            cv2_img = self.imgmsg_to_cv2(msg)





            #Aruco detection, prints found id. 
            #I don't know if ids are in array or in a single int?
            (corners, ids, rejected) = cv.aruco.detectMarkers(
                cv2_img, this_aruco_dictionary, parameters=this_aruco_parameters)
            print(ids)
            #cv.imshow("Result",frame)
            #cv.waitKey(1)

            #search for any aruco markers

            #after finding auroco, compare the id to jetbot's
            if ids == self.jetId:
                msg = String()
                msg.data = "Found!"
                self.found_publisher.publish(msg)



    def qr_sub(self, msg):
        self.jetId = msg

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