import cv2, os
import numpy as np

img_path = 'images/kakao.jpg'
filename, ext = os.path.splitext(os.path.basename(img_path))
ori_img = cv2.imread(img_path)

src = [] #전역변수 지정, 점을 넣어놓음

# mouse callback handler
def mouse_handler(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONUP:  #왼쪽 마우스 클릭시 (클릭하고 떼면)
    img = ori_img.copy()    #img에 오리지널 이미지를 카피

    src.append([x, y]) #전역변수에 x,y 좌표 저장

    for xx, yy in src:
      cv2.circle(img, center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)
    # 클릭시 그 지점에 초록색 점으로 표시
    cv2.imshow('img', img)  #그 이미지를 보여줌

    # perspective transform
    if len(src) == 4:   #src에 들어있는 점이 4개 여야  perspective transform실행
      src_np = np.array(src, dtype=np.float32)  #src 변수 전부다 32비트 float으로 변경후 src_np에 넣음
    # 가로 세로 길이 계산
      width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
      height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

      dst_np = np.array([   #왼쪽 위는 (0,0)인 직사각형의 좌표
        [0, 0],
        [width, 0],
        [width, height],
        [0, height]
      ], dtype=np.float32)

      M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
      result = cv2.warpPerspective(ori_img, M=M, dsize=(width, height))

      cv2.imshow('result', result)
      cv2.imwrite('./result/%s_result%s' % (filename, ext), result)

# main
cv2.namedWindow('img')  #윈도우 이름 지정
cv2.setMouseCallback('img', mouse_handler)  #윈도우에 마우스 핸들러를 콜백함수로 전달

cv2.imshow('img', ori_img)
cv2.waitKey(0)