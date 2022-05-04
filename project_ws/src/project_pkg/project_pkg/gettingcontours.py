import cv2
import numpy as np


def contourSquares(img, id):
    img = cv2.resize(img, (0, 0), None, .50, .50)

    #### contrast
    alpha = 1.9 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    value = 50
    mat = np.ones(adjusted.shape,dtype = 'uint8')*value
    subtract = cv2.subtract(adjusted,mat)

    ##Making the image clearer

    hsv = cv2.cvtColor(subtract, cv2.COLOR_BGR2HSV)

    # Blue
    if (id==1):
        mask = cv2.inRange(hsv, (85,120,100), (110,255,255))
    # Green
    if (id==2):
        mask = cv2.inRange(hsv, (35,120,100), (80,255,255))
    # Red
    if (id==3):
        mask1 = cv2.inRange(hsv, (0,120,100), (15,255,255))
        mask2 = cv2.inRange(hsv, (160,120,100), (180,255,255))
        mask = cv2.bitwise_or(mask1, mask2)
    # Yellow
    if (id==4):
        mask = cv2.inRange(hsv, (20,120,100), (35,255,255))

    # find the colors within the boundaries
    

    kernel = np.ones((7,7),np.uint8)
    # Remove unnecessary noise from mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Segment only the detected region
    #segmented_img = cv2.bitwise_and(img, img, mask=mask)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(subtract, contours, -1, (0, 0, 255), 3)

    threshold = 100

    src_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    src_gray = cv2.blur(src_gray, (3,3))
    canny_output = cv2.Canny(src_gray, threshold, threshold * 2)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])


    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)


    for i in range(len(contours)):
        color = (255,0,255)
        if cv2.contourArea(contours[i]) > 1000:
            cv2.drawContours(drawing, contours_poly, i, color)
            cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
            return 1


    # while True:

    
        # cv2.imshow("rectangles", drawing)
        # cv2.imshow("original", output)
        # cv2.imwrite('output.jpeg', output)
    return 0

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

# contourSquares(cv2.imread('C:/Users/aleskola/Documents/RAS/RAS-Open-project/project_ws/src/project_pkg/images/green.jpeg'),1)