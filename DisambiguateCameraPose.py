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
            worldpts = worldpts[:, 0:3]

            numpts = self.numberOfPoints(C, R, worldpts)
            print("number of points ", numpts)

            if(numpts > self.maxpts):

                self.maxpts = numpts
                self.maxCamerapose = camerapose

            print(" MAX number of points ", self.maxpts)


            i = i + 1






    def numberOfPoints(self, C, R, worldpts):

        numberpts = 0

        for worldpt in worldpts:
            print("World Pt ", worldpt)
            if R.dot(worldpt-C)>0 and worldpt[2]>0:
                numberpts = numberpts + 1

        return numberpts

    def getbestCP(self):

        return self.maxCamerapose



