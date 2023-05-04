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

import bpy
import os
import subprocess

class BlenderToHoudiniExporter(bpy.types.Panel):
    bl_idname = "Houdini_panel"
    bl_category = "Houdini"
    bl_label = "Houdini Menu"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_houdini")

class SendToHoudini(bpy.types.Operator):
    bl_idname = "object.send_houdini"
    bl_label = "Send To Houdini"

    def execute(self, context):
        # Verify the path and print it to the console
        fbxPath = 'I:/Temp_geo/model.fbx'
        print(f"Exporting to path: {fbxPath}")
        
        # Check that the export operator ID is correct
        print(f"Operator ID: {bpy.ops.export_scene.fbx.idname}")
        
        # export the selected object to the specified path
        bpy.ops.export_scene.fbx(filepath=fbxPath, use_selection=True, global_scale=1)
        
        # Show a message box confirming the export
        message = f"Exported to {fbxPath}"
        self.report({'INFO'}, message)
        print(message)

        # Check if Houdini is already running
        is_houdini_running = False
        p = subprocess.Popen('tasklist', stdout=subprocess.PIPE, shell=True)
        for line in p.stdout:
            if b'houdini' in line.lower():
                is_houdini_running = True
                break
        
        if not is_houdini_running:
            # launch Houdini
            Houdinipath = 'C:/Program Files/Side Effects Software/Houdini 19.5.569/bin/hindie.exe'
            # Local path of your scripts folder, Launch Houdini importer script
            HoudiniScript = 'I:/GitHub/Tools/blender2houdini-exporter/invoke-houdini-shelf.py'

            cmd = [Houdinipath, '-c', 'python', HoudiniScript]
            subprocess.Popen(cmd)
        else:
            print('Houdini is already running')
        
        return {'FINISHED'}
        
def register():
    bpy.utils.register_class(BlenderToHoudiniExporter)
    bpy.utils.register_class(SendToHoudini)

def unregister():
    bpy.utils.unregister_class(BlenderToHoudiniExporter)
    bpy.utils.unregister_class(SendToHoudini)

if __name__=="__main__":
    register()
