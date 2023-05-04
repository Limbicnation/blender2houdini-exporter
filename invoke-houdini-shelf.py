import hou

# Create a new Geometry object
obj_level = hou.node('/obj')
geo_node = obj_level.createNode('geo')
file_node = geo_node.createNode('file')

# Change the path to your FBX file here
path = 'I:/Temp_geo/model.fbx'

# Set the path parameter of the file node to the FBX file
file_node.parm('file').set(path)

