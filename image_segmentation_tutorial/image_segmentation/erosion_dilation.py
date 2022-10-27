# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 09:33:45 2022

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
    results_directory = 'results_erosion_dilation4'
    
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
        
        kernel3 = np.ones((3, 3), np.uint8)
        kernel5 = np.ones((5, 5), np.uint8)
        kernel7 = np.ones((7, 7), np.uint8)
        
        # for i in range (1,6):
        #     image_erode3 = cv2.erode(image_grey,kernel3, iterations=i)
        #     param="0{}_erode_k3".format(i)
        #     cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_erode3)
            
        #     image_dilate3 = cv2.dilate(image_grey,kernel3, iterations=i)
        #     param="0{}_dilate_k3".format(i)
        #     cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_dilate3)
            
            
        #     image_erode5 = cv2.erode(image_grey,kernel5, iterations=i)
        #     param="0{}_erode_k5".format(i)
        #     cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_erode5)
            
        #     image_dilate5 = cv2.dilate(image_grey,kernel5, iterations=i)
        #     param="0{}_dilate_k5".format(i)
        #     cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_dilate5)

        #     image_dilate7 = cv2.dilate(image_grey,kernel7, iterations=i)
        #     param="0{}_dilate_k7".format(i)
        #     cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_dilate7)
                
            # image_erode7 = cv2.erode(image_dilate7,kernel7, iterations=i)
            # param="0{}_erode_k7".format(i)
            # cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), image_erode7)
        it = 5 
        image_dilate7 = cv2.dilate(image_grey,kernel7, iterations=it)
        image_erode7 = cv2.erode(image_dilate7,kernel7, iterations=it)
        
        param="0{}_dilate-erode_k7".format(2)
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_00"+param+"."+str(image_ext)), image_grey)
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_01"+param+"."+str(image_ext)), image_dilate7)
        cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_02"+param+"."+str(image_ext)), image_erode7)
       # show the image
# =============================================================================
#         param="02_sift-strContrastThr"
#         cv2.imwrite(os.path.join(results_directory, str(image_name)+"_res_"+param+"."+str(image_ext)), sift_image)
# =============================================================================
        # cv2.namedWindow("Display window", cv2.WINDOW_FULLSCREEN )
        # cv2.imshow("Display window", image)
        # k = cv2.waitKey(0)