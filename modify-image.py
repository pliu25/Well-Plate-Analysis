import cv2

plate =  cv2.imread("colorplate.png", cv2.IMREAD_COLOR)

cv2.rectangle(plate, (0, 0), (1570, 537), (0, 0, 0), -1)
for x in range(72,1574, 130):
    cv2.circle(plate, (x, 70), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 200), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 330), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 460), 35, (255, 255, 255), -1)

cv2.imwrite(f'plate_mask.png', plate)
cv2.imshow(f'plate_mask.png', plate)

cv2.waitKey() 
cv2.destroyAllWindows() 