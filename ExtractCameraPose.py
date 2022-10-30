import numpy as np
from scipy import linalg
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from random import sample
import math

class ExtractCameraPose:
    def __init__(self, E):
        U, S, V = np.linalg.svd(E)
        #if linalg.det(np.dot(U,V))<0:
            #V = -V
        W = np.array([[0,-1, 0],
                      [1, 0, 0],
                      [0, 0, 1]])
        
        c_up, c_down = U[:, 2], -U[:, 2]
        r_up, r_down = np.dot(U, np.dot(W,V)), np.dot(U, np.dot(W.T, V))

        cameraPoses = [[c_up, r_up], [c_down, r_up], [c_up, r_down], [c_down, r_down]]
        self.cameraPoses = cameraPoses

    def getCameraPoses(self):
        return self.cameraPoses
