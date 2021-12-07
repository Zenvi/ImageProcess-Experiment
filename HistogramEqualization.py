import cv2
import numpy as np
from matplotlib import pyplot as plt
# 直方图均衡函数
def Equalization_Histogram (img):
    return cv2.equalizeHist(img)



# 测试上边的函数
if __name__ == '__main__':

    test_img = cv2.imread('./png_files/1/FILE15.png', 0)

    equalized_test_img = Equalization_Histogram(test_img)

    cv2.namedWindow("equalized",0)
    cv2.namedWindow("original",0)
    cv2.imshow('equalized', equalized_test_img)
    cv2.imshow('original', test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


