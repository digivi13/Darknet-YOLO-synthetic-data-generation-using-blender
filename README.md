# Darknet-YOLO-synthetic-data-generation-using-blender
Scripts for generating Darknet YOLO training data using blender animations
Text instructions for github repo titled:  YOLO darknet synthetic data generator using blender: 

Pre-requisite: Knowledge of Blender design/animation software 

To generate YOLO Darnknet CNN training images and annotations, create a model with all materials and animations applied. The scripts render the animations you have created from the frame specified, along with annotations containing the bounding boxes of each of your specified objects

Description of output files: 

Labels.json: Is a summary of the bounding box information for each of the objects in your scene using the bottom left corner as origin.
The bounding boxes are described as xmin, yimin, xmax, ymax

1-0y-0p.png: The rendered image of your animation. The first integer value is the image output number (starts at 0)

1-0y-0p.txt: The annotation file for the corresponding image. Contains all the needed information for training the YOLO darknet network [class, xcenter, ycenter, width, height]

Step 1: 

Customize the scripts to suit your needs using the following instructions: 

batch_render.py

line 32: “bpy.context.scene.render.filepath = os.path.join('/Users/thelabratory/documents/', filename)
Set the file path you would like the images to be saved to

Line 42: file = open('/Users/thelabratory/documents/' + textfilename + '.txt','w+')
Set the file path you would like the images to be saved to (redundancy)

line 74: “scene_setup_steps = 2”
Set the integer value to the number of frames you want to render and generate annotations for

line 78: “frame_num = 46 + i” 
Set the integer value to set the frame at which you want to start at in the animation

Line 98: “mesh_names = ['0, '0.01',’1’]”
Change the names of the 3d models to the integer value of the objects class:
Note: your 3d model must be a single object and have a name with an integer value that matches your objects class (starting at 0).  If you have multiple objects of the same class in your scene, name each of these objects  0.1, 0.2, 0.3. The script will process all the 3d models but only use that first integer value for the objects class.

Ex) if you have a 3d model of a plane, and plane is the first class in your object.names file used for training darknet. You would want your blender model to have the name ‘0’. If we had multiple planes, we would name each of them ‘0.xxxxx’

boundingbox.py 

Line 79: “mesh_object = bpy.data.objects['0, '0.01',’1’]”
This should match line 98 in batch_render.py

scene_setup.py

Line 12: “mesh_names = ['0, '0.01',’1’]”
This should match line 98 in batch_render.py

Step 2: 

-Open your animation

-Set your animation image file format, resolution, etc in blender

-Drag out a new view 

-Open the text editor 

-Load each of the scripts (scene_setup.py, boundingbox.py, batch_render.py) into the  text editor in blender

-Make sure that batch_render.py is the current selected script

-Press run script

Step 3: 

Evaluate the bounding boxes: 

Use the ViewAnnotations.py file

Lines 4, 6, 9: Change to the directory containing your images and annotations

Line 5: Change to image extension type 

Images with bounding boxes will be saved to the directory the script is run from 

