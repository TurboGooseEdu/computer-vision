import numpy as np

import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
(h, w) = img.shape[:2]

M = np.float32([[1, 0, 10], [0, 1, 0]])
result = cv2.warpAffine(img, M, (h, w))

cv2.imshow("Shift right 10 px", result)
cv2.waitKey()
