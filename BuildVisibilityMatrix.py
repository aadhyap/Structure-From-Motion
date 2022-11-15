import numpy as np
from scipy import linalg
from scipy.sparse import lil_matrix
import math


class BuildVisibilityMatrix:


    '''
    input: a list of each camera pose and its image to world pts
    and its own matches and feature matches of previous img
    '''
    def __init__(self, featureMatches, matches, imgtoWorldpts):

        vis_mat = []

        j = 0
        for ncam in imgtoWorldpts:
            j = j + len(ncam) #total jumber for J

        i = len(imgtoWorldpts) #ith camera

        for i in imgtoWorldpts:
            img_to_X = imgtoWorldpts[i] #all world points for ith camera

            for j in img_to_X: #for each world point in that ith camera
                X = img_to_X[j]
                x = j #2D image

                #find the 2D image coords in the matches list







            









