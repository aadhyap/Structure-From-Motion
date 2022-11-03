#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from GetInlierRANSAC import GetInlierRANSAC
from EssentialMatrixFromFundamentalMatrix import EssentialMatrixFromFundamentalMatrix
from ExtractCameraPose import ExtractCameraPose
from LinearTriangulation import LinearTriangulation
from DisambiguateCameraPose import DisambiguateCameraPose


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
            twos = 0
            total = j = 6
            while j  < total + lenpoints  + 1:
                ID = data[j]
                if(ID == "2"):
                    twos = twos + 1
                img_u = float(data[j + 1])
                img_v = float(data[j + 2])
                j = j + 3
                points_data[ID] = [img_u, img_v]


            matching_1[rgb] = points_data

    print(matching_1)

img1 = cv2.imread("./P3Data/1.png")

#Now choose 8 correspondances
#img1 needs 8 and its corresponding image, (lets say 2)



#FundamentalMatrix = EstimateFundamentalMatrix(matching_1)
F = GetInlierRANSAC(matching_1, "2")
print("Final F ", F.getF())
Essential = EssentialMatrixFromFundamentalMatrix(F.getF())
K = Essential.getK() # instrinsic parameters
print("Essential Matrix ", Essential.getEssential())

#Get camera poses
CameraPoses = ExtractCameraPose(Essential.getEssential()).getCameraPoses()
print("Camera Poses ", CameraPoses)




w= LinearTriangulation(K, CameraPoses, matching_1, "2")
worldpoints = w.getWorldPoints()


removeCameraPose = DisambiguateCameraPose(CameraPoses, worldpoints)
bestCP = removeCameraPose.getbestCP()

print("best CP ", bestCP)


print("All World Points ")
#print(worldpoints)







