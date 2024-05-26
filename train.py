import os
from ultralytics import YOLO

# data.yaml 파일의 경로
data_yaml_path = os.path.join(os.path.dirname(__file__), 'data.yaml')

# YOLOv8s 모델 로드
model = YOLO('yolov8s.pt')

# 모델을 데이터로 훈련. 에포크 = 10
model.train(data=data_yaml_path, epochs=10)