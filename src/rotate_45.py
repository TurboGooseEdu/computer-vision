import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
result = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imshow("Rotate 45", result)
cv2.waitKey()
