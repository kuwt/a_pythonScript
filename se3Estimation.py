# Reference
# https://github.com/nghiaho12/rigid_transform_3D/blob/master/rigid_transform_3D.py
#

#!/usr/bin/python

import numpy as np
from math import sqrt

# Input: expects 3xN matrix of points
# Returns R,t
# R = 3x3 rotation matrix
# t = 3x1 column vector

def rigid_transform_3D(A, B):
    assert len(A) == len(B)

    num_rows, num_cols = A.shape;

    if num_rows != 3:
        raise Exception("matrix A is not 3xN, it is {}x{}".format(num_rows, num_cols))

    [num_rows, num_cols] = B.shape;
    if num_rows != 3:
        raise Exception("matrix B is not 3xN, it is {}x{}".format(num_rows, num_cols))

    # find mean column wise
    centroid_A = np.mean(A, axis=1)
    centroid_B = np.mean(B, axis=1)

    # subtract mean
    Am = A - np.tile(centroid_A, (1, num_cols))
    Bm = B - np.tile(centroid_B, (1, num_cols))

    # dot is matrix multiplication for array
    H = Am * np.transpose(Bm)

    # find rotation
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T * U.T

    # special reflection case
    if np.linalg.det(R) < 0:
        print("det(R) < R, reflection detected!, correcting for it ...\n");
        Vt[2,:] *= -1
        R = Vt.T * U.T

    t = -R*centroid_A + centroid_B

    return R, t

    
if __name__ == "__main__":
    ######### input variable ####################
    ax = np.array([[-0.0478,-0.023,-0.00035], [0.0521,-0.055,-0.00344],[0.052,-0.008,-0.0036]])
    A = np.asmatrix(ax)
    
    bx = np.array([[-0.0502,-0.0132,0.402], [0.046,-0.0306,0.381],[0.0475,0.00539,0.372]])
    B = np.asmatrix(bx)
   
    R,t = rigid_transform_3D(A,B)
    print("R = ", R)
    print("t = ", t)