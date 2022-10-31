import numpy as np
from scipy import linalg
import math

class LinearTriangulation:
    def __init__(self, K, camerapose1, camerapose2, matchings, imgID):
        imgpoints = {}
        '''
        A = [[x (cross) P] [x2 cross P]]
        AX = 0
        '''

        #Testing each of the matchings and getting an X world points out of them 

        I = array([[1,0,0],[0,1,0],[0,0,1]])
        C1 = camerapose1[0]
        R1 = camerapose1[1]

        C2 = camerapose2[0]
        R2 = camerapose2[1]

        P1 = np.dot(K, np.dot(R1, np.hstack((I, -C1))))
        P2 = np.dot(K, np.dot(R2, np.hstack((I, -C2))))
    

        for keys in matchings:
            if imgID in matchings[keys]:
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]
                #img points for x and x'


        for keys in imgpoints:

            x_1 = keys
            x_2 = imgpoints[keys]

        

            A = np.array([[np.multiply(np.skew(x_1),P1)], [np.multiply(np.skew(imgpoints[x_2]),P2)]])







        
            
