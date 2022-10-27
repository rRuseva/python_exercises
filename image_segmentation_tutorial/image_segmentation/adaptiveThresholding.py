# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:43:02 2022

@author: Radi
"""

import cv2
import os

import file_manager as fm


if __name__ == '__main__':
    print(cv2.__version__)
    
    image_directory = 'data3'
    image_name = 'c1_p-00001'
    image_ext = 'jpg'
    results_directory = 'results_adaptiveTh3-Otsu'
    
    if os.path.exists(results_directory):
        print("This results directory already exist!")
    else:       
        os.mkdir(results_directory)
    
    images = fm.read_images(image_directory)
    
	
    for image in images:
        image, image_name, image_ext, image_type = image
        image = cv2.imread(os.path.join(image_directory,'.'.join((image_name, image_ext))))
        
        print("Processing: {} - {} - {}".format( image_name, image.shape, image_type))
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # image_gaussianTh = cv2.adaptiveThreshold(image_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        ret2,th2 = cv2.threshold(image_grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # show the image
        param="02_adaptiveThr-Otsu"
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), th2)

# =============================================================================
        # cv2.namedWindow("Display window", cv2.WINDOW_FULLSCREEN )
        # cv2.imshow("Display window", image)
        # k = cv2.waitKey(0)