import cv2

# Haar Cascade 파일 로드 (OpenCV 기본 제공)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 웹캠 실행 (0 = 기본 카메라)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 흑백 변환 (성능 향상)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,   # 이미지 축소 비율
        minNeighbors=5     # 검출 정확도 조절
    )

    # 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 화면 출력
    cv2.imshow('Face Detection', frame)

    # q 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 처리
cap.release()
cv2.destroyAllWindows()