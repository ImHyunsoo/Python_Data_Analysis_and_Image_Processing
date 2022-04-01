BLUE = 0
GREEN = 1
RED = 2

# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다
def get_chars (image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3
    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]
    return image