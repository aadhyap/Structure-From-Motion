import numpy as np
from scipy import linalg
import math
from scipy.stats import skew


class NonlinearTriangulation:

    def __init__(self, camerapose, allworldpts, imgpts):

        #Get P1, and P2

        

        C1 = np.zeros((3,1))
        R1 = np.identity(3)

        C2 = np.array(camerapose[0])
        C2 = np.reshape(C2, (3, 1))
        R2 = np.array(camerapose[1])
        I = np.array([[1,0,0],[0,1,0],[0,0,1]])
 

        P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
        P2 = np.dot(K, np.dot(R2, np.hstack((I, -C2))))


        #is it only the world points that made it in this projection
        for i in range(len(allworldpts)):








    def GeometricError(x1, x2, X, P1, P2):

        












