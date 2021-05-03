import numpy as np, cv2
import cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("V_max", "result")
    th[1] = cv2.getTrackbarPos("V_min", "result")

    ## OpenCV 이진화 함수 이용 - 상위 값과 하위 값 제거
    _, result = cv2.threshold(HSV_img, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)

    cv2.imshow("result", result)

BGR_img = cv2.imread("images/fruits.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
if BGR_img is None: raise Exception("영상 파일 읽기 오류")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV) # 컬러 공간 변환
hue = np.copy(HSV_img[:,:,0])                      # hue 행렬에 색상 채널 복사

th = [100, 255]                                     # 트랙바로 선택할 범위 변수
cv2.namedWindow("result")
cv2.createTrackbar("V_max", "result", th[0], 255, onThreshold)
cv2.createTrackbar("V_min", "result", th[1], 255, onThreshold)
onThreshold(th[0])                                 # 이진화 수행
#cv2.imshow("BGR_img", BGR_img)
cv2.waitKey(0)



