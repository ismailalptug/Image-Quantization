import numpy as np
import cv2


def quantizeImage(image, q):
    quaLevel = q
    new_img = np.uint8(np.floor(np.double(image)/(256/quaLevel)))
    norm_image = cv2.normalize(new_img, None, 0, 255, norm_type=cv2.NORM_MINMAX)
    cv2.imshow("Quantized", norm_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
