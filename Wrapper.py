#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2


#read matching 1 txt file



with open('./P3Data/matching1.txt') as f:

    lines = f.readlines()
    lengthLines = 3
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
           
            imgx = data[4]
            imgy = data[5]

            rgb = tuple([r, g, b, imgx, imgy])



            print("RGB ", rgb)
            #data of other points start after data[5]

            total = j = 6
            while j  < total + lenpoints  + 1:
                ID = data[j]
                img_u = data[j + 1]
                img_v = data[j + 2]
                j = j + 3
                print("j ", j)
                print(" total ", total + lenpoints)
                points_data[ID] = [img_u, img_v]
                print("points data", points_data)


            matching_1[rgb] = points_data

    print(matching_1)

#Now choose 8 correspondances
#img1 needs 8 and its corresponding image, (lets say 2)
for keys in matching_1:
    





