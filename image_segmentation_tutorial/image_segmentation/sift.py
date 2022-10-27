# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:39:20 2022

@author: Radi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

import random

import file_manager as fm

if __name__ == '__main__':
    print(cv2.__version__)
    print(cv2.__version__)
    image_directory = 'data'
    image_name = 'c1_p-00001'
    image_ext = 'jpg'
    results_directory = 'results'
    
    
    images = fm.read_images(image_directory)
	
    for image in images:
        image, image_name, image_ext, image_type = image
        image = cv2.imread(os.path.join(image_directory,'.'.join((image_name, image_ext))))
        
        print("Processing: {} - {} - {}".format( image_name, image.shape, image_type))
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        sift = cv2.xfeatures2d.SIFT_create(contrastThreshold = 0.06)
        
        keypoints, _ = sift.detectAndCompute(image, None)
        sift_image = cv2.drawKeypoints(image_grey, keypoints, None)
        
        
        
        
        
       # show the image
        param="02_sift-strContrastThr"
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), sift_image)
        # cv2.namedWindow("Display window", cv2.WINDOW_FULLSCREEN )
        # cv2.imshow("Display window", image)
        # k = cv2.waitKey(0)