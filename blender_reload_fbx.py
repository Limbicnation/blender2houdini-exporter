bl_info = {
    "name": "Reload FBX",
    "author": "Gero Doll",
    "version": (1, 3),
    "blender": (4, 4, 0),
    "location": "View3D > UI > Houdini",
    "description": "Reload FBX file into the scene",
    "category": "Object"
}

import bpy
import os

import bpy

class ReloadFBXPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__.split('.')[0]  # Ensure bl_idname is correctly set

    fbx_path_linux: bpy.props.StringProperty(
        name="FBX Path (Linux)",
        subtype='FILE_PATH',
        default="/home/gero/Temp_geo/model.fbx",
        description="Path to the FBX file on Linux"
    ) # type: ignore

    fbx_path_windows: bpy.props.StringProperty(
        name="FBX Path (Windows)",
        subtype='FILE_PATH',
        default="I:\\Temp_geo\\model.fbx",
        description="Path to the FBX file on Windows"
    ) # type: ignore

    def draw(self, context):
        layout = self.layout
        layout.label(text="FBX File Path Settings")
        layout.prop(self, "fbx_path_linux")
        layout.prop(self, "fbx_path_windows")

class ReloadFBXOperator(bpy.types.Operator):
    bl_idname = "object.reload_fbx"
    bl_label = "Reload FBX"

    def execute(self, context):
        # Access the add-on preferences
        prefs = context.preferences.addons[__name__].preferences

        # Define the FBX file path based on the operating system
        if os.name == 'posix':  # Linux or macOS
            fbx_path = prefs.fbx_path_linux
        elif os.name == 'nt':  # Windows
            fbx_path = prefs.fbx_path_windows
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
    bpy.utils.register_class(ReloadFBXPreferences)
    bpy.utils.register_class(ReloadFBXOperator)
    bpy.utils.register_class(MyPanel)

def unregister():
    bpy.utils.unregister_class(ReloadFBXPreferences)
    bpy.utils.unregister_class(ReloadFBXOperator)
    bpy.utils.unregister_class(MyPanel)

if __name__ == "__main__":
    register()
