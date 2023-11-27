import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
result = cv2.flip(img, 0)

cv2.imshow("Reflect bottom", result)
cv2.waitKey()
