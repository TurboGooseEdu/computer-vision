import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale", result)
cv2.waitKey()
