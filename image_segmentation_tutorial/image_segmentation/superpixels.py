# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:08:59 2022

@author: Radi
"""

import cv2
import numpy as np
import os

import file_manager as fm



if __name__ == '__main__':
    print(cv2.__version__)
    image_directory = 'data3'
    image_name = 'c1_p-00001'
    image_ext = 'jpg'
    results_directory = 'results_superPixels2'
    
    if os.path.exists(results_directory):
        print("This results directory already exist!")
    else:       
        os.mkdir(results_directory)
        
    images = fm.read_images(image_directory)
	
    
    for image in images:
        image, image_name, image_ext, image_type = image
        image = cv2.imread(os.path.join(image_directory,'.'.join((image_name, image_ext))))
        
        print("Processing: {} - {} - {}".format( image_name, image.shape, image_type))
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height,width,channels = image_hsv.shape
        num_superpixels = 100;  # SEEDS Number of Superpixels
        num_levels = 4;         # SEEDS Number of Levels
        prior = 2;              # SEEDS Smoothing Prior
        num_histogram_bins = 5; # SEEDS histogram bins
        double_step = False;    # SEEDS two steps
        region_size = 20;       # SLIC/SLICO/MSLIC/LSC average superpixel size
        ruler = 15.0;           # SLIC/MSLIC smoothness (spatial regularization)
        ratio = 0.075;          # LSC compactness
        min_element_size = 25;  # SLIC/SLICO/MSLIC/LSC minimum component size percentage
        num_iterations = 10;    # Iterations
        
        
        seeds = cv2.ximgproc.createSuperpixelSEEDS(width, height,channels, num_superpixels, num_levels, prior, num_histogram_bins)
        image_seg = np.zeros((height,width,channels), np.uint8)
        image_seg[:] = (0,0,255)
        seeds.iterate(image_hsv, num_iterations)
        
        labels = seeds.getLabels()
        
        num_label_bits = 2
        labels &= (1<<num_label_bits)-1
        labels *= 1<<(16-num_label_bits)
        
        
        mask = seeds.getLabelContourMask(False)
        
        # stitch foreground & background together
        mask_inv = cv2.bitwise_not(mask)
        result_bg = cv2.bitwise_and(image, image, mask=mask_inv)
        result_fg = cv2.bitwise_and(image_seg, image_seg, mask=mask)
        result = cv2.add(result_bg, result_fg)
        
        
       # show the image
        param="01_superPixels100"
        #cv2.imwrite(os.path.join(results_directory, str(image_name)+"_resBg_"+param+"."+str(image_ext)), result_bg)
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_resFg_"+param+"."+str(image_ext)), result_fg)
        
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), result)
        # cv2.namedWindow("Display window", cv2.WINDOW_FULLSCREEN )
        # cv2.imshow("Display window", image)
        # k = cv2.waitKey(0)
        
