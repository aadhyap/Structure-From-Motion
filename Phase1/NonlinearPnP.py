import numpy as np
from scipy.spatial.transform import Rotation 
import math
import scipy.optimize as optimize


class NonlinearPnP:

    def __init__(self, pts, C, R, P, K):
        q= Rotation.from_matrix(R)
        Q = q.as_quat()
        Quart = [Q[0] ,Q[1],Q[2],Q[3]]
        C = [C[0], C[1], C[2]] 
        params = C + Quart


        optimize_QC = optimize.least_squares(
        fun = self.getLoss,
        x0=params,
        method="trf",
        args=[pts, K])

        params = optimize_QC.x
        C = params[:3]
        Q = params[3:]
        R = Rotation.from_quat(Q)
        self.R = R.as_matrix()
        self.C = C


    def getPose(self):
        return self.C,self.R
        

    def getLoss(self, params, pts,  K):
        C = params[:3]
        Q = params[3:]
        C = C.reshape(-1,1)
        R = Rotation.from_quat(Q)
        R = R.as_matrix()


        P = self.getProjection(C, R, K)


        allerrors = []
        for imagepts in pts:
            x = imagepts[0]
            y = imagepts[1]

            X = pts[imagepts]
            P1_1, P1_2, P1_3 = P

            x = imagepts[0]
            y = imagepts[1]

            #X = np.append(X, 1)

            alg_err = np.square(np.divide( np.dot(P1_1.reshape(1,-1), X), np.dot(P1_3.reshape(1,-1), X) ) - x) + np.square(np.divide( np.dot(P1_2.reshape(1,-1), X), np.dot(P1_3.reshape(1,-1), X) ) - y) 
            error = alg_err
            allerrors.append(error)



        allerrors = np.array(allerrors).squeeze()
        mean_error = np.mean(allerrors)

        return mean_error



    def getProjection(self, C2, R2, K):
        C2 = np.array(C2)
        C2 = np.reshape(C2, (3, 1))
        R2 = np.array(R2)
        I = np.array([[1,0,0],[0,1,0],[0,0,1]])
 
        P = np.dot(K, np.dot(R2, np.hstack((I, -C2))))

        return P




        