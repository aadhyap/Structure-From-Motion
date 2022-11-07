import numpy as np
from scipy import linalg
import math
from scipy.stats import skew
import pry



class DisambiguateCameraPose:

    def __init__(self, K, CameraPoses, allworldpts):


        self.maxpts = 0
        self.maxCamerapose = None

    

        self.bestpoints = {}



        i = 0

        for pose in CameraPoses:


            C1 = np.zeros((3,1))
            R1 = np.identity(3)

            C_ = np.array(pose[0])
            C = np.reshape(C_, (3, 1))
        
            #C = C.reshape(-1,1) 
            print("C ", C)
            R = np.array(pose[1])
            r = R[2, :].reshape(1,-1)
       
            I = np.array([[1,0,0],[0,1,0],[0,0,1]])
     

            P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
            P2 = np.dot(K, np.dot(R, np.hstack((I, -C))))


            worldpts =  allworldpts[i]
           
            #worldpts = worldpts[:, 0:3]

            allpts = self.numberOfPoints(C_, worldpts, r)


            if(len(allpts) > self.maxpts):

                self.maxpts = len(allpts)
                self.maxCamerapose = pose
                self.allpts = allpts




            i = i + 1



    def numberOfPoints(self, C, worldpts, r):
        allpts = {}

        for pt in worldpts:


            world_pt = worldpts[pt]

            world_pt = world_pt / world_pt[3].reshape(-1,1)
            world_pt = world_pt[0][0:3]

        

            value = np.dot(r, (world_pt-C))
            value = value[0]
       

  
            if value>0 and world_pt[2]>0:
                allpts[pt] = world_pt

        return allpts 

    def getbestCP(self):

        return self.maxCamerapose, self.allpts



