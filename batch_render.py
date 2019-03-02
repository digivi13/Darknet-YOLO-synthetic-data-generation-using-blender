import bpy, os
from math import sin, cos, pi
import numpy as np
import json
import sys

"""
Add scripts folder to Blender's Python interpreter and reload all scripts.
http://web.purplefrog.com/~thoth/blender/python-cookbook/import-python.html
"""
dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)

import boundingbox
import importlib
importlib.reload(boundingbox)

def render(scene, camera_object, mesh_objects, camera_steps, file_prefix="render"):
    """
    Renders the scene at different camera angles to a file, and returns a list of label data
    """

    """ This will store the bonding boxes """
    labels = []

    for i in range(0, camera_steps + 1):
        for j in range(0, camera_steps + 1):
            # Rendering
            # https://blender.stackexchange.com/questions/1101/blender-rendering-automation-build-script
            filename = '{}-{}y-{}p.png'.format(str(file_prefix), str(i), str(j))
            bpy.context.scene.render.filepath = os.path.join('/Users/thelabratory/documents/', filename)
            bpy.ops.render.render(write_still=True)

            scene = bpy.data.scenes['Scene']
            label_entry = {
                'image': filename,
                'meshes': {}
            }
            sep = '.png'
            textfilename = filename.split(sep, 1)[0]
            file = open('/Users/thelabratory/documents/' + textfilename + '.txt','w+')
            """ Get the bounding box coordinates for each mesh """
            for object in mesh_objects:
                bounding_box = boundingbox.camera_view_bounds_2d(scene, camera_object, object)
                if bounding_box:
                    label_entry['meshes'][object.name] = {
                        'x1': bounding_box[0][0],
                        'y1': bounding_box[0][1],
                        'x2': bounding_box[1][0],
                        'y2': bounding_box[1][1]
                    }
                y = object.name, bounding_box[0][0], bounding_box[0][1], bounding_box[1][0], bounding_box[1][1]
                width = bounding_box[1][0] - bounding_box[0][0] 
                height = bounding_box[1][1] - bounding_box[0][1]
                xC = bounding_box[0][0] + (width / 2)
                yC = 1 - (bounding_box[0][1] + (height / 2))
                objname = object.name.split('.')[0]
                z = objname, xC, yC, width, height
                for item in z:
                    file.write("%s" % item)
                    file.write(' ')
                file.write('\n')
                
                print(label_entry)
            labels.append(label_entry)
            file.close()
    return labels


def batch_render(scene, camera_object, mesh_objects):
    import scene_setup
    camera_steps = 0
    scene_setup_steps = 2
    labels = []

    for i in range(0, scene_setup_steps):
        frame_num = 46 + i
        scene_setup.simulate(scene, mesh_objects, frame_num)
        scene_labels = render(scene, camera_object, mesh_objects, camera_steps, file_prefix=i)
        labels += scene_labels # Merge lists

    with open('/Users/thelabratory/documents/labels.json', 'w+') as f:
        json.dump(labels, f, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    scene = bpy.data.scenes['Scene']
    camera_object = bpy.data.objects['Camera']
    mesh_names = ['Sphere.003', 'Cylinder']
    mesh_objects = [bpy.data.objects[name] for name in mesh_names]
    batch_render(scene, camera_object, mesh_objects)
