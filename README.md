# 나동빈님 Python_Data_Analysis_and_Image_Processing 강의 스터디

## 강좌 목표
* Python 을 이용하여 현실 세계의 다양한 실전 데이터를 처리해볼 수 있습니다
* Python 을 이용하여 웹에서 데이터를 가져와 분석하는 자동화 프로그램을 만들 수 있습니다
* Python 을 활용하여 이미지를 원하는 방식대로 변형하고 가공할 수 있습니다
* Python 을 활용하여 인증 시스템을 Hacking 할 수 있습니다
* 여러분이 하고 싶은 많은 것들을 할 수 있습니다
### [예시] 
1) 영화 사이트 리뷰 데이터를 수집을 통한 나만의 영화 추천 프로그램
2) 공모전 사이트 자동 크롤링 및 메일 알림 서비스
3) 가상화폐 가격 예측 시스템

## 활용 프로젝트 
1. 주요 웹 사이트에서 다양한 데이터를 수집하여 시각화해서 보여줄 거예요
2. 유명 라이브러리 해킹방어대회에서 등장한 Captcha 를 Hacking 해 볼 거예요## 배운 것
 Python 을 이용하여 현실 세계의 다양한 실전 데이터를 처리해볼 수 있습니다


## 배운 것
### 행렬과 Numpy
* 행렬은 컴퓨터의 메모리 구조, 표 형태의 데이터, 이미지 등을 표현할 수 있고, Numpy는 이 행렬을 효과적으로 처리할 수 있는 도구이며, 다양한 활용법을 익혔습니다.

### OpenCV 
* 영상 처리와 컴퓨터 비전을 위한 오픈소스 라이브러리로, 손쉽게 이미지를 다룰 수 있는 방법을 익혔습니다. 

### KNN 알고리즘
* K-Nearest Neighbot, KNN은 지도학습의 간단한 예로, 다양한 레이블의 데이터 중에서, 자신과 가까운 데이터를 찾아 자신의 레이블을 결정하는 방식입니다. 이후 Captcha 해킹할 때 숫자 이미지를 학습하여 수식의 각 숫자 및 연산 기호를 인식하는데 사용됩니다.

### Captcha 해킹
#### 1. 특정한 수식 사진을 OpenCV 로 처리하여 각 문자를 하나씩 분리합니다
##### 1) 데이터 수집과 분석
* 웹 브라우저를 통해 데이터를 수집합니다. 
<img src="https://user-images.githubusercontent.com/20950569/161182942-d709f322-519e-4719-b01b-b0ab05e10f52.png" width="400" height="140"/>

* 색상 추출기를 활용하여, 각 문자의 색상이 어떻게 구성되어 있는지 확인합니다.
<img src="https://user-images.githubusercontent.com/20950569/161183567-d838720c-8022-4040-b1e7-4d3a18a4a51a.png" width="400" height="140"/>

##### 2) 데이터 정제
* 색상별로 이미지를 추출합니다.
<img src="https://user-images.githubusercontent.com/20950569/161184288-a247ad1f-75aa-4472-831d-d810aba10970.png" width="400" height="140"/>
<img src="https://user-images.githubusercontent.com/20950569/161184404-032bb97f-d494-452a-a244-d91a67f59fde.png" width="400" height="140"/>
<img src="https://user-images.githubusercontent.com/20950569/161184140-8d67143a-1ef7-4ef4-ba54-4fb992309c0d.png" width="400" height="140"/>
<img src="https://user-images.githubusercontent.com/20950569/161184145-30be672c-89e8-4812-813c-6d37a4b1401c.png" width="400" height="140"/>

##### 3) 트레이닝 데이터 만들기
* 전체 이미지에서 왼쪽부터 단어별로 추출한 후 이미지를 (20 x 20)크기로 통일합니다.

<img src="https://user-images.githubusercontent.com/20950569/161185365-10b96e39-3467-42a8-a8ea-93b2ea5d5742.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185368-169ff5c6-7c82-4521-9b88-1d975dd04f3e.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185369-927bdf25-eb4f-4a3a-b1ef-2fbea7ff106e.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185370-98758efe-3fd5-4d14-a2c4-587871d3f6b3.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185374-51eee4e0-d67f-42fd-92e9-1d16948d8851.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185376-9f828bb6-9772-4792-b0ad-05799e002521.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185378-80aa6659-8b5e-4fa8-8de2-9fc0eeded5b3.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185380-2e642ac5-de97-4f3c-b30f-2da826e01e7a.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185381-9f247724-3ea6-4683-b4ae-e49b7a34198c.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185382-40f0917b-a3e4-4dda-bbcd-aef4d6c6c570.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185361-6a1bd244-2110-4c44-b93f-c0fa8dcadafa.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185362-6117f9f7-e776-45c1-a736-ad84fc27beec.png" width="20" height="20"/> <img src="https://user-images.githubusercontent.com/20950569/161185364-fcd54d92-7944-4446-acaf-2e37d7633baf.png" width="20" height="20"/>



#### 2. 분리된 각 문자가 어떤 문자에 해당하는지 인식합니다
#### 3. 인식된 수식을 계산하여 정답을 도출합니다
