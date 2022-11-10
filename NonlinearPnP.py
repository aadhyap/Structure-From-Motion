import numpy as np
from scipy.spatial.transform import Rotation 
import math


class NonlinearPnP:

    def __init__(self, pts, C, R, P, K):
        q= Rotation.from_matrix(R)
        Q = q.as_quat()
        Quart = [Q[0] ,Q[1],Q[2],Q[3]]
        C = [C[0], C[1], C[2]] 


        optimizeX = optimize.least_squares(
        fun = getLoss,
        x0=M,
        method="trf",
        args=[pts, K, Q, C])




    def getLoss(self, M, pts,  K, Q, C):
        C = C.reshape(-1,1)
       
        R = Rotation.from_quat(Q)
        R = R.as_matrix()



    def getProjection(self, C2, R2):
        C1 = np.zeros((3,1))
        R1 = np.identity(3)

        C2 = np.array(C2)
        C2 = np.reshape(C2, (3, 1))
        R2 = np.array(R2)
        I = np.array([[1,0,0],[0,1,0],[0,0,1]])
 

        P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
        P2 = np.dot(K, np.dot(R2, np.hstack((I, -C2))))

        