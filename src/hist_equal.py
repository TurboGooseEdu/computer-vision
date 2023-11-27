import cv2
import sys

input_path = sys.argv[1]
img = cv2.imread(input_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = cv2.equalizeHist(gray)

cv2.imshow("Equalized histogram", result)
cv2.waitKey()
