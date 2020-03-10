# Reference
#

#!/usr/bin/python

import sys
import os
import json

def transverseImageAnnoDirectory(root, img_ext = ".bmp", anno_ext = ".json"):
    image_paths = []
    annotations = []
    
    anno_file_names = []
    for root, dirs, files in os.walk(root):
        for f in files:
            filename, extension = os.path.splitext(f)
            if extension == anno_ext: # found annotation
                anno_file_names.append(filename)
    
    for name in anno_file_names:
        image_path = root + "/" + name + img_ext
        if os.path.isfile(image_path):# found image of an annotation
             ### ready image path  ###
            image_paths.append(image_path)
            ### ready annotation ###
            anno_file_path = root + "/" + name + anno_ext
            with open(anno_file_path, 'r') as f:
                anno_dict = json.load(f)
                shapes = anno_dict["shapes"]
                anno = []
                for i in range(7):
                    anno.append([-1,-1])
                for shape in shapes: 
                    point_index = int(shape["label"])
                    point_coord = shape["points"]
                    anno[point_index - 1] = point_coord[0]
                annotations.append(anno)
    return image_paths, annotations

    
if __name__ == "__main__":
    image_paths, annotations = transverseImageAnnoDirectory(".")
    print(image_paths[0])
    print(annotations[0])