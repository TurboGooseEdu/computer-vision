import cv2
import sys

input_path = sys.argv[1]

img = cv2.imread(input_path)

sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(img, None)
result = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("SIFT features", result)
cv2.waitKey()
