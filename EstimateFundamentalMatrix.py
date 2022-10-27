#Estimating fundamental matrix
import numpy as np
from scipy import linalg


class EstimateFundamentalMatrix:
    def __init__(self, points):
        # build matrix for equations
        A = np.zeros((8,9))
        i = 0
        for keys in points:
            print("key ",keys)
            print("points ", points[keys])
            refpoints = points[keys]

            print("key x ",keys[0])
            print("points x ", refpoints[0])

            print("key x ",keys[1])
            print("points x ", refpoints[1])
            A[i] = [keys[0]*refpoints[0], keys[0]*refpoints[1], keys[0], keys[1]*refpoints[0], keys[1]*refpoints[1], keys[1], refpoints[0], refpoints[1], 1 ]
            i = i + 1


                
        # compute linear least square solution
        U,S,V = linalg.svd(A)
        F = V[-1].reshape(3,3)
            
        # constrain F
        # make rank 2 by zeroing out last singular value
        U,S,V = linalg.svd(F)
        S[2] = 0
        F = np.dot(U,np.dot(np.diag(S),V))
        F = F/F[2,2]
        print("_____F_____")
        print(F)

        
        return F/F[2,2]

            


#if __name__ == '__main__':
     #FundamentalMatrix = EstimateFundamentalMatrix()