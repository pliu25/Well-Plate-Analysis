import cv2

plate =  cv2.imread("colorplate.png", cv2.IMREAD_GRAYSCALE)

cv2.circle(plate, (145, 200), 100, 255, -1)

cv2.imwrite("colorplate.png", plate) 

cv2.imshow(f'colorplate.png', plate)

cv2.waitKey() 
cv2.destroyAllWindows() 