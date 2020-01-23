####################################################
# Aim: facenormaldot
#
# Author:  by kuwingto on Jan 23, 2010
# Prerequisite: 
# pip install numpy
# pip install scipy
###############################################

import numpy as np
import math


def facenormaldot(face0p0, face0p1, face0p2, face1p0, face1p1, face1p2) :
    
    v1 = face0p1 - face0p0
    v2 = face0p2 - face0p0
    n1 = np.cross(v1, v2)
    n1 = n1 / np.linalg.norm(n1)
    
    v3 = face1p1 - face1p0
    v4 = face1p2 - face1p0
    n2 = np.cross(v3, v4)
    n2 = n2 / np.linalg.norm(n2)
    
    dot = np.dot(n1,n2)
    return n1, n2, dot

if __name__ == "__main__":
    ######### input variable ####################
    face0p0 = np.array([-0.655967,-0.836715,-0.715628])
    face0p1 = np.array([-0.975908,-0.915637,-0.466769])
    face0p2 = np.array([-0.914375,-0.836715,-0.437339])
    face1p0 = np.array([-0.655967,-0.836715,-0.715628])
    face1p1 = np.array([-0.914375,-0.836715,-0.437339])
    face1p2 = np.array([-0.600787,-0.81512,-0.65543])
  
    ######### function ####################
    normal0, normal1, dot = facenormaldot(face0p0, face0p1, face0p2, face1p0, face1p1, face1p2)
    print("dot = ", dot)
    print("normal0 = ", normal0)
    print("normal1 = ", normal1)
