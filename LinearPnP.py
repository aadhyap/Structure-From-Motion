import numpy as np
from scipy import linalg
import math


class LinearPnP:

'''
Getting pose from 2D-3D correspondences
Inputs:
 X - size (N x 3) matrix of 3D points
 x - size (N x 2) matrix of 2D points whose rows correspond with X
 K - size (3 x 3) camera calibration (intrinsics) matrix
Outputs:
 C - size (3 x 1) pose transation
 R - size (3 x 3) pose rotation
'''


'''
Parameters
new_matchings --> The matchings for the new image (for example image 2 points to image 3 points)
worldpointstoImage --> Image 1 and Image 2 --> Image 3




'''
    def __init__(self, new_matchings, worldpointstoImage, K):

       newimgpts = self.getNewImg_pts()

       for pt in newimgpts:
            u, v = pt
            imgCross = np.array([[0, -1, v],
                            [1,  0 , -u],
                            [-v, u, 0]])


            zero4 = np.zeros((1, 4))
            X = newimgpts[pt].reshape((1, 4))
            Tilde_X = np.vstack((np.hstack((X, zero4, zero4)), 
                            np.hstack((zero4,X, zero4)), 
                            np.hstack((zero4, zero4,X))))

            A = np.dot(imgCross, Tilde_X)

            U, S, V = np.linalg.svd(A)
            V = V[-1]
            P = V.reshape((3, 4)) #P has 4 but we want the first 3 for rotation and the last one is for translation
            p = P[:, :3] #Rotational

            #Get Rotational Matrix
            K_inv = np.linalg.inv(K) #inverse of K
            r = np.dot(K_inv, p)
            U, S, V = np.linalg.svd(r)
            R = (np.dot(U, V)).T

            t = P[:, 3]

            print("All of P ", P)
            print("Ps three columns ", p)
            print("Ps 4th column ", t)


            #Get Translational
            T = np.divide(np.dot(K_inv, t), S)
            temp = -np.linalg.inv(R)
            C = np.dot(temp, T)
            if np.linalg.det(R) < 0:
                R = -R
                C = -C

            self.R = R
            self.C = C

    


    def getNewImg_pts(self,new_matchings, worldpointstoImage):


        newimgpts = {}
        for pts in worldpointstoImage:
            x2 = pts[1]
            if(x2 in new_matchings):
                #image2 match with new image pts
                new_img = new_matchings[x2]
                worldpt = worldpointstoImage[pts]
                newimgpts[new_img] = worldpt

        #returns newimgpts with correct new image points correspondace with world points
        return newimgpts


    def getPose(self):
        return C, R




        
