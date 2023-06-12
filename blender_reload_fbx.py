import bpy
import platform


class ReloadFBXOperator(bpy.types.Operator):
    bl_idname = "object.reload_fbx"
    bl_label = "Reload FBX"

    def execute(self, context):
        # Specify the path to the FBX file
        if platform.system() == "Windows":
            fbx_path = 'I:/Temp_geo/model.fbx'
        elif platform.system() == "Linux":
            fbx_path = '/media/ws-ml/linux-drive/linux_projects/Temp_geo/model.fbx'  # Update with the Linux path

        # Check if any objects are selected
        if not bpy.context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}

        # Get the first selected object
        selected_obj = bpy.context.selected_objects[0]

        # Delete the selected object and its mesh data
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = selected_obj
        selected_obj.select_set(True)
        bpy.ops.object.delete()

        # Import the FBX file and create a new object
        bpy.ops.import_scene.fbx(filepath=fbx_path)
        new_objs = bpy.context.selected_objects

        if not new_objs:
            self.report({'ERROR'}, "No objects found in the FBX file")
            return {'CANCELLED'}

        # Assign the original name to the first new object
        new_obj = new_objs[0]
        new_obj.name = selected_obj.name

        # Set the new object as the active object
        bpy.context.view_layer.objects.active = new_obj

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
