#! /usr/bin/python
import base64
import cv2 as cv
import numpy as np

import rclpy
from rclpy.node import Node
import sys
from sensor_msgs.msg import Image


class CamSubscriber(Node):
    def __init__(self):
        super().__init__('image_listener')
        self.cnt = 0
        self.image_sub = self.create_subscription(Image, 'Image_PubSubTopic', self.image_sub_callback, 10)


    def image_sub_callback(self, msg):

        # Convert ROS Image message to OpenCV2
        cv2_img = self.imgmsg_to_cv2(msg)

        self.cnt += 1
        # Save OpenCV2 image as a jpeg
        cv.imwrite('camera_image.jpeg'.format(self.cnt), cv2_img)
        #print("Received an image!_{}".format(self.cnt))


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

        # If the byte order is different between the message and the system.
        if img_msg.is_bigendian == (sys.byteorder == 'little'):
            cv2_img = cv2_img.byteswap().newbyteorder()

        return cv2_img


def main():
    rclpy.init()
    cam_subscriber = CamSubscriber()

    # Spin until ctrl + c
    rclpy.spin(cam_subscriber)

    cam_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()