import bpy
from mathutils import *
from math import *

# Getting width, height and the camera
scn = bpy.data.scenes['Scene']
w = scn.render.resolution_x*scn.render.resolution_percentage/100.
h = scn.render.resolution_y*scn.render.resolution_percentage/100.
cam = bpy.data.cameras['Camera']
camobj = bpy.data.objects['Camera']

# Some point in 3D you want to project
v = Vector((1,2,3))

# Getting camera parameters
# Extrinsic
RT = camobj.matrix_world.inverted()
# Intrinsic
C = Matrix().to_3x3()
C[0][0] = -w/2 / tan(cam.angle/2)
ratio = w/h
C[1][1] = -h/2. / tan(cam.angle/2) * ratio
C[0][2] = w / 2.
C[1][2] = h / 2.
C[2][2] = 1.
C.transpose()

# Projecting v with the camera
p = (v * RT) * C
p /= p[2]