import cv2
import numpy as np
from matplotlib import pyplot as plt


def book_Find(book_path):
    MIN_MATCH_COUNT = 10

    detector = cv2.xfeatures2d.SIFT_create()

    FLANN_INDEX_KDITREE = 0
    flannParam = dict(algorithm=FLANN_INDEX_KDITREE, tree=5)
    searchParam = dict(checks=50)
    flann = cv2.FlannBasedMatcher(flannParam, searchParam)

    # 책 이미지
    trainImg = cv2.imread(book_path, 0)
    trainKP, trainDesc = detector.detectAndCompute(trainImg, None)

    cam=cv2.VideoCapture(0)
    ret, QueryImgRGB=cam.read()
    #QueryImgRGB = cv2.imread("files/1.jpg")
    QueryImg=cv2.cvtColor(QueryImgRGB, cv2.COLOR_BGR2GRAY)
    cam.release()
    # 책장 이미지 RGB ver, Grey ver
    queryKP, queryDesc = detector.detectAndCompute(QueryImg, None)

    matches = flann.knnMatch(queryDesc, trainDesc, k=2)

    # 특징 매칭
    good = []
    for m, n in matches:
        if (m.distance < 0.7 * n.distance):
            good.append(m)

    # 판별
    if (len(good) > MIN_MATCH_COUNT):
        tp = []
        qp = []
        for m in good:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp, qp = np.float32((tp, qp))
        H, status = cv2.findHomography(tp, qp, cv2.RANSAC, 3.0)
        h, w = trainImg.shape
        trainBorder = np.float32([[[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]])
        queryBorder = cv2.perspectiveTransform(trainBorder, H)
        cv2.polylines(QueryImgRGB, [np.int32(queryBorder)], True, (0, 255, 0), 5)

        # 직사각형 박스추가된 이미지 생성
        new_path = book_path[5:]
        cv2.imwrite('files/new/' + new_path, QueryImgRGB)
        return 'files/new/' + new_path

    else:
        return "None"

def book_Match(books, book):
    max_g = 0
    cnt = 0
    i = -1
    for book_m in books:
        path = book_m.book_image

        detector = cv2.xfeatures2d.SIFT_create()

        FLANN_INDEX_KDITREE = 0
        flannParam = dict(algorithm=FLANN_INDEX_KDITREE, tree=5)
        searchParam = dict(checks=50)
        flann = cv2.FlannBasedMatcher(flannParam, searchParam)

        # 책 이미지
        trainImg = cv2.imread(path, 0)
        trainKP, trainDesc = detector.detectAndCompute(trainImg, None)

        #? 오류
        QueryImgRGB=cv2.imread(book)
        QueryImg=cv2.cvtColor(QueryImgRGB, cv2.COLOR_BGR2GRAY)
        queryKP, queryDesc = detector.detectAndCompute(QueryImg, None)

        matches = flann.knnMatch(queryDesc, trainDesc, k=2)

        # 특징 매칭
        good = []
        for m, n in matches:
            if (m.distance < 0.7 * n.distance):
                good.append(m)
        if len(good) > max_g:
            i = cnt
            max_g = len(good)
            cnt = cnt + 1

    return i