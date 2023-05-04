import os
import subprocess

# Path to Blender executable
blender_path = "C:/Program Files/Blender Foundation/Blender 3.5/blender.exe"

hou.parm('/obj/geo1/rop_fbx1/execute').pressButton()

# Path to save the FBX file
fbx_path = "I:/Temp_geo/model.fbx"

# Use subprocess to run Blender and import the FBX file
subprocess.call([blender_path, "--background", "--python", "import bpy; bpy.ops.import_scene.fbx(filepath='"+fbx_path+"')"], shell=True)

# Show a message box confirming the export
message = f"Exported to Blender"
hou.ui.displayMessage(message)
print(message)