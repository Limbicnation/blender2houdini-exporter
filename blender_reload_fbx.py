bl_info = {
    "name": "Reload FBX",
    "author": "Gero Doll",
    "version": (1, 2),
    "blender": (4, 2, 0),
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
            self.report({'ERROR'}, "Unsupported operating system.")
            return {'CANCELLED'}

        # Check if the FBX file exists
        if not os.path.exists(fbx_path):
            self.report({'ERROR'}, f"FBX file not found: {fbx_path}")
            return {'CANCELLED'}

        try:
            # Switch to OBJECT mode
            bpy.ops.object.mode_set(mode='OBJECT')

            # Deselect all objects in the current view layer
            bpy.ops.object.select_all(action='DESELECT')

            # Import the FBX file
            bpy.ops.import_scene.fbx(filepath=fbx_path)

            # Post-import adjustment for colorspace
            valid_colorspaces = {item.identifier for item in bpy.types.ColorManagedInput.colorspace_items}
            fallback_colorspace = 'Linear Rec.709 (sRGB)' if 'Linear Rec.709 (sRGB)' in valid_colorspaces else 'Raw'

            for img in bpy.data.images:
                try:
                    if img.colorspace_settings.name not in valid_colorspaces:
                        img.colorspace_settings.name = fallback_colorspace
                        print(f"Setting colorspace for {img.name} to fallback: {fallback_colorspace}")
                except Exception as e:
                    print(f"Error setting colorspace for {img.name}: {e}")
                    self.report({'WARNING'}, f"Error setting colorspace for {img.name}. Defaulting to '{fallback_colorspace}'.")

            self.report({'INFO'}, "FBX file imported successfully.")
            return {'FINISHED'}

        except Exception as e:
            self.report({'ERROR'}, f"Failed to import FBX file: {e}")
            print(f"Error details: {e}")
            return {'CANCELLED'}

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
