import hou
import platform

def create_and_reload_file_node():
    # Get the 'geo1' node
    geo1_node = hou.node('/obj/geo1')

    # Create a new file node inside 'geo1'
    file_node = geo1_node.createNode('file')

    # Define the path to your FBX file based on the operating system
    if platform.system() == 'Windows':
        path = 'I:/Temp_geo/model.fbx'
    elif platform.system() == 'Linux':
        path = '/home/ws-ml/Temp_geo/model.fbx'
    else:
        raise OSError("Unsupported operating system.")

    # Set the path parameter of the file node to the FBX file
    file_node.parm('file').set(path)

    # Reload the file on the file node
    file_node.parm('reload').pressButton()

    # Set the display flag to the newly created file node
    file_node.setDisplayFlag(True)

if __name__ == "__main__":
    create_and_reload_file_node()
