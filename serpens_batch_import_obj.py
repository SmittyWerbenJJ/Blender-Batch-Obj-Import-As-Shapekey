
import os
from pathlib import Path

# the files that the user selects using the blender import interface
#selected_files
obj_files=selected_files
print(obj_files)

#serpens variable - the active object from the scene
#original_model

#get all obj files from the folder


print(f"importing {len(obj_files)}obj files ...")
for obj in obj_files:
    bpy.ops.wm.obj_import(filepath=obj)

#select each imported object, then select the original object,then execute "join as shapes" operator
bpy.ops.object.select_all(action='DESELECT')
for obj in [Path(file).stem for file in obj_files] :
    bpy.data.objects[obj].select_set(True)
original_model.select_set(True)
bpy.context.view_layer.objects.active = original_model
bpy.ops.object.join_shapes()

#delete imported objects
original_model.select_set(False)
bpy.ops.object.delete()
