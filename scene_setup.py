import bpy
import random

def simulate(scene, mesh_objects, frame_num):
    scene.frame_set(0)
    
    for i in range(1, 100):
        scene.frame_set(frame_num)

if __name__ == '__main__':
    scene = bpy.data.scenes['Scene']
    mesh_names = ['Sphere.001','Cylinder']
    mesh_objects = [bpy.data.objects[name] for name in mesh_names]
    frame_num = scene.frame_current + 1
    simulate(scene, mesh_objects, frame_num)
