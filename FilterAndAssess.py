import numpy as np
import cv2



# 图像与图像的差距的计算函数，你仅需要修改或者改进这个函数
def calculate_diff(ori_img, noisy_img):

    # 直方图计算函数
    def GetHist(img):
        img = img.flatten()
        img = img.tolist()
        hist = []
        for i in range(0, 256):
            hist.append(img.count(i))
        return hist

    return np.sum(np.sqrt( (np.array(GetHist(noisy_img)) - np.array(GetHist(ori_img))) ** 2 ) ) / 256


def assess(ori_img, noisy_img, method='mean'):

    diff_before = calculate_diff(ori_img, noisy_img)

    # 进行滤波操作
    if method == 'mean':
        filtered_img = cv2.blur(noisy_img, (3, 3))
    elif method == 'gaussian':
        filtered_img = cv2.GaussianBlur(noisy_img, (3, 3), 0)
    elif method == 'median':
        filtered_img = cv2.medianBlur(noisy_img, 3)
    else:
        print('Wrong method! Try again.')
        return

    diff_after = calculate_diff(ori_img, filtered_img)

    return diff_before-diff_after, filtered_img


if __name__ == '__main__':

    cv2.namedWindow("Original", 0)
    cv2.namedWindow("Before filtering", 0)
    cv2.namedWindow("Filtered", 0)

    noisy_img_path = './png_files/2/Pulse_Noised_Image.png'
    ori_img_path = './png_files/2/Original.png'

    noisy_img = cv2.imread(noisy_img_path, 0)
    ori_img = cv2.imread(ori_img_path, 0)

    for filter_name in ['mean', 'gaussian', 'median']:
        effect, filtered_img = assess(ori_img, noisy_img, method=filter_name)
        print('nosiy image name: {}, filter name: {}, effect: {}'.format(noisy_img_path.split('/')[-1], filter_name, effect))

        cv2.imshow("Original", ori_img)
        cv2.imshow("Before filtering", noisy_img)
        cv2.imshow("Filtered", filtered_img)

        if cv2.waitKey(0)& 0xFF == ord('d'):
            continue

    cv2.destroyAllWindows()