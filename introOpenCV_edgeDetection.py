# intro to OpenCV - image processing
# tutorial from:
# https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/

# import imutils
import cv2
import sys
import os


image_path = 'assets\\'
# image_name = 'IMG_20200919_094007'
image_name = 'tetris2'
image_ext = '.jpg'
results_path = 'results\\'

# read image file
image = cv2.imread(image_path + image_name + image_ext)

(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))


# roi = image[1060:1160, 2320:2420]
# show result images
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

# # cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)
# cv2.imshow("roi", roi)


# # rotation
# center = (w // 2, h // 2)
# M = cv2.getRotationMatrix2D(center, -45, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.namedWindow("OpenCV Rotation", cv2.WINDOW_NORMAL)
# cv2.imshow("OpenCV Rotation", rotated)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow("Gray", cv2.WINDOW_NORMAL)
# cv2.imshow("Gray", gray)

edged = cv2.Canny(gray, 50, 150)

# cv2.namedWindow("Edged", cv2.WINDOW_NORMAL)
# cv2.imshow("Edged", edged)

thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
# cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
# cv2.imshow("Thresholding", thresh)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
output = image.copy()
for c in contours:
    cv2.drawContours(output, [c], -1, (0, 0, 255), 3)

print("{} objects found".format(len(contours)))
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.imshow("Contours", output)
cv2.waitKey(0)
