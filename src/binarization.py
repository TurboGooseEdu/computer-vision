import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
ret, threshold_image = cv2.threshold(img, 127, 255, 0)

cv2.imshow("Binarization", threshold_image)
cv2.waitKey()
