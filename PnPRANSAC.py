import numpy as np
from scipy import linalg
from random import sample
from LinearPnP import LinearPnP
import math


class PnPRANSAC:

    def __init__(self, new_matchings, imgtoX, K):

        

        allmatchings = {}

        size_matchings = 0
        for pts in imgtoX:
            x2 = pts[1][0:2]     
            if(x2 in new_matchings):
                size_matchings += 1
                new_img = new_matchings[x2]
                worldpt = imgtoX[pts]
                allmatchings[tuple(new_img)] = worldpt

        self.size_matchings = size_matchings #number of coresspondance in dictionary
        self.RANSAC(allmatchings)

        

    def RANSAC(self, allimgpts):

        n = {}
        bestres = 0
        for i in range(30):
            #choose 6 points
            imgpoints = self.choose6(new_matchings, imgtoX)
            PnP = LinearPnP(imgpoints, K)
            C, R, P= PnP.getPose()
            S = {} #inliers

            for keys in allimgpts:
                x = keys[0]
                y = keys[1]
                z = 1
                image = np.array([x, y, z])

                worldpt = allimgpts[keys]

                error = self.GeometricError(P, image, worldpt)

                if(error  < 0.05):
                    S[keys] = allimgpts[keys]

            if (len(S) > len(n)):
                n = S.copy()


        newPnP = LinearPnP(n, K)
        C, R, P= newPnP.getPose()
        print("<=======================Final Camera Pose===========================>")
        print(C, R)


    def GeometricError(self, P, x, X):

            print("CURRENT X ", X)

            P1, P2, P3 = P

            u = x[0]
            v = x[1]

            X = np.append(X, 1)


            error = np.square((u - np.divide(np.dot(P1.T, X), np.dot(P3.T, X)))) + np.square((v - np.divide(np.dot(P2.T, X), np.dot(P3.T, X)))) 

            return error.squeeze()


    def choose6(self, new_matchings, imgtoX):


        newimgpts = {}

        

        size_matchings = 0
        count = 0
        randomNum = []

        rangenums =  sample(range(0, self.size_matchings), 6) 
        print("length of list ", len(rangenums))


        for num in rangenums:
            count = 0
            for pts in imgtoX:
                x2 = pts[1][0:2]
                if(x2 in new_matchings) and (count == num) :
                    #image2 match with new image pts
                    new_img = new_matchings[x2]
                    worldpt = imgtoX[pts]
                    newimgpts[tuple(new_img)] = worldpt
                if count > num:
                    break
                
                count +=  1

        print("length of new img points ", newimgpts)

        #returns newimgpts with correct new image points correspondace with world points
        return newimgpts





