import cv2
import imutils


def is_contour_bad_large(c):
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    area = cv2.contourArea(c)
    #if(len(approx) == 4):
        #print("rect\n",approx,area)
    # the contour is 'bad' if it is not a rectangle
    return (area > 20000)

def is_contour_bad_small(c):
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    area = cv2.contourArea(c)
    #if(len(approx) == 4):
        #print("rect\n",approx,area)
    # the contour is 'bad' if it is not a rectangle
    return (area < 20000)


image = cv2.imread('./set.jpg')

image = imutils.resize(image, width=1000)
cv2.imshow("go", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
ret, mask = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
edged = cv2.Canny(gray, 50, 100)
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
    # if the contour is bad, draw it on the mask
    if is_contour_bad_large(c):
        cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)
edged = cv2.Canny(mask, 50, 100)
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
    # if the contour is bad, draw it on the mask
    if is_contour_bad_small(c):
        cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)

edged = cv2.Canny(mask, 50, 100)
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.imshow('Masked2', mask)
# if the contour is bad, draw it on the mask




mask = cv2.GaussianBlur(mask, (5, 5), 0)
res = cv2.bitwise_and(image, image, mask=mask)
for c in cnts:
    if(cv2.contourArea(c) < 20000):
        cv2.imshow('Masked3', res)
        cv2.drawContours(res, [c], -1, (0, 0, 255), 2)
        print(cv2.contourArea(c))


cv2.imshow('Masked3', res)
#save the folling outputs
cv2.waitKey(0)
cv2.destroyAllWindows()
