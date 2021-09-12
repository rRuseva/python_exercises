import numpy as np
import cv2


image_path = 'assets\\'
image_name = '2017-06-10-20-45-25'
image_ext = '.jpg'
results_path = 'result3\\'

img = cv2.imread(image_path + image_name + image_ext)
# cv2.imshow('Original', img)

kernel = np.ones((3, 3), 'uint8')

erode_img = cv2.erode(img, kernel, cv2.BORDER_REFLECT, iterations=1)
cv2.imwrite(results_path + image_name + '_erode' + image_ext, erode_img)

dilate_img = cv2.dilate(img, kernel, iterations=2)
cv2.imwrite(results_path + image_name + '_dilate' + image_ext, dilate_img)


new_img = cv2.erode(img, kernel, cv2.BORDER_REFLECT, iterations=1)
new_img = cv2.morphologyEx(new_img, cv2.MORPH_OPEN, kernel)
new_img = cv2.dilate(new_img, kernel, iterations=2)
cv2.imwrite(results_path + image_name + '_morph' + image_ext, new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
