import numpy as np
import math
import time
from scipy.optimize import least_squares


#https://scipy-cookbook.readthedocs.io/items/bundle_adjustment.html
class BundleAdjustment:

    def __init__(self, camera_params, points_3d, n_cameras, n_points, camera_indices, point_indices, points_2d ):
        x0 = np.hstack((camera_params.ravel(), points_3d.ravel()))
        f0 = fun(x0, n_cameras, n_points, camera_indices, point_indices, points_2d)
        t0 = time.time()
        res = least_squares(fun, x0, jac_sparsity=A, verbose=2, x_scale='jac', ftol=1e-4, method='trf',
                            args=(n_cameras, n_points, camera_indices, point_indices, points_2d))
       
        x = res.x
        optimized_params = x1[:number_of_cam * 6].reshape((number_of_cam, 6))
        optimized_points_3d = x1[number_of_cam * 6:].reshape((n_points, 3))

        self.optimized_X = optimized_points_3d

        optimized_C_set, optimized_R_set = [], []
        for i in range(len(optimized_params)):
            R = getRotation(optimized_params[i, :3], 'e')
            C = optimized_params[i, 3:].reshape(3,1)
            self.optimized_C.append(C)
            self.optimized_R.append(R)

    def getPose(self):
        return self.optimized_C, self.optimized_R, self.optimized_X




