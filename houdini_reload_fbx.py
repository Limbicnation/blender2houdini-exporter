import hou

# Get the shelf named "MyShelf"
my_shelf = hou.shelves.shelves()["houdini-importer"]

# Press the Button to reload geometry
hou.parm('/obj/geo1/file1/reload').pressButton()
