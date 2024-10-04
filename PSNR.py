import math
import cv2
import numpy as np
size=128
original1 = cv2.imread("C:\\Users\\AMIRTH\\Desktop\\Cyber\\resultsets\\recovered_watermark.jpg")
original=cv2.resize(original1,(size, size))
contrast = cv2.imread("C:\\Users\\AMIRTH\\Desktop\\Cyber\\resultsets\\recovered_watermark 3.jpg")

def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d = psnr(original, contrast)
print(d)
