# Mask R-CNN for Object Detection and Segmentation

### 2023-2 오픈소스 SW 실습 강의 1번째 과제 (MaskRCNN Balloon)
📢 Anaconda를 이용한 환경 구축 <br/>
📢 공식 Github의 Baloon 예제 Train / Test 적용 <br/>

<br/><br/>

## 1. 환경 구축
### 1.1 Anaconda 가상환경 생성 (python 3.7)
```
conda create -n tf115 python==3.7
conda activate tf115
```
### 1.2 git clone
```
https://github.com/herbssssst/Mask_RCNN.git
```
### 1.3 필요한 라이브러리 설치
```
pip install keras==2.1.2
pip install tensorflow-gpu==1.15.5
pip install -U scikit-image==0.16.2
pip install protobuf==3.20.*
```
### 1.4 폴더 생성 및 dataset 다운로드
```
Mask_RCNN/model/balloon/datasets
                       /logs
```
<br/>
❗ 아래 파일을 다운받아 Mask_RCNN 폴더에 저장❗ <br/>
https://github.com/matterport/Mask_RCNN/releases/download/v2.1/mask_rcnn_balloon.h5
<br/>
❗ 아 파일을 다운받아 Mask_RCNN/model/balloon/datasets 폴더에 저장❗<br/>
https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip 


<br/><br/>

## 2. 실행
❗ samples/balloon 폴더로 이동항 아래 명령어 실행❗<br/>
```
python balloon.py --dataset ../../model/balloon/datasets --weights ../../mask_rcnn_balloon.h5 --logs ../../model/balloon/logs --image <이미지 상대 경로> splash
```
<br/><br/>

## 3. 결과
❗ train 예제❗<br/>
![train1](https://github.com/herbssssst/OpenSource-SW-Telegram-Bot/assets/98319466/d756635b-32d1-4c07-9dcd-39dd7296ff9d)
![train2](https://github.com/herbssssst/OpenSource-SW-Telegram-Bot/assets/98319466/11726609-abb1-4207-8285-2e1dbfcda82d)

<br/>

❗ var 예제❗<br/>
![var1](https://github.com/herbssssst/OpenSource-SW-Telegram-Bot/assets/98319466/ba24f33d-95f6-4547-a63e-0dec1c5cf05d)
![var2](https://github.com/herbssssst/OpenSource-SW-Telegram-Bot/assets/98319466/4205945e-11c5-4813-a80a-a9577794bf4b)
