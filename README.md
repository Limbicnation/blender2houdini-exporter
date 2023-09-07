![alt text](https://github.com/Limbicnation/blender2houdini-exporter/blob/main/banner.png)

# Blender to Houdini Exporter

This is a Blender add-on that exports selected objects to FBX and launches Houdini.
To export your work from Houdini to Blender, you can use the provided HDA (Houdini Digital Asset)

Thanks to Simon Houdini for providing insight on his [method](https://www.youtube.com/watch?v=H5aY9wcbX3c&list=LL&index=3)

The link to my [tutorial](https://www.youtube.com/watch?v=Oue4qUfea4I) 

Tested with ```Blender 3.6.2```
```Houdini 19.5.716```

# Features 

•	Export selected objects to FBX.
•	Launch Houdini.
•	Automatically check if Houdini is already running and open the specified script if it is not.

# Installation

1. Download the repository.
2. In Blender, go to Edit > Preferences > Add-ons > Install.
3. Select the downloaded repository and exttract the contents.
5. Select the scritps ```blender2houdini-exporter.py``` and ```blender_reload_fbx.py``` and "Install Add-on"
4. Enable the add-on's.
5. Go to Houdini and install the new digital Asset ```Export_to_Blender.1.0.hdalc``` (Note this project requires Houdini Indie and the Houdini Launcher to run)
6. Copy the ```houdini_importer.shelf``` to your ```/houdini19.5/toolbar/``` folder and activate the shelf

# Usage in Blender

1. Select the objects you want to export.
2. Go to the "Houdini" menu in the sidebar.
3. Click "Send To Houdini".
4. Houdini will launch and the imported file will be available in the specified location.
5. Note: Ensure you set the correct path for your model file in the scripts. Check the geoPath variable in the blender2houdini-exporter.py, houdini_import_fbx.py, and houdini_reload_fbx.py scripts, and adjust them to your needs.

# Usage in Houdini

1. Place down the ```Export_to_Blender``` hda and connect yout output 
2. Click ```Save to Disk```
3. In Blender reload model.
4. Note: Also, ensure you set the correct path for your model file in the Houdini shelf tools and in the scripts houdini_import_fbx.py and houdini_reload_fbx.py if they reference any paths.

# Versioning

This project uses semantic versioning. The current version is v0.2.

# Contributing

Pull requests and bug reports are welcome! Please open an issue before submitting a pull request.

# License

Apache License 2.0
