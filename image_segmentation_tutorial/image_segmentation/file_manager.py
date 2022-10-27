import cv2
import sys
import os
import argparse
import re 
import pydicom as dicom

import numpy as np
from matplotlib import pyplot as plt


def read_images(image_directory):

	if not os.path.exists(image_directory):
		print("(>_<)  Oops! No such directory (-_-)  \n")
		return
	else: 
		print("reading image files in \"{}\" ...".format(image_directory))
	image_name = ''
	image_ext = 'png'
	images = []
	image_type = ''
	image_data = ''
	
	for filename in os.listdir(image_directory):
		filename_rel_path = os.path.join(image_directory,filename)
		if re.search("\\.|jpg|png|jepg",filename, re.I):
			name =  filename.split('.')
			image_name = name[0]
			image_ext = name[1]
			image_type = 'Color'
			image_data = cv2.imread(filename_rel_path)
			
		else:
			image_name = filename
			image_ext = 'png'
			ds = dicom.dcmread(filename_rel_path)
			image_type =  ds.PhotometricInterpretation  #usually dicom x-ray is MONOCHROME2
			if ds.pixel_array.any():
				### convert byte raw image data into uint8 in range [0,255]
				image_data = ds.pixel_array - np.min(ds.pixel_array)
				image_data = image_data / np.max(image_data)
				image_data = (image_data * 255).astype(np.uint8)		
		
		if image_data.any():
			images.append((image_data, image_name, image_ext, image_type))

	return(images)

if __name__ == '__main__':
	pass