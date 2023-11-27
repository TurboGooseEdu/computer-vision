import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)
(h, w, _) = img.shape
point = (w // 3, h // 4)

rotation_matrix = cv2.getRotationMatrix2D(point, 30, 1.0)
result = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imshow("Rotate 30 around point", result)
cv2.waitKey()
