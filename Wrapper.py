#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2


#read matching 1 txt file

with open('./P3Data/matching1.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if( i != 0):
            data = lines[i]
            data = data.split()
    

      
            print(data)
            points = data[0]
            r = data[1]
            g = data[2]
            b = data[3]
           
            imgx = data[4]
            imgy = data[5]

            rgb = [r, g, b]

            print("RGB ", rgb)
            #print("points ", points)


