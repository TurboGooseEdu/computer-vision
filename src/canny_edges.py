import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Canny edges", edges)
cv2.waitKey()