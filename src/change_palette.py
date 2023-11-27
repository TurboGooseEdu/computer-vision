import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

db, dg, dr = 30, 10, 10
b, g, r = cv2.split(img)
result = cv2.merge((b + db, g + dg, r + dr))

cv2.imshow("Change color palette", result)
cv2.waitKey()
