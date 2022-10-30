#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math


class GetInlierRANSAC:
    def __init__(self, matchings, imgID):
        self.matchings = matchings
        self.imgID = imgID
        eight_points_data, imgpoints = self.get8points()
        self.RANSAC(eight_points_data)

    def RANSAC(self, eightpointdata):
        print("eightpoints generated ", eightpointdata)
        n = {}
        bestres = 0
        for i in range(30):
            #choose 8 coorespondance 

            eightpointdata, imgpoints = self.get8points()
            Fund = EstimateFundamentalMatrix(eightpointdata)
            F = Fund.getMatrix()
            S = {} #inliers

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

              
                res1 = np.dot(image2, F)
                res = np.dot(res1, image1)


                

                if(res < 0.05):
                    S[keys] = imgpoints[keys]
                    print("res that made it ", res)
            print("length of S ", len(S))
            if (len(S) > len(n)):
                bestres = F
                n = S.copy()

        print("Lenght ", len(n))
        print("RES Final ", bestres)


        print("FINISHED")

        print("THE FINISHED ")
        print(n)

        #recalculate F = 
        newF = EstimateFundamentalMatrix(n)
        print("newF")
        self.bestF = newF.getMatrix()


    def get8points(self):
        

        matchings = self.matchings 
        imgID = self.imgID

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


        return eight_points_data, imgpoints


    def getF(self):
        return self.bestF


        
#how to recompute Fundamental?



