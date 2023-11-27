import sys

import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

input_path = sys.argv[1]
img = cv2.imread(input_path)

increase_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 75, 155, 255])(range(256))
decrease_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 45, 95, 255])(range(256))
blue_ch, green_ch, red_ch = cv2.split(img)
red_ch = cv2.LUT(red_ch, increase_table).astype(np.uint8)
blue_ch = cv2.LUT(blue_ch, decrease_table).astype(np.uint8)
result = cv2.merge((blue_ch, green_ch, red_ch))

cv2.imshow("Make warmer", result)
cv2.waitKey()
