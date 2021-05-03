import cv2
import numpy as np
#파이썬 OpenCV 프로젝트

# ---① 설정 값 셋팅
exp = 0.5       # 볼록, 오목 지수 (오목 : 0.1 ~ 1, 볼록 : 1.1~)
scale = 1           # 변환 영역 크기 (0 ~ 1)

img = cv2.imread('images/matplot.jpg')
rows, cols = img.shape[:2]

# 매핑 배열 생성 ---②
mapy, mapx = np.indices((rows, cols),dtype=np.float32)

# 좌상단 기준좌표에서 -1~1로 정규화된 중심점 기준 좌표로 변경 ---③
mapx = 2*mapx/(cols-1)-1
mapy = 2*mapy/(rows-1)-1

# 직교좌표를 극 좌표로 변환 ---④
r, theta = cv2.cartToPolar(mapx, mapy)

# 왜곡 영역만 중심확대/축소 지수 적용 ---⑤
#r[r< scale] = r[r<scale] **exp
#k1, k2, k3 = 0.5, 0.2, 0.0	# Barrel 왜곡
k1, k2, k3 = -0.3, 0.0, 0.0	# 핀쿠션 왜곡
r = r*(1 + k1*(r**2) + k2*(r**4) + k3*(r**6))

# 극 좌표를 직교좌표로 변환 ---⑥
mapx, mapy = cv2.polarToCart(r, theta)

# 중심점 기준에서 좌상단 기준으로 변경 ---⑦
mapx = ((mapx + 1)*cols-1)/2
mapy = ((mapy + 1)*rows-1)/2

# 재매핑 변환
distorted = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

cv2.imshow('origin', img)
cv2.imshow('distorted', distorted)

cv2.waitKey(0)