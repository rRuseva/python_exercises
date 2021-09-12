import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
import argparse

print(sys.version)
print(cv2. __version__ )


print("hello openCV")
image_path = 'assets\\'
image_name = 'IMG_20200919_094007'
image_ext = '.jpg'
results_path = 'results\\'

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True, help="path to the image")
	args = vars(ap.parse_args())

	image = cv2.imread(args["image"])
	image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("original image", image)
	cv2.imshow("grey image", image_grey)


	hist_grey = cv2.calcHist([image_grey], [0], None, [256], [0,256])

	# plt.figure()
	# plt.axis("off")
	# plt.imshow()
	# plt.show()

	# plot the histogram
	plt.figure()
	plt.title("Grayscale Histogram")
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	plt.plot(hist_grey)
	plt.xlim([0, 256])
	plt.show()


	k = cv2.waitKey(0)