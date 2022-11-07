#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
import random
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
            if (len(S) > len(n)):
                bestres = F
                n = S.copy()

       

        #recalculate F = 
        newF = EstimateFundamentalMatrix(n)
        print("newF")
        self.bestF = newF.getMatrix()

    def GeometricError(self, X, P1, P2, x1, x2):

        P1_1, P1_2, P1_3 = P1

        x = x1[0]
        y = x1[1]

        X = np.append(X, 1)

        geo_err1 = np.square(np.divide( np.dot(P1_1.reshape(1,-1), X), np.dot(P1_3.reshape(1,-1), X) ) - x) + np.square(np.divide( np.dot(P1_2.reshape(1,-1), X), np.dot(P1_3.reshape(1,-1), X) ) - y) 


        P2_1, P2_2, P2_3 = P2

        x = x2[0]
        y = x2[1]

        geo_err2 = np.square(np.divide(np.dot(P2_1.reshape(1,-1), X), np.dot(P2_3.reshape(1,-1), X) ) - x) + np.square(np.divide( np.dot(P2_2.reshape(1,-1), X),np.dot(P2_3.reshape(1,-1), X) ) - y) 

        error = geo_err1 + geo_err2

        return error.squeeze()


    def get8points(self):
        

        matchings = self.matchings 
        imgID = self.imgID

        eight_points_data = {}
        imgpoints = {}
        size_matchings = 0
        count = 0
        randomNum = []

        for keys in matchings:
            if imgID in matchings[keys]:
                randomNum.append(size_matchings)
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]
            size_matchings += 1
        print("NUMBER OF SIZE MATCHINGS ", randomNum)

                

        rangenums =  random.sample(randomNum, 8)
        print("FIRST RANGE NUMS ", len(rangenums)) 
        for nums in rangenums:
            count = 0
            for keys in matchings:
                if imgID in matchings[keys]:
                    print("nums ", nums)
                    print("count ", count)
                    if(count == nums):
                        currentimg = tuple([keys[3], keys[4]])
                        eight_points_data[currentimg] = matchings[keys][imgID]
                    if(count > nums):
                        break
                count += 1
        print("ALL EIGHT POINTS ", eight_points_data)



        return eight_points_data, imgpoints


    def getF(self):
        return self.bestF


        
#how to recompute Fundamental?



