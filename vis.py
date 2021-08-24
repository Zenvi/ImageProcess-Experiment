import cv2
import numpy as np

image_path = './png_files/3/flower.png'

image = cv2.imread(image_path)



cv2.namedWindow('1', 0)
for i in range(3):
    cv2.imshow('1', image)

    cv2.waitKey(0)
cv2.destroyAllWindows()