import numpy as np
import cv2
import utils
import requests
import shutil
import time

FILE_NAME = "trained.npz"

# 학습된 데이터를 불러와서 변수 형태로 담음
# 각 글자의 1 x 400 데이터와 정답 (0 ~ 9, +, *)
with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

# knn 객체를 만들어서 실제로 학습까지 시킨 것임
# 사실 이 데이터 자체가 그냥 학습된 데이터 그 자체라고 말할 수 있음
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

def check(test, train, train_labels):
    # 가장 가까운 k개의 글자를 찾아, 어떤 숫자에 해당하는지 찾음 (테스트 데이터 개수에 따라서 조절)
    # 각 숫자 이미지가 똑같아서 1개만 찾아도 됨
    ret, result, neighbours, dist = knn.findNearest(test, k=1)
    return result

def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_chars(image)  # 그 파일을 왼쪽에서부터 차례대로 각각의 이미지를 이 캐릭터에 담음
    result_string = ""
    for char in chars:
        # cv2.imshow('Image Gray', char[1])
        # cv2.waitKey(0)
        matched = check(utils.resize20(char[1]), train, train_labels) # 모든 이미지에 대해서 크기를 400으로 쭉 늘어뜨린 다음에,
        # 실제로 트레인 데이터 중에서 그 이미지가 어떤 걸로 분류가 되는지를 찾은 다음에, 이 matched에 담음
        # print(matched)

        if matched < 10:
            result_string += str(int(matched))
            continue
        if matched == 10:
            matched = '+'
        elif matched == 11:
            matched = '-'
        elif matched == 12:
            matched = '*'
        result_string += matched  # 예) "7532+312" 같이 문자열로 결과 반환하기 위함함    return result_string
    return result_string

# print(get_result("1.png"))

host = "http://192.168.0.7:10000"
url = "/start"  # 먼저 이 스타트 url로 접속하기 위함

# target_images 라는 폴더 생성
with requests.Session() as s:  # 이제 해당 웹사이트에 접속을 해서
    answer = ''  # 맨 첨에 빈 문자열 넣어주는 이유: 첨에 start 버튼 눌렀을 때, 어떤 파라미터 정답에 대한 내용을 보내 줄 필요가 없기 때문
    for i in range(0, 100):  # 실제 문제에서는 문제를 총 100번 풀어야 됐었음
        # 이제 각각의 이미지를 다운로드 받아서 수식을 푼 다음에 다시 서버로 전송하는 그 시간을 계산하기 위함
        start_time = time.time()
        params = {'ans': answer}  # 'ans' 이 파라미터에 값을 넣어서 서버로 전송하기 위함, 다음 번에 호출이 이루어질 때는 answer가 서버에 전달됨

        # 정답을 파라미터에 달아서 전송하여, 이미지 경로를 받아옴
        response = s.post(host + url, params)   # 해당 url에 포스트 방식으로 접속을 해서
        print('Server Retrun: ' + response.text)   # 이제 서버로부터 리턴 값을 받아옴
        if i == 0:   # 맨 첨 같은 경우는 start 라서 바로 이미지 url 정보가 나옴
            returned = response.text  # 그 이미지에 해당하는 url 정보를 그대로 받아옴
            image_url = host + returned  # 이미지 url을 초기화 해줬기 때문에 이 url로부터 이미지 다운로드 받아서 그 이미지의 수식을 계산할 수 있음
            url = '/check'   # 접속할 url을 체크로 바꿔줌, 정답 코드를 제출할 그 url이 바로 체크이기 때문
        else:
            returned = response.json()   # json 형태로 서버로부터 데이터가 들어옴
            image_url = host + returned['url']  # 그 정보는 이 url에 해당 이미지 url 정보가 담겨있음, 이미지 url 정보를 갱신할 수 있도록 하면 됨

        print('Problem ' + str(i) + ': ' + image_url)  # 다음 문제에 해당하는 image_url 출력함
        # 해당 이미지 파일을 서버로부터 다운 받음(특정 폴더에 다가)
        response = s.get(image_url, stream=True)  # 이렇게 손쉽게 이미지 파일을 다운로드 받을 수 있음
        target_image = './target_images/' + str(i) + '.png'  # 다운받은 이미지를 타겟 이미지라는 폴더 안에다가 저장하기 위함
        with open(target_image, 'wb') as out_file:  # 이미지 파일을 해당 폴더 경로에다가 저장함
            shutil.copyfileobj(response.raw, out_file)
        del response

        # 다운로드 받은 이미지 파일을 분석하여 답을 도출함
        answer_string = get_result(target_image)  # 해당 이미지에 대한 스트링 값 구함
        print('String: ' + answer_string)
        answer_string = utils.remove_first_0(answer_string)  # 수식을 정상적으로 인식하기 위해서 각각의 수에 대해서 앞쪽에 있는 0들을 제거할 수 있도록 정제
        answer = str(eval(answer_string))  # eval() 이용해서 해당 수식을 계산함
        print('Answer: ' + answer)
        print("--- %s seconds ---" % (time.time() - start_time))
