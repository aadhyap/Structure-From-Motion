import numpy as np
from scipy import linalg
import math
from scipy.stats import skew

class LinearTriangulation:
    def __init__(self, K, camerapose1, camerapose2, matchings, imgID):
        imgpoints = {}
        world_points = []
        '''
        A = [[x (cross) P] [x2 cross P]]
        AX = 0
        '''

        #Testing each of the matchings and getting an X world points out of them 

        C1 = np.array(camerapose1[0])
        C1 = np.reshape(C1, (3, 1))
        R1 = np.array(camerapose1[1])

        C2 = np.array(camerapose2[0])
        C2 = np.reshape(C2, (3, 1))
        R2 = np.array(camerapose2[1])
        I = np.array([[1,0,0],[0,1,0],[0,0,1]])
        print("length camerapose1 ", len(I))
       
        print("length camerapose1 ", np.dot(R1, np.hstack((I, -C1))))
        print("length camerapose1 ", np.dot(K, np.dot(R1, np.hstack((I, -C1)))))
        print("length camerapose1 ", C1.shape)

        

        P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
        P2 = np.dot(K, np.dot(R2, np.hstack((I, -C2))))
        print("length camerapose1 ", P1.shape)
        print("length camerapose1 ", P2.shape)




        for keys in matchings:
            if imgID in matchings[keys]:
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]
                #img points for x and x'

        for keys in imgpoints:
            x_1 = keys
            x_2 = imgpoints[keys]

            #Ax = 0
            A = np.array([np.dot(skew(x_1),P1), np.dot(skew(x_2),P2)])
            U, S, V = np.linalg.svd(A)
            X = V.T
            world_point = X[:,-1]
            world_points.append(world_point)
            print("World Point ", world_point)

        self.world_points = world_points



    def getWorldPoints(self):
        return self.world_points









        
            
