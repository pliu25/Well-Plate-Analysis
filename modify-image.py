import cv2
import matplotlib.pyplot as plt

plate =  cv2.imread("colorplate.png", cv2.IMREAD_COLOR)

cv2.rectangle(plate, (0, 0), (1570, 537), (0, 0, 0), -1)
for x in range(72,1574, 130):
    cv2.circle(plate, (x, 70), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 200), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 330), 35, (255, 255, 255), -1)
    cv2.circle(plate, (x, 460), 35, (255, 255, 255), -1)

cv2.imwrite(f'plate_mask.png', plate)

org_plate =  cv2.imread("colorplate.png", cv2.IMREAD_COLOR)

for r, row in enumerate(org_plate):
        for c, value in enumerate(row):
            if plate[r][c][0] != 0:
                plate[r][c][0] = org_plate[r][c][0]
            if plate[r][c][1] != 0:
                plate[r][c][1] = org_plate[r][c][1]
            if plate[r][c][2] != 0:
                plate[r][c][2] = org_plate[r][c][2]

cv2.imwrite(f'plate_color_grid.png', plate)
cv2.imshow(f'plate_color_grid.png', plate)

dilution = []

for i in range(0, 12):
     dilution.append(2**i)
print(dilution)

for r, row in enumerate(plate):
    for c, value in enumerate(row):
         for pixel in range(len(row)):
              column = 
#column = 1st pixel of each row etc       

cv2.waitKey() 
cv2.destroyAllWindows() 