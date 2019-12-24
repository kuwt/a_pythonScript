####################################################
# Aim: rotationMatrixToEulerAngles
#
# Author: https://www.learnopencv.com/rotation-matrix-to-euler-angles/
#       modify by kuwingto on Dec 20, 2019
# Prerequisite: 
# pip install numpy

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
    9.3894723537283509e-01, 5.3525686911359100e-03,-3.4401953315780837e-01,\
    2.0086072025752594e-03,9.9977666724996994e-01, 2.1037612023438450e-02,\
    3.4405530759285713e-01, -2.0444207760381201e-02,9.3872678649660080e-01])
    R = R.reshape(3,3)
    ######### function ####################
    x,y,z = rotationMatrixToEulerAngles(R)
    print("XYZ radian = ", x,y,z)
    print("XYZ deg = ", x * 180/3.1415, y * 180/3.1415, z * 180/3.1415)
