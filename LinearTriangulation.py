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
    

        for keys in matchings:
            if imgID in matchings[keys]:
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]
                #img points for x and x'


        for keys in imgpoints:
            x = keys[0]
            y = keys[1]

            x_2, y_2 = imgpoints[keys][0], imgpoints[keys][1]





        
            
