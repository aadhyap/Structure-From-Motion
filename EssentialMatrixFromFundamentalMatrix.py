#Match Outlier Rejection via RANSAC
import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math
from scipy.stats import skew

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
        E = np.dot(self.K.T, np.dot(self.F, self.K))
        '''

        U,S,V = linalg.svd(E)
        if linalg.det(np.dot(U,V))<0:
            V = -V
        E = np.dot(U,np.dot(np.diag([1,1,0]),V))    
        
        # create matrices (Hartley p 258)
        Z = skew([0,0,-1])
        W = np.array([[0,-1,0],[1,0,0],[0,0,1]])
        
        # return all four solutions
       
        P2 = [np.vstack((np.dot(U,np.dot(W,V)).T,U[:,2])).T,
                 np.vstack((np.dot(U,np.dot(W,V)).T,-U[:,2])).T,
                np.vstack((np.dot(U,np.dot(W.T,V)).T,U[:,2])).T,
                np.vstack((np.dot(U,np.dot(W.T,V)).T,-U[:,2])).T]
        '''
        return E



















#how to add the singular values of E