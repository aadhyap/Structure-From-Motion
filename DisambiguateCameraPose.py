import numpy as np
from scipy import linalg
import math
from scipy.stats import skew



class DisambiguateCameraPose:

    def __init__(self, CameraPoses, allworldpts):


        self.maxpts = 0
        self.maxCamerapose = None

    

        self.bestpoints = {}



        i = 0

        for pose in CameraPoses:


            C1 = np.zeros((3,1))
            R1 = np.identity(3)

            C = np.array(pose[0])
            C = np.reshape(C2, (3, 1))
            R = np.array(pose[1])
            R = R[2, :].reshape(1,-1)
            I = np.array([[1,0,0],[0,1,0],[0,0,1]])
     

            P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
            P2 = np.dot(K, np.dot(R, np.hstack((I, -C))))


            worldpts =  np.asarray(allworldpts[i])
            #worldpts = worldpts[:, 0:3]

            allpts = self.numberOfPoints(C, R, worldpts)
            print("number of points ", numpts)

            if(len(allpts) > self.maxpts):

                self.maxpts = len(numpts)
                self.maxCamerapose = pose
                self.allpts = allpts

            print(" MAX number of points ", self.maxpts)


            i = i + 1



    def numberOfPoints(self, C, R, worldpts):
        allpts = {}

        for pt in worldpts:

            world_pt = worldpts[pt]
            world_pt = worldpt[0:3]

            print("World Pt ", world_pt)
            if R.dot(world_pt-C)>0 and world_pt[2]>0:
                allpts[pt] = world_pt

        return allpts 

    def getbestCP(self):

        return self.maxCamerapose, self.allpts



