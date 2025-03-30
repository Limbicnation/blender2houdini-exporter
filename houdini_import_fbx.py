import hou
import platform
import os

def create_file_node_with_fbx():
    # Create or get the 'geo1' node
    obj_context = hou.node('/obj')
    geo1_node = hou.node('/obj/geo1')
    if not geo1_node:
        geo1_node = obj_context.createNode('geo', 'geo1')

    # Create a new file node inside 'geo1'
    try:
        file_node = geo1_node.createNode('file')
    except hou.OperationFailed as e:
        raise RuntimeError(f"Failed to create file node: {e}")

    # Define the path to the FBX file based on the operating system
    fbx_path = None
    if platform.system() == 'Windows':
        fbx_path = os.path.join('I:', 'Temp_geo', 'model.fbx')
    elif platform.system() == 'Linux':
        fbx_path = os.path.join('/home', 'gero', 'Temp_geo', 'model.fbx')
    else:
        raise OSError(f"Unsupported operating system: {platform.system()}")

    # Check if the FBX file exists
    if not os.path.exists(fbx_path):
        raise FileNotFoundError(f"The specified file does not exist: {fbx_path}")

    # Set the path parameter of the file node to the FBX file
    file_node.parm('file').set(fbx_path)

    # Reload the file on the file node
    try:
        file_node.parm('reload').pressButton()
    except hou.OperationFailed as e:
        print(f"Failed to reload the file: {e}")

    # Set the display flag to the newly created file node
    file_node.setDisplayFlag(True)

# Execute the function to create the file node with FBX
create_file_node_with_fbx()
