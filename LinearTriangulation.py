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

        for keys in matchings:
            if imgID in matchings[keys]:
                currentimg = tuple([keys[3], keys[4]])
                imgpoints[currentimg] = matchings[keys][imgID]

        
            
