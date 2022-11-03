import numpy as np
from scipy import linalg
import math
from scipy.stats import skew
import scipy.optimize as optimize


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


        optimized_X = []
        #is it only the world points that made it in this projection
        for i in range(len(allworldpts)):
            geometric_error = optimize.least_squares(fun=GeometricError, x0=allworldpts[i], method="trf", args=[P1, P2, x1[i], x2[i]])
            optimized_X.append(optimized_params.x)
            # x3D_.append(X1[:3])
        return np.array(optimized_X)










    def GeometricError(X, P1, P2, x1, x2):

        P1_1, P1_2, P1_3 = P1

        geo_err1 = np.square(np.divide( np.dot(P1_1, X), np.dot(P1_3, X) ) - x) + np.square(np.divide( np.dot(P1_2, X), np.dot(P1_3, X) ) - y) 


        P2_1, P2_2, P2_3 = P2

        geo_err2 = np.square(np.divide(np.dot(P2_1, X), np.dot(P2_3, X) ) - x) + np.square(np.divide( np.dot(P2_2, X),np.dot(P2_3, X) ) - y) 

        error = geo_err1 + geo_err2

        return error.squeeze()






        












