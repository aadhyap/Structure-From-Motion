import numpy as np
from scipy import linalg
import math
from scipy.stats import skew



class DisambiguateCameraPose:

    def __init__(self, CameraPoses, allworldpts):


        self.maxpts = 0
        self.maxCamerapose = None

        j = 0 
        for i in allworldpts:
            camerapose = CameraPoses[j]
            j = j + 1


            C = np.array(camerapose[0])
            R = np.array(camerapose[1])
            R = R[2, :].reshape(1,-1)

            worldpts =  np.asarray(allworldpts[i])
            worldpts = worldpts[:, 0:3]


            numpts = self.numberOfPoints(C, R, worldpts)
            print("number of points ", numpts)

            if(numpts > self.maxpts):

                self.maxpts = numpts
                self.maxCamerapose = camerapose

        print(" MAX number of points ", self.maxpts)

    

    def numberOfPoints(self, C, R, worldpts):

        numberpts = 0

        for worldpt in worldpts:
            print("World Pt ", worldpt)
            if R.dot(worldpt-C)>0 and worldpt[2]>0:
                numberpts = numberpts + 1

        return numberpts

    def getbestCP(self):

        return self.maxCamerapose



