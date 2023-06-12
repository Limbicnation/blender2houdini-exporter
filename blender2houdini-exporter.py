# Information for the Blender to Houdini addon
bl_info = {
    "name": "Blender to Houdini Exporter",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
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


class SendToHoudini(bpy.types.Operator):
    bl_idname = "object.send_houdini"
    bl_label = "Send To Houdini"

    Houdinipath = ''
    HoudiniScript = '/media/ws-ml/linux-drive/linux_projects/GitHub/blender2houdini-exporter/houdini_import_fbx.py'
    geoPath = '/media/ws-ml/linux-drive/linux_projects/Temp_geo/model.fbx'

    def execute(self, context):
        # Verify the path and print it to the console
        print(f"Exporting to path: {self.geoPath}")

        # Check that the export operator ID is correct
        print(f"Operator ID: {bpy.ops.export_scene.fbx.idname}")

        # export the selected object to the specified path
        bpy.ops.export_scene.fbx(filepath=self.geoPath, use_selection=True, global_scale=1)

        # Show a message box confirming the export
        message = f"Exported to {self.geoPath}"
        self.report({'INFO'}, message)
        print(message)

        # Check if Houdini is already running
        is_houdini_running = False

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
                output = subprocess.check_output('pgrep houdinifx', shell=True)
                is_houdini_running = output.strip() != b''
            except subprocess.CalledProcessError:
                pass
            houdini_path = '/opt/hfs19.5.640/bin/houdinifx'

        if not is_houdini_running:
            # launch Houdini
            cmd = [houdini_path, '-c', 'python', self.HoudiniScript]
            subprocess.Popen(cmd)
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
    SendToHoudini,
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
