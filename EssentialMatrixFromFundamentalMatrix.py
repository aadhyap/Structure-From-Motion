#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math

class EssentialMatrixFromFundamentalMatrix:
    def __init__(self):
        #getting the K matrix
        self.K = []
        with open('./P3Data/calibration.txt') as f:
            lines = f.readlines()
            lengthLines = len(lines)
            for i in range(lengthLines):
                data = lines[i]
                data = data.split()
                self.K.append(data)
            self.K = np.array(self.K).astype(float)
            print("K in an array ", self.K)

               


    #E = K^(T) * F * K
    #def getMatrix():


Test = EssentialMatrixFromFundamentalMatrix()












#how to add the singular values of E