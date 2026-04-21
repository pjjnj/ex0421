import cv2
import numpy as np

image_path = "test.png"

img = cv2.imread(image_path)

if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

print("이미지 크기 출력:", img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean_value = np.mean(gray)

print("평균 밝기:", mean_value)
