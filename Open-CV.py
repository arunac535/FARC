from cv2 import EVENT_LBUTTONDOWN, IMREAD_GRAYSCALE, cvtColor, destroyAllWindows
import numpy as np
import cv2
# loads the image in color
img1 = cv2.imread("C:\\Users\\aruna\\Pictures\\Nitro\\p1.jpg")
# loads the image in grayscale
img2 = cv2.imread(
    "C:\\Users\\aruna\\Pictures\\Nitro\\p1.jpg", IMREAD_GRAYSCALE)
# # creation of geometric shapes
# img3 = cv2.rectangle(img1, (0, 0), (469, 469), (255, 0, 0), 5)
# img3 = cv2.circle(img3, (200, 200), 50, (0, 255, 0), 5)
# img3 = cv2.arrowedLine(img3, (480, 480), (640, 640), (255, 0, 0), 5)
# font = cv2.FONT_HERSHEY_TRIPLEX
# img3 = cv2.putText(img3, "Open-CV", (700, 700), font, 4, (255, 255, 255), 5)
# # displays the images that were loaded
# cv2.imshow("pic1", img1)
# cv2.imshow("pic2", img2)
# cv2.imshow("pic3", img3)
# cv2.waitKey(0) & 0xFF

# # saving the images that were loaded
# cv2.imwrite("p1_copy.png", img1)
# cv2.imwrite("p2_copy.png", img2)
# cv2.imwrite("p3_copy.png", img3)


# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("video1.mp4", fourcc, 20.0, (640, 480))

# while(cap.isOpened()):
#     # Reading the video file
#     ret, frame = cap.read()
#     if (ret == True):
#         # Saving the video file
#         out.write(frame)
#         cv2.imshow("video2", frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# # handling mouseclicks


# def click_event(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, ",", y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strxy = str(x)+"," + str(y)
#         cv2.putText(img1, strxy, (x, y), font, 1, (255, 255, 255), 2)
#         cv2.imshow("image", img1)
# # Using right mouse click to display rgp value of a pixel
#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img1[y, x, 0]
#         green = img1[y, x, 1]
#         red = img1[y, x, 2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         stbgr = str(blue)+"," + str(green)+","+str(red)
#         cv2.putText(img1, stbgr, (x, y), font, 1, (0, 255, 255), 2)
#         cv2.imshow("image", img1)


# cv2.imshow("image", img1)
# cv2.setMouseCallback("image", click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

        

def click_event3(event, x3, y3, flag, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x3,",",y3)
        stab=str(x3)+","+str(y3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,stab,(x3,y3),font,2,(255,255,255),2)
        def click_event2(event, x2, y2,flag,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x2, ",", y2)
                strxy = str(x2)+","+str(y2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img1,strxy, (x2, y2), font, 1, (255, 255, 255), 2)
            cv2.line(img1,(x2,y2),(x3,y3),(255,255,255),5)
        cv2.imshow("image",img1)
                # # for rectangle
                # # cv2.rectangle(img1,(x2,y2),(x3,y3),(255,0,0),5)


cv2.imshow("image", img1)
cv2.setMouseCallback("image", click_event3)
cv2.waitKey(0)
cv2.destroyAllWindows()
