#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math


class GetInlierRANSAC:
    def __init__(self, matchings, imgID):
        self.get8points(matchings, imgID)

    def RANSAC(self, eightpointdata, imgpoints):
        print("eightpoints generated ", eightpointdata)
        n = [[0]]
        bestres = 0
        for i in range(30):
            #choose 8 coorespondance 

            Fund = EstimateFundamentalMatrix(eightpointdata)
            F = Fund.getMatrix()
            S = [] #inliers

            #iterate through all match points
            for keys in imgpoints:
                x2 = imgpoints[keys][0]
                y2 = imgpoints[keys][1]
                z2 = 1
                image2 = np.array([x2, y2, z2])

                x = keys[0]
                y = keys[1]
                z = 1
                image1 = np.array([x, y, z])

                print("F ", F)
                print("image 2 ", image2)
                res1 = np.dot(image2, F)
                res = np.dot(res1, image1)

                print("res ", res)

                

                if(res < 0.05):
                    S.append([keys, imgpoints[keys]])
                    print("res that made it ", res)
            
            if (len(S) > len(n[0])):
                bestres = res
                n[0] = S

        print("FINAL ", S)
        print("Lenght ", len(S))
        print("RES Final ", bestres)








    def get8points(self, matchings, imgID):
        


        eight_points_data = {}
        imgpoints = {}
        size_matchings = 0
        count = 0
        
        for keys in matchings:
            if imgID in matchings[keys]:
                size_matchings += 1
           
                

        rangenums =  sample(range(0, size_matchings), 8) 
        for keys in matchings:
            if imgID in matchings[keys]:
                count += 1
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]
                if(count in rangenums and len(eight_points_data) < 8):
                    currentimg = tuple([keys[3], keys[4]])
                    eight_points_data[currentimg] = matchings[keys][imgID]


        self.RANSAC(eight_points_data, imgpoints)


    def imageMatches(self):
        image1Toimage2 = []
        



