import cv2
import math
import numpy as np
points=[]

def circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,255),2)
        if (len(points)!=0):
            cv2.arrowedLine(img,tuple(points[0]),(x,y),(0,255,0),3)
        points.append([x,y])
        cv2.imshow('image', img)
        print(points)
        if (len(points) == 3):
            degrees= findangle()
            print(np.abs(degrees))



def findangle():
    a=points[-2]
    b=points[-3]
    c=points[-1]
    m1=slope(b,a)
    m2=slope(b,c)
    angle=math.atan((m2-m1)/1+m1*m2)
    angle=round(math.degrees((angle)))


def slope(p1,p2):
    return(p2[1]-p1[1]/p2[0]-p1[0])


img=np.zeros((512,512,3),np.uint8)

cv2.imshow('image',img)
cv2.setMouseCallback('image',circle)
cv2.imwrite("Amazing_drawing.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
















#
#
# import cv2
# import numpy as np
# import math
# points=[]
# def circle(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),6,(255,0,0),-1)
#         if(len(points)!=0):
#             cv2.arrowedLine(img,tuple(points[0]),(x,y),(255,0,0),3)
#         points.append([x,y])
#         print(points)
#         if(len(points)==3):
#             degrees=findangle()
#             print(degrees)
#
#     cv2.imshow('image',img)
#
# def findangle():
#     a=points[-2]
#     b=points[-3]
#     c=points[-1]
#     m1=slope(b,a)
#     m2=slope(b,c)
#     angle=math.atan((m2-m1)/1+m1*m2)
#     angle=round(math.degrees((angle)))
#
#
#
# def slope(p1,p2):
#     return (p2[1]-p1[1]/p2[0]-p1[0])
#
#
#
#
#
#
#
# img=np.zeros((512,512,3),np.uint8)
# cv2.imshow('image',img)
# cv2.setMouseCallback('image',circle)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#


















