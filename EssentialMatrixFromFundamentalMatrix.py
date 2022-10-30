#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math

class EssentialMatrixFromFundamentalMatrix:
    def __init__(self, F):
        #getting the K matrix
        self.K = []
        self.F = F
        with open('./P3Data/calibration.txt') as f:
            lines = f.readlines()
            lengthLines = len(lines)
            for i in range(lengthLines):
                data = lines[i]
                data = data.split()
                self.K.append(data)
            self.K = np.array(self.K).astype(float)
            print("K in an array ", self.K)

        self.getEssential()

    
    #E = K^(T) * F * K
    #def getMatrix():

    def getEssential(self):
        transposeK = self.K.transpose()
        print("transpose K ", transposeK)

        print("Fundamental ", self.F)
        test = np.multiply(transposeK, self.F)
        print("test ", test)
        E = np.multiply(np.multiply(transposeK, self.F), self.K)

        print("E ", E)
        return E

















#how to add the singular values of E