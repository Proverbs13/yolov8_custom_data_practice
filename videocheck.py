from ultralytics import YOLO

# 사전 훈련된 YOLOv8s 모델 로드
model = YOLO("model_1.pt")

# - save=True: 결과 저장
# - imgsz=640: 입력 이미지의 크기 - 640x640
# - conf=0.3: 객체를 감지하기 위한 최소 확률 임계값 - 0.3
model.predict("testvideo.mp4", save=True, imgsz=640, conf=0.5)
#model.predict("testvideo2.mp4", save=True, imgsz=640, conf=0.5)
