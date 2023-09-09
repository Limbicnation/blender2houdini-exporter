bl_info = {
    "name": "Blender to Houdini Exporter",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (3, 6, 1),
    "location": "View3D > Sidebar > Houdini Menu",
    "description": "Export selected objects to FBX and launch Houdini",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export",
}

import os
import bpy
import subprocess
import re
import platform

class SendToHoudiniOperator(bpy.types.Operator):
    bl_idname = "object.send_houdini"
    bl_label = "Send To Houdini"

    def execute(self, context):
        # Paths for Houdini and export files
        HOUDINI_SCRIPT = '/media/ws-ml/linux-drive/linux_projects/GitHub/blender2houdini-exporter/houdini_import_fbx.py'
        
        # Set export path based on OS
        if platform.system() == 'Windows':
            GEO_PATH = 'I:\\Temp_geo\\model.fbx'
        elif platform.system() == 'Linux':
            GEO_PATH = '/home/ws-ml/Temp_geo/model.fbx'
        else:
            self.report({'ERROR'}, "Unsupported OS")
            return {'CANCELLED'}

        print(f"Exporting to path: {GEO_PATH}")

        bpy.ops.export_scene.fbx(filepath=GEO_PATH, use_selection=True, global_scale=1)
        message = f"Exported to {GEO_PATH}"
        self.report({'INFO'}, message)
        print(message)

        is_houdini_running = False
        houdini_path = ''

        if platform.system() == 'Windows':
            try:
                output = subprocess.check_output('tasklist', shell=True)
                output = output.decode('utf-8').lower()
                is_houdini_running = re.search(r'houdinifx\.exe', output) is not None
            except subprocess.CalledProcessError:
                pass
            houdini_path = r'C:\Program Files\Side Effects Software\Houdini 19.5.640\bin\houdinifx.exe'
        elif platform.system() == 'Linux':
            try:
                output = subprocess.check_output(['pgrep', 'houdinifx'])
                is_houdini_running = output.strip() != b''
            except subprocess.CalledProcessError:
                pass
            houdini_path = '/opt/hfs19.5.716/bin/houdinifx'

        if not is_houdini_running:
            cmd = [houdini_path, '-j', HOUDINI_SCRIPT]
            try:
                process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                stdout, stderr = process.communicate()
                print("STDOUT:", stdout.decode())
                print("STDERR:", stderr.decode())
            except Exception as e:
                print("Error launching Houdini:", e)
        else:
            print('Houdini is already running')

        return {'FINISHED'}

class HOUDINI_PT_Panel(bpy.types.Panel):
    bl_idname = "HOUDINI_PT_Panel"
    bl_label = "Houdini Menu"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Houdini'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_houdini", text="Send To Houdini")

classes = (
    SendToHoudiniOperator,
    HOUDINI_PT_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
