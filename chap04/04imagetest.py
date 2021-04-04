import cv2
from Common.utils import print_matInfo      #공통적으로 쓰는 파일 모아두고 불러오기

title1, title2 = "gray2grey", "gray2color"  #윈도우 이름
gray2gray = cv2.imread("images/read_color.jpg", cv2.IMREAD_GRAYSCALE)    #영상 파일 적재
gray2color = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)

if (gray2gray is None or gray2color is None) :   #예외처리 - 영상 파일 읽기 여부 조사
    raise Exception("영상파일 읽기 에러")

# 행렬 내 한 화소 값 표시
print("행렬 좌표 (100, 100) 화소값")
print("%s %s" % (title1, gray2gray[100, 100]))
print("%s %s\n" % (title2, gray2color[100, 100]))

print_matInfo(title2, gray2color)

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

## 행렬을 영상 파일로 저장
cv2.imwrite("images/write_test1.jpg", gray2color)                   # 디폴트는 95
cv2.imwrite("images/write_test2.jpg", gray2color, params_jpg)       # 지정 화질로 저장
cv2.imwrite("images/write_test3.jpg", gray2color, params_png)
cv2.imwrite("images/write_test4.jpg", gray2color)                   # BMP 파일로 저장

cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)

# read_grey.jpg 를 출력해보면,
# 시각적으로 보면 차이가 없는데 100,100의 화소값을 보면 grey는 한 바이트에 대한 값이 저장되어져 있고 color로 읽으면 한 바이트에 대한 세 개의 값을 포함함.
# Red, Green, Blue 값을 통일하면 gray값으로 나옴

