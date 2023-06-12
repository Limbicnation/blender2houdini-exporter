import hou
import platform

# Get the file node named "file1" inside the 'geo1' node
file_node = hou.node('/obj/geo1/file1')

# Define the file path based on the operating system
if platform.system() == 'Windows':
    file_path = 'I:/Temp_geo/model.fbx'
elif platform.system() == 'Linux':
    file_path = '/media/ws-ml/linux-drive/linux_projects/Temp_geo/model.fbx'
else:
    raise OSError("Unsupported operating system.")

# Set the file path parameter of the file node
file_node.parm('file').set(file_path)

# Press the Button to reload geometry
file_node.parm('reload').pressButton()