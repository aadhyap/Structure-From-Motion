import numpy as np
from scipy import linalg
from random import sample
from LinearPnP import LinearPnP
import math


class PnPRANSAC:

    def __init__(self, new_matchings, imgtoX, K):

        

        size_matchings = 0
        for pts in imgtoX:
            x2 = pts[1][0:2]     
            if(x2 in new_matchings):
                size_matchings += 1

        self.size_matchings = size_matchings #number of coresspondance in dictionary

        imgpoints = self.choose6(new_matchings, imgtoX)
        PnP = LinearPnP(imgpoints, K)
        C, R = PnP.getPose()

        print("<=======================Final Camera Pose===========================>")
        print(C, R)




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





