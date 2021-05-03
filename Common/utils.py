import cv2

def print_matInfo(name, image):     #다루고자 하는 이미지가 어떤 타입인지 알고자 하면 이용
    if image.dtype == 'uint8':
        mat_type = "CV_8U"
    elif image.dtype == 'int8':
        mat_type = "CV_8S"
    elif image.dtype == 'uint16':
        mat_type = "CV_16U"
    elif image.dtype == 'int16':
        mat_type = "CV_16S"
    elif image.dtype == 'float32':
        mat_type = "CV_32F"
    elif image.dtype == 'float64':
        mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    ## depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))

def put_string(frame, text, pt, value, color=(120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)    # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기

def contain_pts(p, p1, p2):
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]