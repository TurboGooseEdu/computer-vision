import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
brightness_offset = 100

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
lim = 255 - brightness_offset
v[v > lim] = 255
v[v <= lim] += brightness_offset

final_hsv = cv2.merge((h, s, v))
result = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("Change brightness", result)
cv2.waitKey()
