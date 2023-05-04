bl_info = {
    "name": "Reload FBX",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > UI > Houdini",
    "description": "Reload FBX file into the scene",
    "category": "Object"
}

import bpy


class ReloadFBXOperator(bpy.types.Operator):
    bl_idname = "object.reload_fbx"
    bl_label = "Reload FBX"

    def execute(self, context):
        # Specify the path to the FBX file
        fbx_path = 'I:/Temp_geo/model.fbx'

        # Get the selected object
        selected_obj = bpy.context.selected_objects[0]

        # Remove the object and its mesh data
        bpy.ops.object.delete()

        # Import the FBX file and assign it to a new object
        bpy.ops.import_scene.fbx(filepath=fbx_path)
        new_obj = bpy.context.selected_objects[0]

        # Rename the new object to the original name
        new_obj.name = selected_obj.name

        # Select the new object
        new_obj.select_set(True)

        # Switch to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
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
