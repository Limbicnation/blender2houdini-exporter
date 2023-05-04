import hou

obj_level = hou.node('/obj')

# Create a new SOP node in Houdini
geo_node = hou.node("/obj").createNode("geo")

# Create a new file in Houdini
file_node = geo_node.createNode('file')

# Import the Blender geometry into the SOP node
path = 'I:/Temp_geo/model.fbx'
file_node.parm("file").set(path)

# Set the display flag on the new SOP node
geo_node.setCurrent(True, clear_all_selected=True)
