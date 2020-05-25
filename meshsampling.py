import numpy as np
import argparse
import trimesh

#############################################
# The purpose of this script is to convert 
# .stl mesh to .ply point cloud
# input: stl mesh path
# output: ply point cloud path
# 
# Dependency:
# pip3 install trimesh
# pip3 install numpy
###############################################

def write_ascii_ply(path,points):
    with open(path, mode='w') as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write("comment\n")
        f.write("element vertex {}\n".format(points.shape[0]))
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("element face 0\n")
        f.write("property list uchar int vertex_indices\n")
        f.write("end_header\n")
        for point in points:
            f.write("{} {} {}\n".format(point[0],point[1],point[2]))
    return
           
def meshsampling(path,num_of_points):
    # mesh objects can be loaded from a file name or from a buffer
    # you can pass any of the kwargs for the `Trimesh` constructor
    # to `trimesh.load`, including `process=False` if you would like
    # to preserve the original loaded data without merging vertices
    # STL files will be a soup of disconnected triangles without
    # merging vertices however and will not register as watertight
    mesh = trimesh.load(path)
    points, index = trimesh.sample.sample_surface_even(mesh,num_of_points )
    print("num of points = {}".format(points.shape[0]))
    return points


if __name__ == "__main__":
    ############# argument #######################
    parser = argparse.ArgumentParser(description='meshsampling')
    parser.add_argument('--src', type=str, default='./CircularPartsTemplate.STL')
    parser.add_argument('--tar', type=str, default='./a.ply')
    parser.add_argument('--num', type=int, default=20000)
    args = parser.parse_args()

    ############# argument #######################
    print("sampling {} to {}".format(args.src,args.tar))
    points = meshsampling(args.src,args.num)
    write_ascii_ply(args.tar,points)
    print("done.")