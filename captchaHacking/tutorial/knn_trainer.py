import os
import cv2
import numpy as np

file_names = list(range(0, 13)) # 0 ~ 9, 10, 11, 12
train = []
train_labels = []

# 파일 읽어옴
for file_name in file_names:
    path = './training_data/' + str(file_name) + '/'
    file_count = len(os.listdir(path))  # 해당 이미지 파일이 몇개 있는지 확인
    for i in range(1, file_count + 1):
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray)                # 훈련할 이미지들
        train_labels.append(file_name)    # 훈련할 labels

x = np.array(train)
train = x[:, :].reshape(-1, 400).astype(np.float32) # 학습 시키기 위해서는 1차원 배열로 만들어 줘야함 (20 x 20) -> 400
train_labels = np.array(train_labels)[:, np.newaxis] # 레이블도 1차원 배열 형태로 바꿔줌
print(train.shape)
print(train_labels.shape)
print(train_labels)
np.savez("trained.npz", train=train, train_labels=train_labels) # 해당 트레인 데이터 정보를 파일 형태로 저장함