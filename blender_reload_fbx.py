bl_info = {
    "name": "Reload FBX",
    "author": "Your Name",
    "version": (1, 1),
    "blender": (3, 6, 1),
    "location": "View3D > UI > Houdini",
    "description": "Reload FBX file into the scene",
    "category": "Object"
}

import bpy
import os

class ReloadFBXOperator(bpy.types.Operator):
    bl_idname = "object.reload_fbx"
    bl_label = "Reload FBX"

    def execute(self, context):
        # Define the FBX file path based on the operating system
        if os.name == 'posix':  # Linux or macOS
            fbx_path = '/home/ws-ml/Temp_geo/model.fbx'
        elif os.name == 'nt':  # Windows
            fbx_path = r'I:\Temp_geo\model.fbx'
        else:
            raise OSError("Unsupported operating system.")

        # Check if there is a selected object
        if context.active_object:
            # Store the active object's name
            selected_obj_name = context.active_object.name

            # Switch to OBJECT mode
            bpy.ops.object.mode_set(mode='OBJECT')

            # Deselect all objects in the current view layer
            bpy.ops.object.select_all(action='DESELECT')  # Removed `extend=False`

            # Import the FBX file
            bpy.ops.import_scene.fbx(filepath=fbx_path)

            # Get the newly imported object
            new_obj = context.view_layer.objects.active

            if new_obj:
                # Rename the new object to the original name
                new_obj.name = selected_obj_name

        return {'FINISHED'}

class MyPanel(bpy.types.Panel):
    bl_label = "Reload FBX"
    bl_idname = "OBJECT_PT_reload_fbx"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Houdini"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Click to reload FBX")
        row.operator("object.reload_fbx")

def register():
    bpy.utils.register_class(ReloadFBXOperator)
    bpy.utils.register_class(MyPanel)

def unregister():
    bpy.utils.unregister_class(ReloadFBXOperator)
    bpy.utils.unregister_class(MyPanel)

if __name__ == "__main__":
    register()
