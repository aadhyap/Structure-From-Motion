import numpy as np
from scipy import linalg
import math
from scipy.stats import skew

class LinearTriangulation:
    def __init__(self, K, camerapose2, matchings, imgID):


        imgpoints = {}
        world_points = {}
        '''
        A = [[x (cross) P] [x2 cross P]]
        AX = 0
        '''

        #Testing each of the matchings and getting an X world points out of them 

        C1 = np.zeros((3,1))
        R1 = np.identity(3)

        C2 = np.array(camerapose2[0])
        C2 = np.reshape(C2, (3, 1))
        R2 = np.array(camerapose2[1])
        I = np.array([[1,0,0],[0,1,0],[0,0,1]])
 

        P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
        P2 = np.dot(K, np.dot(R2, np.hstack((I, -C2))))
     




        for keys in matchings:
            if imgID in matchings[keys]:
                currentimg = tuple([keys[3], keys[4], 1])
                imgpoints[currentimg] = [matchings[keys][imgID][0], matchings[keys][imgID][1], 1]
                #img points for x and x'

        for keys in imgpoints:
            x_1 = np.array(keys)
            x_2 = np.array(imgpoints[keys])

            print("x_1 ", x_1)
            print("x_2 ", x_2)
            print("P_1 ", P1)
            print("P_2 ", P2)

            #Ax = 0
            #A = np.array([np.dot(skew(x_1),P1), np.dot(skew(x_2),P2)])


            A = np.zeros((6,6))
            A[:3,:4] = P1
            A[3:,:4] = P2
            A[:3,4] = -x_1
            A[3:,5] = -x_2
            print("A ")
            print(A)
           
            U, S, V = np.linalg.svd(A)
            X = V[-1,:4]
            world_point = X / X[3]
            world_point = world_point.T
            world_points[tuple(x_1, x_2)] = world_point #Add image points for image 1 and image 2 and world point into dictionary 
            print("World Point ", world_point)

        self.world_points = world_points



    def getWorldPoints(self):
        return self.world_points









        
            
