import cv2
import numpy as np


if __name__ == "__main__":
    img_bgr = cv2.imread('Module_02_Exercise_M02EX01/dog.jpg', 1)

    gray_img_1 = np.stack(
        [img_bgr.min(axis=2), img_bgr.max(axis=2)]).mean(axis=0)
    gray_img_2 = img_bgr.mean(axis=2)
    gray_img_3 = 0.21*img_bgr[:, :, 2] + 0.72 * \
        img_bgr[:, :, 1] + 0.07*img_bgr[:, :, 0]

    cv2.imwrite('Module_02_Exercise_M02EX01/pic1.jpg', gray_img_1)
    cv2.imwrite('Module_02_Exercise_M02EX01/pic2.jpg', gray_img_2)
    cv2.imwrite('Module_02_Exercise_M02EX01/pic3.jpg', gray_img_3)

    print(gray_img_1[0][0])
    print(gray_img_2[0][0])
    print(gray_img_3[0][0])
