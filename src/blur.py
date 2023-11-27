import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

result = cv2.blur(img, ksize=(10, 10))

cv2.imshow("", result)
cv2.waitKey()
