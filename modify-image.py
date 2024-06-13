import cv2
import matplotlib.pyplot as plt
import math 

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

yellow = []
red=[]
blue=[]
green = []

color_mask = cv2.imread("plate_color_grid.png", cv2.IMREAD_COLOR)
for x in range(73, 1570, 130):
     temp_list = []
     radius = 65
     for y in range(12, 140):
          for circle in range(x-radius, x+radius):
               if color_mask[y][circle][0] != 0 and color_mask[y][circle][1] != 0 and color_mask[y][circle][2] != 0:
                    temp_list.append(color_mask[y][circle][0])
                    temp_list.append(color_mask[y][circle][1])
                    temp_list.append(color_mask[y][circle][2])
     if temp_list==[]:
          yellow.append(0)
     else:
          yellow.append(math.trunc((sum(temp_list))/len(temp_list)))
print("yellow", yellow)

for x in range(73, 1570, 130):
     temp_list = []
     radius = 65
     for y in range(140, 268):
          for circle in range(x-radius, x+radius):
               if color_mask[y][circle][0] != 0 and color_mask[y][circle][1] != 0 and color_mask[y][circle][2] != 0:
                    temp_list.append(color_mask[y][circle][0])
                    temp_list.append(color_mask[y][circle][1])
                    temp_list.append(color_mask[y][circle][2])
     if temp_list==[]:
          red.append(0)
     else:
          red.append(math.trunc((sum(temp_list))/len(temp_list)))
print("red", red)
for x in range(73, 1570, 130):
     temp_list = []
     radius = 65
     for y in range(268, 396):
          for circle in range(x-radius, x+radius):
               if color_mask[y][circle][0] != 0 and color_mask[y][circle][1] != 0 and color_mask[y][circle][2] != 0:
                    temp_list.append(color_mask[y][circle][0])
                    temp_list.append(color_mask[y][circle][1])
                    temp_list.append(color_mask[y][circle][2])
     if temp_list==[]:
          blue.append(0)
     else:
          blue.append(math.trunc((sum(temp_list))/len(temp_list)))
print("blue", blue)
for x in range(73, 1570, 130):
     temp_list = []
     radius = 65
     for y in range(396, 537):
          for circle in range(x-radius, x+radius):
               if color_mask[y][circle][0] != 0 and color_mask[y][circle][1] != 0 and color_mask[y][circle][2] != 0:
                    temp_list.append(color_mask[y][circle][0])
                    temp_list.append(color_mask[y][circle][1])
                    temp_list.append(color_mask[y][circle][2])
     if temp_list==[]:
          green.append(0)
     else:
          green.append(math.trunc((sum(temp_list))/len(temp_list)))
print("green", green)

hist_dict = {}
grayscale_mask = cv2.imread("plate_color_grid.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite(f"grayscale_mask.png", grayscale_mask)
cv2.imshow(f"plate_color_grid.png", grayscale_mask)

for i in range(48):
     hist_dict[i] = dict()
     hist_dict[i]["B"] = [] 
     hist_dict[i]["G"] = [] 
     hist_dict[i]["R"] = []
     hist_dict[i]["gray"] = [] 

pt_x = 73
pt_y = 77
radius = 65
num = -1

for x in range(4):
     pt_x = 73
     for y in range(12):
        num+=1
        start_x = pt_x - radius 
        end_x = pt_x + radius 
        start_y = pt_y - radius 
        end_y = pt_y + radius 

        B_tempdict = {}
        G_tempdict = {}
        R_tempdict = {}
        gray_tempdict = {}

        for i in range(0, 256):
            hist_dict[num]["B"].append(i)
            hist_dict[num]["G"].append(i)
            hist_dict[num]["R"].append(i)
            hist_dict[num]["gray"].append(i)

            B_tempdict[i] = 0
            G_tempdict[i] = 0
            R_tempdict[i] = 0
            gray_tempdict[i] = 0
    
        for r, row in enumerate(color_mask):
            for c, value in enumerate(row):
                if c>= start_x and c<= end_x and r>=start_y and r<=end_y:
                    if color_mask[r][c][0] != 0 and color_mask[r][c][1] != 0 and color_mask[r][c][2] != 0:
                        B_tempdict[value[0]]+=1
                        G_tempdict[value[1]]+=1
                        R_tempdict[value[2]]+=1
                        gray_tempdict[grayscale_mask[r][c]]+=1
        for i in range(0, 256):
            hist_dict[num]["B"][i] = B_tempdict[i]
            hist_dict[num]["G"][i] = G_tempdict[i]
            hist_dict[num]["R"][i] = R_tempdict[i]
            hist_dict[num]["gray"][i] = gray_tempdict[i]
        pt_x+=129
     pt_y+=129

x = range(256)
row = -1
col = -1
num = -1

fig, axs = plt.subplots(4, 12)
for i in range(4):
    row += 1
    col = -1
    for i in range(12):
        col += 1
        num += 1
        y = hist_dict[num]["B"]
        axs[row, col].plot(x, y, "blue")
        y = hist_dict[num]["G"]
        axs[row, col].plot(x, y, "green")
        y = hist_dict[num]["R"]
        axs[row, col].plot(x, y, "red")
        y = hist_dict[num]["gray"]
        axs[row, col].plot(x, y, "gray")



fig.supxlabel('Color Value')
fig.supylabel("Value Frequency")
fig.suptitle("Well Color Channel Histograms")
plt.show() 

print("hist_dict", hist_dict)


          

# for x in range(73, 1570, 130):
#      radius = 65
#      pixelB_list = []
#      pixelG_list = []
#      pixelR_list = []
#      blue_list = [0] * 256
#      green_list = [0] * 256
#      red_list = [0] * 256
#      for y in range(12, 537):
#          for circle in range(x-radius, x+radius):
#             if color_mask[y][circle][0] != 0 and color_mask[y][circle][1] != 0 and color_mask[y][circle][2] != 0:
#                  pixelB_list.append(color_mask[y][circle][0])
#                  pixelG_list.append(color_mask[y][circle][1])
#                  pixelR_list.append(color_mask[y][circle][2])
#                  for value in range(len(blue_list)):
#                     blue_list[value] = pixelB_list.count(value)
#      print(pixelB_list)
#print(pixelB_list)              
# for r, row in enumerate(plate):
#     for c, value in enumerate(row):
#          for pixel in range(len(row)):
#               column = 
#column = 1st pixel of each row etc       



fig = plt.figure(figsize=(10, 5.4))
ax2 = fig.add_subplot(111)
plt.plot(dilution, yellow, color="yellow")
plt.plot(dilution, red, color="red")
plt.plot(dilution, blue, color="blue")
plt.plot(dilution, green, color="green")
plt.title("Well Plate Analysis: Correlation Between Color and Dilution", loc='center')
plt.xlabel("Dilution Factor")
plt.ylabel("Average RGB Value")
plt.savefig("avg_rgb_value.png")
plt.show() 
cv2.waitKey() 
cv2.destroyAllWindows() 