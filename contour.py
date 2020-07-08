import cv2

img = cv2.imread('image.png')

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(grayscale, 10, 10)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,0), 3)


area = []
for contour in contours:
    area.append(cv2.contourArea(contour))

corners = []
for contour in contours:    
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
    num_corner = len(approx)
    corners.append(num_corner)

triangle = []
quad = []
pentagon = []
hexagon = []
circle = []

centres = []

for contour in contours:
    M = cv2.moments(contour)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    centre = (x,y)
    centres.append(centre)

i = 0

for corner_num in corners:
    if corner_num == 3:
        triangle.append([area[i],i,centres[i]])
    elif corner_num == 4:
        quad.append([area[i],i,centres[i]])
    elif corner_num == 5:
        pentagon.append([area[i],i,centres[i]])
    elif corner_num == 6:
        hexagon.append([area[i],i,centres[i]])
    else:
        circle.append([area[i],i,centres[i]])
        
    i = i+1

def sorting(val):
    return val[0]
    
triangle.sort(key=sorting)
quad.sort(key=sorting)
pentagon.sort(key=sorting)
hexagon.sort(key=sorting)
circle.sort(key=sorting) 

shapes = triangle+quad+pentagon+hexagon+circle 

for index in range(len(shapes)-1):
    cv2.line(img, shapes[index][2], shapes[index+1][2], (0,0,0), 3)
    

#cv2.imshow('Gray', grayscale)
#cv2.imshow('Canny',canny)
cv2.imshow('Contour Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()