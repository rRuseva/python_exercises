import cv2
import sys
import os
import numpy as np

print(sys.version)
print(cv2. __version__ )


print("hello openCV")
image_path = 'assets\\'
image_name = 'IMG_20200919_094007'
image_ext = '.jpg'
results_path = 'results\\'

### read image file
curr_img = cv2.imread(image_path + image_name + image_ext)
# cv2.imwrite(results_path + image_name + '_original' + image_ext, curr_img)

### averaging blur 
kernel = np.ones((5,5), np.float32)/25
avbl_img = cv2.filter2D(curr_img, -1, kernel)

cv2.imwrite(results_path + image_name + '_average' + image_ext, avbl_img)

### 
blur_img = cv2.blur(curr_img, (5,5))
cv2.imwrite(results_path + image_name + '_blur5x5' + image_ext, blur_img)

blur_img = cv2.blur(curr_img, (7,7))
cv2.imwrite(results_path + image_name + '_blur7x7' + image_ext, blur_img)


### Gaussian blur 
gBlur_img = cv2.GaussianBlur(curr_img, (5,5), 0)
cv2.imwrite(results_path + image_name + '_gaussian' + image_ext, gBlur_img)

gBlur_img = cv2.GaussianBlur(curr_img, (7,7), 0)
cv2.imwrite(results_path + image_name + '_gaussian7x7' + image_ext, gBlur_img)


### Median 
median_blur_img = cv2.medianBlur(curr_img, 5)
cv2.imwrite(results_path + image_name + '_median' + image_ext, median_blur_img)

### Bilateral
bilateral_blur_img = cv2.bilateralFilter(curr_img,9, 75, 75)
cv2.imwrite(results_path + image_name + '_bilateral' + image_ext, bilateral_blur_img)


# Wait for a keypress
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()