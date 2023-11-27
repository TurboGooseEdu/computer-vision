import numpy as np

import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

kernel = np.ones((5, 5), 'uint8')
result = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Dilate', result)
cv2.waitKey()
