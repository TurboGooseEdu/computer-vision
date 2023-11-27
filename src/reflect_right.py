import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
result = cv2.flip(img, 1)

cv2.imshow("Change contrast", result)
cv2.waitKey()
