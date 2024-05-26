# mlhw8
 yolov8 모델을 통한 커스텀 데이터 학습 ( 고양이, 텀블러, 모자)

 -결과 예시 영상은 "학습결과영상1.avi" 입니다. 
 ( runs-detect-predict-testvideo.avi와 동일 영상)
 
 -train.py 코드를 통해 학습을 진행합니다.

 -videocheck.py 코드를 통해 테스트 동영상을 yolo 모델로 객체 탐지를 돌린 영상을 얻을 수 있습니다. 
 ( runs-detect-predict 롤더가 추가됨, 안에 영상 포함)
 
 -dataset 폴더에 데이터셋이 저장되어 있습니다.
 
 -"model_1.pt"가 진행한 학습 모델의 가중치 파일을 가져온 것입니다.
 ( runs-detect-train-weights-best.pt와 동일 파일)
