import sys

import cv2

input_path = sys.argv[1]

img = cv2.imread(input_path)
contrast_factor = 0.2

clahe = cv2.createCLAHE(clipLimit=-20, tileGridSize=(8, 8))
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
lab = cv2.merge((clahe.apply(l), a, b))
result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

cv2.imshow("Change contrast", result)
cv2.waitKey()

