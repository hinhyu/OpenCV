import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200                              #행,열 모드. 그 값을 200으로 초기화

title1, title2 = 'Position1', 'Position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)            #윈도우 이동
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400, 400)
cv2.resizeWindow(title2, 400, 400)

cv2.waitKey(0)
cv2.destroyAllWindows()
