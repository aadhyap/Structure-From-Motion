import numpy as np
from scipy import linalg
import math
from scipy.stats import skew



class DisambiguateCameraPose:

    def __init__(self, allworldpts):


        self.maxpts = 0
        self.maxCamerapose = None
        for camerapose in allworldpts:

            C = camerapose[0].reshape(-1,1) 
            R = camerapose[1].reshape(-1,1) 
            R = R[2, :].reshape(1,-1)

            worldpts = allworldpts[camerapose]
            worldpts = worldpts[:, 0:3]

            numpts = self.numberOfPoints(C, R, worldpts)

            if(numpts > self.maxpts):
                self.maxpts = numpts
                self.maxCamerapose = camerapose

        return self.maxCamerapose




    def numberOfPoints(self, C, R, worldpts):

        numberpts = 0

        for worldpt in worldpts:
            if R.dot(worldpt-C)>0 and worldpt[2]>0:
                numberpts = numberpts + 1:

        return numberpts



