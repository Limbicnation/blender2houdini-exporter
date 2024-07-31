import os
import bpy
import subprocess
import platform
from pathlib import Path

bl_info = {
    "name": "Blender to Houdini Exporter",
    "author": "Gero Doll",
    "version": (1, 2),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Houdini Menu",
    "description": "Export selected objects to FBX and launch Houdini",
    "category": "Import-Export",
}

class HoudiniExporterPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    houdini_path_windows: bpy.props.StringProperty(
        name="Houdini Path (Windows)",
        subtype='FILE_PATH',
        default=r"C:\Program Files\Side Effects Software\Houdini\bin\houdinifx.exe"
    ) # type: ignore

    houdini_path_linux: bpy.props.StringProperty(
        name="Houdini Path (Linux)",
        subtype='FILE_PATH',
        default="/opt/hfs/bin/houdinifx"
    ) # type: ignore

    geo_path: bpy.props.StringProperty(
        name="FBX Export Path",
        subtype='FILE_PATH',
        default=""
    ) # type: ignore

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "houdini_path_windows")
        layout.prop(self, "houdini_path_linux")
        layout.prop(self, "geo_path")

class SaveFBXOperator(bpy.types.Operator):
    bl_idname = "object.save_fbx"
    bl_label = "Save FBX"
    bl_description = "Export selected objects to FBX"

    def execute(self, context):
        preferences = bpy.context.preferences.addons[__name__].preferences
        geo_path = Path(preferences.geo_path)

        if not geo_path.suffix == '.fbx':
            self.report({'ERROR'}, "Export path must end with '.fbx'.")
            return {'CANCELLED'}

        try:
            geo_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to create export directory: {e}")
            return {'CANCELLED'}

        bpy.ops.export_scene.fbx(filepath=str(geo_path), use_selection=True, global_scale=1)
        self.report({'INFO'}, f"Exported FBX to {geo_path}")

        return {'FINISHED'}

class SendToHoudiniOperator(bpy.types.Operator):
    bl_idname = "object.send_houdini"
    bl_label = "Send To Houdini"

    def execute(self, context):
        preferences = bpy.context.preferences.addons[__name__].preferences
        geo_path = preferences.geo_path
        houdini_path = preferences.houdini_path_windows if platform.system() == 'Windows' else preferences.houdini_path_linux

        if not geo_path.endswith('.fbx'):
            self.report({'ERROR'}, "Export path must end with '.fbx'.")
            return {'CANCELLED'}

        os.makedirs(os.path.dirname(geo_path), exist_ok=True)
        bpy.ops.export_scene.fbx(filepath=geo_path, use_selection=True, global_scale=1)
        self.report({'INFO'}, f"Exported FBX to {geo_path}")

        if not os.path.isfile(houdini_path):
            self.report({'ERROR'}, "Houdini path is not valid.")
            return {'CANCELLED'}

        if not self.check_houdini_running():
            try:
                subprocess.Popen([houdini_path, '-j', geo_path])
                self.report({'INFO'}, "Launched Houdini with the exported FBX.")
            except Exception as e:
                self.report({'ERROR'}, f"Error launching Houdini: {e}")
                return {'CANCELLED'}
        else:
            self.report({'INFO'}, "Houdini is already running.")

        return {'FINISHED'}

    def check_houdini_running(self):
        try:
            if platform.system() == 'Windows':
                output = subprocess.check_output("tasklist", shell=True).decode().lower()
                return "houdinifx.exe" in output
            else:
                output = subprocess.check_output(["pgrep", "-x", "houdinifx"]).decode().strip()
                return output != ""
        except Exception as e:
            print(f"Error checking Houdini process: {e}")
            return False

class HOUDINI_PT_Panel(bpy.types.Panel):
    bl_idname = "HOUDINI_PT_Panel"
    bl_label = "Houdini Menu"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Houdini'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.save_fbx", text="Save FBX")
        layout.operator("object.send_houdini", text="Send To Houdini")

def register():
    bpy.utils.register_class(HoudiniExporterPreferences)
    bpy.utils.register_class(SaveFBXOperator)
    bpy.utils.register_class(SendToHoudiniOperator)
    bpy.utils.register_class(HOUDINI_PT_Panel)

def unregister():
    bpy.utils.unregister_class(HoudiniExporterPreferences)
    bpy.utils.unregister_class(SaveFBXOperator)
    bpy.utils.unregister_class(SendToHoudiniOperator)
    bpy.utils.unregister_class(HOUDINI_PT_Panel)

if __name__ == "__main__":
    register()
