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

desired_aruco_dictionary = cv.aruco.DICT_4X4_50
this_aruco_dictionary = cv.aruco.Dictionary_get(desired_aruco_dictionary)
this_aruco_parameters = cv.aruco.DetectorParameters_create()

class Tello(Node):
    
    def __init__(self):
        super().__init__('tello')
        self.cnt = 0
        self.image_sub = self.create_subscription(Image, "/camera",self.cam_callback, 10)
        self.takeoff_publisher = self.create_publisher(Empty, '/takeoff', 10)
        self.land_publisher = self.create_publisher(Empty, '/land', 10)

    def cam_callback(self,msg):
        self.cnt += 1
        if(self.cnt % 5 == 0):
            cv2_img = self.imgmsg_to_cv2(msg)

            #This is for launching the tello. This should come from the jetbot. 
            #if self.cnt == 1:
            #    msg = Empty()
            #    self.takeoff_publisher.publish(msg)
            #    time.sleep(2)
            #    print("nousi")
            #    self.cnt = 1

            #Aruco detection, prints found id. 
            (corners, ids, rejected) = cv.aruco.detectMarkers(
                cv2_img, this_aruco_dictionary, parameters=this_aruco_parameters)
            print(ids)
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
    tello = Tello()

    rclpy.spin(tello)

    tello.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()