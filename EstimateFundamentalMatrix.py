#Estimating fundamental matrix
import numpy as np
from scipy import linalg


class EstimateFundamentalMatrix:
    def __init__(self, points):

        print("len of of eight points ", len(points))
        # build matrix for equations

       
        A = np.zeros((len(points),9))
        i = 0
        for keys in points:
            #print("key ",keys)
            #print("points ", points[keys])
            refpoints = points[keys]

            #print("key x ",keys[0])
            #print("points x ", refpoints[0])

            #print("key x ",keys[1])
            #print("points x ", refpoints[1])
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

        #why is the last F in the corner 1 
        print("_____F_____")
        print(F)

   
        self.matrix = F


    def getMatrix(self):

        
        return self.matrix

    
            


#if __name__ == '__main__':
     #FundamentalMatrix = EstimateFundamentalMatrix()