import cv2
import numpy as np
import re

BLUE = 0
GREEN = 1
RED = 2

# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다
def get_chars (image, color):
    other_1 = (color + 1) % 3         # 다른 색
    other_2 = (color + 2) % 3         # 다른 색
    c = image[:, :, other_1] == 255   # 다른 색 해당되면 제거
    # print("c1: ", c, "    다른 색 해당되면 제거")
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255   # 다른 색 해당되면 제거
    # print("c2: ", c, "    다른 색 해당되면 제거")
    image[c] = [0, 0, 0]
    c = image[:, :, color] < 170      # 겹치는 색 해당되면 제거
    # print("c3: ", c, "    겹치는 색 해당되면 제거")
    image[c] = [0, 0, 0]
    c = image[:, :, color] != 0       # 해당 색이면 흰색
    # print("c4: ", c, "    해당 색이면 흰색처리")
    image[c] = [255, 255, 255]
    return image


# 전체 이미지에서 왼쪽부터 단어별로 이미지를 추출합니다
def extract_chars (image):
    chars = []
    colors = [BLUE, GREEN, RED]
    for color in colors:
        image_from_one_color = get_chars(image.copy(), color)   # 색상 별로 모든 이미지 추출할 수 있도록 함함
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)  # 그레이 형태로 바꾼 이유는 쓰레쉬홀드 적용하기 위함임
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)  # 흑과 백으로 나누주는데 여기선 사실 컨투어를 찾기 위해 사용함
        # RETR_EXTERNAL 옵션으로 숫자의 외각을 기준으로 분리
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 일반적으로 컨투어를 찾을 때 먼저 쓰레쉬홀드를 거친 다음에 컨투어를 찾도록 만듦
        # 실제로 쓰레쉬홀드를 추출 하도록 만들면 각각의 숫자를 감싸는 형태로 쓰레쉬홀드들이 만들어짐

        for contour in contours:
            # 추출된 이미지 크기가 50 이상인 경우만 실제 문자 데이터인 것으로 파악
            area = cv2.contourArea(contour)
            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                roi = image_gray[y:y + height, x:x + width]
                chars.append((x, roi))

    chars = sorted(chars, key=lambda char: char[0])
    return chars


# 특정한 이미지를 (20 x 20) 크기로 Scaling 함
# roi가 제각각이기 때문에 모든 이미지를 다 동일한 크기로 리사이즈
def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float32) # 실제 knn 알고리즘 적용하기 위해서는 1차원 배열로 쭉 늘어뜨려야 하기 때문에 이렇게 크기를 그냥 400으로 바꿔주겠다는 거임
    # 실제로 머신러닝에서 다양한 분류 예제를 다룰 때는 이미지의 크기를 동일하게 하기 때문에 모든 숫자에 대해서 전부 다  동일한 크기를 가질 수 있도록 스케일링해줌


def remove_first_0(string):
    temp = []
    for i in string:
        if i == '+' or i == '-' or i == '*':  # 연산 기호 3개 밖에 없음
            temp.append(i)
    split = re.split('\*|\+|-', string)   # 연산 기호를 기준으로 각 문자열을 나눔
    i = 0
    temp_count = 0
    result = ""
    for a in split:  # 나우어진 문자를 하나씩 확인
        a = a.lstrip('0')  # 왼쪽에 오는 0들을 지움
        if a == '':  # 0 하나 남기는 부분임
            a = '0'
        result += a
        if i < len(split) - 1:
            result += temp[temp_count]  # 연산 기호 붙임
            temp_count = temp_count + 1
        i = i + 1
    return result

