#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2
from EstimateFundamentalMatrix import EstimateFundamentalMatrix


#read matching 1 txt file



with open('./P3Data/matching1.txt') as f:

    lines = f.readlines()
    lengthLines = len(lines)
    matching_1 = {}
    for i in range(lengthLines):
        if( i != 0):
            points_data = {}
            data = lines[i]
            data = data.split()
    

      
            print(data)
            lenpoints = int(data[0])
            r = data[1]
            g = data[2]
            b = data[3]
           
            imgx = float(data[4])
            imgy = float(data[5])

            rgb = tuple([r, g, b, imgx, imgy])




            #data of other points start after data[5]

            total = j = 6
            while j  < total + lenpoints  + 1:
                ID = data[j]
                img_u = float(data[j + 1])
                img_v = float(data[j + 2])
                j = j + 3
                points_data[ID] = [img_u, img_v]


            matching_1[rgb] = points_data

    print(matching_1)

#Now choose 8 correspondances
#img1 needs 8 and its corresponding image, (lets say 2)

eight_points_data = {}

for keys in matching_1:
    if "2" in matching_1[keys]:
        print(matching_1[keys]["2"])
        currentimg = tuple([keys[3], keys[4]])
        eight_points_data[currentimg] = matching_1[keys]["2"]
    if(len(eight_points_data) >= 8):
        break

print("eight points ", eight_points_data)

FundamentalMatrix = EstimateFundamentalMatrix(eight_points_data)





