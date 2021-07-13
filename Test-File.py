import cv2
from Quantization import quantizeImage

inimg = cv2.imread('PEPPER.TIF',0)
cv2.imshow("Original", inimg)
quantizeImage(inimg, 4)