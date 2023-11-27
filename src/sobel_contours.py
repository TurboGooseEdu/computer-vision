import numpy as np

import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

kernel = np.array([[-1, 0, 1],  [-2, 0, 2],  [-1, 0, 1]])
result = cv2.filter2D(img, -1, kernel)

cv2.imshow("", result)
cv2.waitKey()
