import os
import bpy
import subprocess
import platform


class SendToHoudini(bpy.types.Operator):
    bl_idname = "object.send_houdini"
    bl_label = "Send To Houdini"
    
    if platform.system() == "Windows":
        Houdinipath = r'C:\Program Files\Side Effects Software\Houdini 19.5.569\bin\hindie.exe'
        HoudiniScript = r'I:\GitHub\Tools\blender2houdini-exporter\houdini_import_fbx.py'
    elif platform.system() == "Linux":
        Houdinipath = '/opt/hfs19.5.640/bin/houdini'
        HoudiniScript = '/media/ws-ml/linux-drive/linux_projects/GitHub/blender2houdini-exporter/houdini_import_fbx.py'  # Update with the correct path
        
    export = None

    def execute(self, context):
        # Verify the path and print it to the console
        fbxPath = '/media/ws-ml/linux-drive/linux_projects/Temp_geo/model.fbx'  # Update with the desired export path
        print(f"Exporting to path: {fbxPath}")
        
        # Check that the export operator ID is correct
        print(f"Operator ID: {bpy.ops.export_scene.fbx.idname}")
        
        # Export the selected object to the specified path
        bpy.ops.export_scene.fbx(filepath=fbxPath, use_selection=True, global_scale=1)
        
        # Show a message box confirming the export
        message = f"Exported to {fbxPath}"
        self.report({'INFO'}, message)
        print(message)

        # Launch Houdini
        cmd = [self.Houdinipath, '-c', 'python', self.HoudiniScript]
        subprocess.Popen(cmd, shell=True)
        
        return {'FINISHED'}
        

def register():
    bpy.utils.register_class(SendToHoudini)


def unregister():
    bpy.utils.unregister_class(SendToHoudini)


if __name__ == "__main__":
    register()
