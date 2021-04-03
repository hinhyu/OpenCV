import numpy as np
import cv2


def onChange(pos):  # 트랙바 핸들러
    global img, title
    # 트랙바의 값 받아오기
    # 트랙바 이름, 윈도우 창 이름
    r = cv2.getTrackbarPos('R', title)
    g = cv2.getTrackbarPos('G', title)
    b = cv2.getTrackbarPos('B', title)
    img[:] = (b, g, r)
    cv2.imshow(title, img)


# 마우스 입력 값에 따라 어떤 동작을 실행할 것인지 지정하는 함수
# event : 마우스 이벤트 타입
# x, y : 마우스 이벤트의 x, y좌표
# flags : 마우스 이벤트가 발생할 때 키보드 또는 마우스 상태
# param : 콜백 함수에 전달된 데이터(마우스 이벤트)
def onMouse(event, x, y, flags, param):
    global title, pt                            # 전역 변수 참조

    if event == cv2.EVENT_LBUTTONDOWN:

        if flags & cv2.EVENT_FLAG_CTRLKEY:          # Ctlr과 마우스 왼쪽 버튼을 이용하고 두개의 점을 클릭하여 원을 그리시오.
            if pt[0] < 0:
                pt = (x, y)  # 시작 좌표 지정
                cv2.circle(img, pt, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
                cv2.imshow(title, img)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))
                cv2.circle(img, pt, radius, red, 2)
                cv2.imshow(title, img)
                pt = (-1, -1)  # 시작 좌표 초기화

        elif flags & cv2.EVENT_FLAG_SHIFTKEY:       # Shift와 마우스 왼쪽 버튼을 이용하고 두개의 점을 클릭하여 직선을 그리시오.
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(img, pt, 1, 0, 2)  # 직선의 시작점(2화소 원) 표시
                cv2.imshow(title, img)
            else:
                cv2.line(img, pt, (x, y), orange, 2)
                cv2.imshow(title, img)
                pt = (-1, -1)  # 시작 좌표 초기화
        elif flags & cv2.EVENT_FLAG_ALTKEY:         # Alt와 마우스 왼쪽 버튼을 이용하고 두개의 점을 클릭하여 사각형을 그리시오.
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(img, pt, 1, 0, 2)  # 사각형의 시작점(2화소 원) 표시
                cv2.imshow(title, img)
            else:
                cv2.rectangle(img, pt, (x, y), blue, 2)
                cv2.imshow(title, img)
                pt = (-1, -1)  # 시작 좌표 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Alt와 마우스 오른쪽 버튼을 이용하고 두개의 점을 클릭하여 내부를 칠한 사각형을 그리시오.
        if flags & cv2.EVENT_FLAG_ALTKEY:
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(img, pt, 1, 0, 2)  # 사각형의 시작점(2화소 원) 표시
                cv2.imshow(title, img)
            else:
                cv2.rectangle(img, pt, (x, y), violet, -1)
                cv2.imshow(title, img)
                pt = (-1, -1)  # 시작 좌표 초기화

        #Ctrl과 마우스 오른쪽 버튼을 이용하고 두개의 점을 클릭하여 내부를 칠한 원을 그리시오.
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(img, pt, 1, 0, 2)  # 사각형의 시작점(2화소 원) 표시
                cv2.imshow(title, img)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))
                cv2.circle(img, pt, radius, brown, -1)
                cv2.imshow(title, img)
                pt = (-1, -1)  # 시작 좌표 초기화

    cv2.imshow(title, param[0])

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)    	# 색상 선언
olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
orange, cyan = (0, 165, 255), (255, 255, 0)

# 하얀 배경 생성
img = np.zeros((512, 512, 3), np.uint8) + 255

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, img)  # 이미지 보여주기

# img란 GUI창위에 onMouse란 콜백 함수를 이용하여, 데이터 전달하기
# [img] : onMouse란 콜백 함수에 전달할 데이터
# 마우스 이벤트가 입력되면 사전에 작성한 함수를 불러와서 작동
cv2.setMouseCallback(title, onMouse, [img])  # 마우스 콜백 함수

# 트랙바 생성
# 트랙바 이름, 윈도우 창 이름, 최소값, 최대값, 콜백 함수
cv2.createTrackbar('R', title, 0, 255, onChange)
cv2.createTrackbar('G', title, 0, 255, onChange)
cv2.createTrackbar('B', title, 0, 255, onChange)

# 트랙바 위치 초기화
# 트랙바 이름, 위노우 창 이름, 초기값
cv2.setTrackbarPos('R', title, 0)
cv2.setTrackbarPos('G', title, 0)
cv2.setTrackbarPos('B', title, 0)

cv2.waitKey()
cv2.destroyAllWindows()
