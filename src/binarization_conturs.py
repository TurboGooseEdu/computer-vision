import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

ret, threshold_image = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(threshold_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 256), 3, cv2.LINE_AA, hierarchy, 1)

cv2.imshow("Contours on binarized picture", img)
cv2.waitKey()
