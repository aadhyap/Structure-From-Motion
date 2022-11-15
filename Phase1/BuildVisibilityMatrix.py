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
        j = 0

       ''' vis_mat = []

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




    def findMatch(featureMatches, matches, 2Dcoords, iD):
        for key in featureMatches:
            if iD in featureMatches[key]:
                if featureMatches[key][iD] == 2Dcoords:'''

                    #This feature is present 
                    #Found a feature match woohoo, so this specific point is visible


    #https://scipy-cookbook.readthedocs.io/items/bundle_adjustment.html
    def bundle_adjustment_sparsity(n_cameras, n_points, camera_indices, point_indices):
        n_points = n_points.shape[0]
        m = camera_indices.size * 2
        n = n_cameras * 9 + n_points * 3
        A = lil_matrix((m, n), dtype=int)

        i = np.arange(camera_indices.size)
        for s in range(9):
            A[2 * i, camera_indices * 9 + s] = 1
            A[2 * i + 1, camera_indices * 9 + s] = 1

        for s in range(3):
            A[2 * i, n_cameras * 9 + point_indices * 3 + s] = 1
            A[2 * i + 1, n_cameras * 9 + point_indices * 3 + s] = 1

        return A









            









