import cv2
import sys
import os

print(sys.version)
print(cv2. __version__ )


print("hello openCV")
image_path = 'assets\\'
image_name = '2017-06-10-20-45-25'
image_ext = '.jpg'
results_path = 'results\\'

### read image file
curr_img = cv2.imread(image_path + image_name + image_ext)
# cv2.imshow("My_Image", curr_img)

### resizing image by scale factor
scale = 60 
width = int(curr_img.shape[1]*scale/100)
height = int(curr_img.shape[0]*scale/100)

resized_img = cv2.resize(curr_img, (width,height), cv2.INTER_AREA)
# cv2.imshow("Resized_Image", resized_img)
cv2.imwrite(results_path + image_name + '_resized' + image_ext, resized_img)

###-----------------------------------------------------------------###
###--------------------- Switching color space ---------------------###
### switching to greyscale
grey_img = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(results_path + image_name + '_grey' + image_ext, grey_img)

### switching to YCbCr color space
ycbcr_img = cv2.cvtColor(curr_img, cv2.COLOR_BGR2YCR_CB)
cv2.imwrite(results_path + image_name + '_ycbcr' + image_ext, ycbcr_img)

### switching to LAB color space
lab_img = cv2.cvtColor(curr_img, cv2.COLOR_BGR2LAB)
cv2.imwrite(results_path + image_name + '_lab' + image_ext, lab_img)

### switching to HLS color space
hls_img = cv2.cvtColor(curr_img, cv2.COLOR_BGR2HLS)
cv2.imwrite(results_path + image_name + '_HLS' + image_ext, hls_img)

### switching to HSV color space
hsv_img = cv2.cvtColor(curr_img, cv2.COLOR_BGR2HSV)
cv2.imwrite(results_path + image_name + '_HSV' + image_ext, hsv_img)

###-----------------------------------------------------------------###


# Wait for a keypress
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()