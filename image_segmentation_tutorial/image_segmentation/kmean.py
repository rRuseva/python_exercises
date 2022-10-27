# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:08:59 2022

@author: Radi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


import file_manager as fm

if __name__ == '__main__':
    image_directory = 'data'
    image_name = 'c1_p-00001'
    image_ext = 'jpg'
    results_directory = 'results'
    
    
    images = fm.read_images(image_directory)
	
    for image in images:
        image, image_name, image_ext, image_type = image
        image = cv2.imread(os.path.join(image_directory,'.'.join((image_name, image_ext))))
        
        print("Processing: {} - {} - {}".format( image_name, image.shape, image_type))
        
        # reshape the image to a 2D array of pixels and 3 color values (RGB)
        pixel_values = image.reshape((-1, 3))
        # convert to float
        pixel_values = np.float32(pixel_values)
        
        
        # define stopping criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        k = 3
        
        _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        # convert back to 8 bit values
        centers = np.uint8(centers)
        
        # flatten the labels array
        labels = labels.flatten()
        
        # convert all pixels to the color of the centroids
        segmented_image = centers[labels.flatten()]
        
        
        # reshape back to the original image dimension
        segmented_image = segmented_image.reshape(image.shape)
        # show the image
        
        param="01_k3"
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res"+param+"."+str(image_ext)), segmented_image)
        # cv2.namedWindow("Display window", cv2.WINDOW_FULLSCREEN )
        # cv2.imshow("Display window", image)
        # k = cv2.waitKey(0)
        
