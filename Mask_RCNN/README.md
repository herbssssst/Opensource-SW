# Mask R-CNN for Object Detection and Segmentation

**2023-2 오픈소스 SW 실습 강의 1번째 과제 (MaskRCNN)** <br/>
📢 Anaconda를 이용한 환경 구축 <br/>
📢 공식 Github의 Baloon 예제 Train / Test 적용 <br/>

<br/><br/>

## 1. 환경 구축
### 1.1 Anaconda 가상환경 생성 (python 3.7)
```
conda create -n MaskRCNN python==3.7
conda activate MaskRCNN
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

**❗ 아래 가중치 파일을 다운 받아 Mask_RCNN 폴더로 이동 ❗**<br/>
https://github.com/matterport/Mask_RCNN/releases/download/v2.1/mask_rcnn_balloon.h5

<br/>

**❗ 아래 데이터셋 파일을 다운 받아 Mask_RCNN/model/ballon/datesets 폴더로 이동 ❗**<br/>
https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip 

<br/><br/>

## 2. 실행
### 2.1 samples/balloon 폴더로 이동하여 아래 명령어 실행 - 다운로드 받은 가중치 파일로 실행하는 방법
```
python balloon.py --dataset ../../model/balloon/datasets --weights ../../mask_rcnn_balloon.h5
--image <이미지 상대 경로> splash
```
### 2.2 samples/balloon 폴더로 이동하여 아래 명령어 실행 - 가중치 파일을 생성하여 실행하는 방법
```
python balloon.py train --dataset ../../model/balloon/datasets --weights=coco
```

<img width="1280" alt="스크린샷 2023-11-23 212700" src="https://github.com/herbssssst/OpenSource-SW-Telegram-Bot/assets/98319466/2f9db0d9-e773-417a-9bf8-ee044144a79c"> <br/>

```
python balloon.py --dataset ../../model/balloon/datasets --weights ../../logs/mask_rcnn_balloon_01.h5
--image <이미지 상대 경로> splash
```

<br/><br/>

## 3. 결과
### 3.1 train 예제
![train1](https://github.com/herbssssst/Opensource-SW/assets/98319466/d756635b-32d1-4c07-9dcd-39dd7296ff9d)
![train2](https://github.com/herbssssst/Opensource-SW/assets/98319466/11726609-abb1-4207-8285-2e1dbfcda82d)

<br/>

### 3.2 var 예제
![var1](https://github.com/herbssssst/Opensource-SW/assets/98319466/f4b88257-a5a2-4f8d-ac1b-5fa14d7394b9)
![var2](https://github.com/herbssssst/Opensource-SW/assets/98319466/4205945e-11c5-4813-a80a-a9577794bf4b)

<br/><br/><br/>

**참고 :** https://hdongle.tistory.com/202 <br/>
**참고 :** https://reyrei.tistory.com/21

<br/><br/><br/>

기존에 Mask_RCNN를 포크하였던 레포를 현 레포에 합쳐 이러한 형태로 정리한 것을 알립니다.<br/>
원본 : https://github.com/matterport/Mask_RCNN 

