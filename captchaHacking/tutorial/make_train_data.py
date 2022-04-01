import os
import cv2
import utils

# training_data 폴더 생성 및 그 내부에 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 폴더 생성
image = cv2.imread("4.png")
chars = utils.extract_chars(image)  # 색상별로 숫자 이미지를 추출함

for char in chars:         # 각각의 숫자 이미지에 대해서
    cv2.imshow('Image', char[1])   # 일단 그 이미지를 보여주고
    input = cv2.waitKey(0)
    resized = cv2.resize(char[1], (20, 20))  # 크기를 20 x 20 으로 바꾸어서 저장함

    # 사용자가 직접 숫자를 보고  어떤 숫자인지 레이블링함, 0 ~ 9
    # 예) 9 입력하면 '9'라는 폴더 안에 이미지 파일이 저장됨
    # +, - , * 에 대해서는 각각 a, b, c를 입력해서 해당 특수문자로 분류될 수 있도록 함, 10, 11, 12
    if input >= 48 and input <= 57:
        name = str(input - 48)
        file_count = len(os.listdir('./training_data/' + name + '/'))   # 폴더 안 에 파일 갯수
        cv2.imwrite('./training_data/' + str(input - 48) + '/' + str(file_count + 1) + '.png', resized)
    elif input == ord('a') or input == ord('b') or input == ord('c'):
        name = str(input - ord('a') + 10)
        file_count = len(os.listdir('./training_data/' + name + '/'))
        cv2.imwrite('./training_data/' + name + '/' + str(file_count + 1) + '.png', resized)