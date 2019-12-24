####################################################
# Aim: rotationMatrixToEulerAngles
#
# Author:  by kuwingto on Dec 20, 2019
# Prerequisite: 
# pip install numpy
# pip install scipy
###############################################

import numpy as np
import math

# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R) :
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6
 
 
# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
def rotationMatrixToEulerAngles(R) :
 
    assert(isRotationMatrix(R))
     
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])

if __name__ == "__main__":
    ######### input variable ####################
    R = np.identity(3)
    R = np.array([ \
    9.3241647136940242e-01, -4.0489578408968181e-05, -3.6138555903581182e-01,\
    -3.9759644122188131e-03, 9.9993832052141274e-01, -1.0370480211116796e-02,\
    3.6136368885933323e-01, 1.1106462686671929e-02, 9.3235879942249944e-01])
    R = R.reshape(3,3)
    ######### function ####################
    x,y,z = rotationMatrixToEulerAngles(R)
    print("XYZ radian = ", x,y,z)
    print("XYZ deg = ", x * 180/3.1415, y * 180/3.1415, z * 180/3.1415)
