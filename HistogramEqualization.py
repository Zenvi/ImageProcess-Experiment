import cv2
import numpy as np

# 直方图均衡函数
def Equalization_Histogram(img):
    '''
    函数的功能：对输入图片进行直方图均衡，并返回均衡后的图片
    函数的输入：img，类型为numpy.ndarray
    函数的返回值：new_img，类型为numpy.ndarray
    提示：你需要先计算一下函数的直方图，才能去做直方图均衡
    '''

    # 直方图计算函数
    def GetHist(img):
        img = img.flatten()
        img = img.tolist()
        hist = []
        for i in range(0, 256):
            hist.append(img.count(i))
        return hist

    hist = GetHist(img)

    pr = {}
    for i in range(len(hist)):
        pr[i] = hist[i] / (img.shape[0] * img.shape[1])

    tmp = 0
    for m in pr.keys():
        tmp += pr[m]
        pr[m] = int((len(hist)) * tmp)

    new_img = np.zeros(shape=(img.shape[0], img.shape[1]), dtype=np.uint8)

    for k in range(img.shape[0]):
        for l in range(img.shape[1]):
            new_img[k][l] = pr[img[k][l]]

    return new_img

# 测试上边的函数
if __name__ == '__main__':

    test_img = cv2.imread('./png_files/1/FILE3.png', 0)

    equalized_test_img = Equalization_Histogram(test_img)

    cv2.namedWindow("equalized",0)
    cv2.namedWindow("original",0)
    cv2.imshow('equalized', equalized_test_img)
    cv2.imshow('original', test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


