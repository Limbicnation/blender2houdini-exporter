import bpy
import os

class BlenderToHoudiniExportter(bpy.types.Panel):
    bl_idname = "Houdini_panel"
    bl_category = "Houdini"
    bl_label = "Houdini Menu"  # Fix the spelling error
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

def register():
    bpy.utils.register_class(BlenderToHoudiniExportter)

def unregister():
    bpy.utils.unregister_class(BlenderToHoudiniExportter)        

# Call register function

if __name__=="__main__":
    register()