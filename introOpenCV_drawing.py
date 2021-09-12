import cv2
import os
import sys
import numpy as np


print(sys.version)
print(cv2. __version__)


print("hello openCV")
image_path = 'assets\\'
image_name = 'IMG_20200919_094007'
image_ext = '.jpg'
results_path = 'results4\\'

# read image file
curr_img = cv2.imread(image_path + image_name + image_ext)
# cv2.imwrite(results_path + '0_' + image_name + '_original' + image_ext, curr_img)

img_width = int(curr_img.shape[1])
img_height = int(curr_img.shape[0])
print("original image id: ", id(curr_img))

new_img = np.empty_like(curr_img)
new_img[:] = curr_img
print("new image id: ", id(new_img))

# Drawing  a line
cv2.line(new_img, (0, 0), (img_width, img_height), (255, 0, 0), 5)
cv2.imwrite(results_path + image_name + '_line' + image_ext, new_img)

# show result images
# cv2.namedWindow("Drawned_Image", cv2.WINDOW_NORMAL)
# cv2.imshow("Drawned_Image", new_img)
# cv2.namedWindow("Original_Image", cv2.WINDOW_NORMAL)
# cv2.imshow("Original_Image", curr_img)

new_img[:] = curr_img
cv2.rectangle(new_img, (int(img_width / 4), int(img_height / 4)), (int(img_width * 3 / 4), int(img_height * 3 / 4)), (0, 0, 255), 5)
pts = np.array([[int(img_width / 2), int(img_height / 5)], [int(img_width * 4 / 5), int(img_height / 2)], [int(img_width / 2), int(img_height * 4 / 5)], [int(img_width / 5), int(img_height / 2)]], np.int32)
cv2.polylines(new_img, [pts], True, (255, 255, 0), 3)
cv2.imwrite(results_path + image_name + '_rect' + image_ext, new_img)

new_img[:] = curr_img
cv2.circle(new_img, (int(img_width / 2), int(img_height / 2)), int(img_width / 4), (0, 255, 0), 5)
cv2.imwrite(results_path + image_name + '_circle' + image_ext, new_img)

# save a copy of the original image to prove it was not affected by the programm
cv2.imwrite(results_path + '1_' + image_name + '_original' + image_ext, curr_img)
print("original image id: ", id(curr_img))


# # Wait for a keypress
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()
