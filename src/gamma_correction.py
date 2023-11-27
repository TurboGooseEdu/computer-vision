import numpy as np
import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

gamma = 2.2
table = [((i / 255) ** (1 / gamma)) * 255 for i in range(256)]
table = np.array(table, np.uint8)
result = cv2.LUT(img, table)

cv2.imshow("Gamma correction", result)
cv2.waitKey()
