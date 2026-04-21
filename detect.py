import cv2
import tensorflow as tf
import numpy as np

print("TensorFlow version:", tf.__version__)

image_path = "sample.png"
img = cv2.imread(image_path)

if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 이미지를 RGB로 변환
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 평균 픽셀값 계산
mean_value = np.mean(img_rgb)

# 밝기에 따라 라벨 지정
if mean_value > 120:
    label = "Bright Object"
else:
    label = "Dark Object"

# 이미지에 텍스트 출력
cv2.putText(img, label, (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2)

# 결과 저장
cv2.imwrite("result_practice.jpg", image)
print("결과 저장 완료")