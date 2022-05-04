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

        #self.jetId is the number corresponding to a color
        self.jetId=0
        self.cnt = 0
        #takenoff is a boolean to know if there has been a take off command
        self.takenoff = False


        self.image_sub = self.create_subscription(Image, "/camera",self.cam_callback, 10)
        self.qr_subber = self.create_subscription(Int16, "/objectfound", self.color_sub, 10)#QRKOODI, "/QRKAMERA", self.qr_callback, 10 )
        #self.cmdvel_publisher = self.create_publisher(Twist, '/control',self.qr_sub, 10)
        self.found_publisher = self.create_publisher(Int16, "/command", 10)
        self.takeoff_subber = self.create_subscription(Empty, '/takeoff',self.takeoff_sub, 10)

        #TAKEOFF AND LAND NOT REQUIRED, JETBOT PUBLISHES THESE
        #self.takeoff_publisher = self.create_publisher(Empty, '/takeoff', 10)
        #self.land_publisher = self.create_publisher(Empty, '/land', 10)

    def cam_callback(self,msg):
        self.cnt += 1
        if(self.cnt % 5 == 0):
            cv2_img = self.imgmsg_to_cv2(msg)





            #Aruco detection, prints found id. 
            #ids = array of arrays
            (corners, ids, rejected) = cv.aruco.detectMarkers(
                cv2_img, this_aruco_dictionary, parameters=this_aruco_parameters)
            print(ids)
            #if ids:
            #    print(ids[0][0])
            #cv.imshow("Result",frame)
            #cv.waitKey(1)

            #search for any aruco markers

            if ids is not None:
                msg = Int16()
                msg.data = int(ids[0][0])
                self.found_publisher.publish(msg)



    def color_sub(self, msg):
        self.jetId = msg
        print(msg)

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