![alt text](https://github.com/Limbicnation/blender2houdini-exporter/blob/main/images/banner.png)

# Blender to Houdini Exporter

This is a Blender add-on that exports selected objects to FBX and launches Houdini.
To export your work from Houdini to Blender, you can use the provided HDA (Houdini Digital Asset)

Thanks to Simon Houdini for providing insight on his [method](https://www.youtube.com/watch?v=H5aY9wcbX3c&list=LL&index=3)

The link to my [tutorial](https://www.youtube.com/watch?v=Oue4qUfea4I) 

Tested with ```Blender 4.1.1```
```Houdini 20.0.688```

# Features 

•	Export selected objects to FBX.
•	Launch Houdini.
•	Automatically check if Houdini is already running and open the specified script if it is not.

# Installation

1. Download the repository.
2. In Blender, go to Edit > Preferences > Add-ons > Install.
3. Select the downloaded repository and extract the contents.
4. Select the scripts ```blender2houdini-exporter.py``` and ```blender_reload_fbx.py``` and "Install Add-on"
5. Enable the add-ons.
6. Go to Houdini and install the new digital Asset ```Export_to_Blender.1.0.hdalc``` (Note this project requires Houdini Indie and the Houdini Launcher to run)
7. Copy the ```houdini_importer.shelf``` to your ```/houdini19.5/toolbar/``` folder and activate the shelf

# Usage in Blender

To transfer your models from Blender to Houdini:

1. Select the objects you intend to export.
2. Navigate to the "Houdini" menu located in the sidebar.
3. Click the "Send To Houdini" option.
4. Upon executing, Houdini will automatically launch.
5. Your imported model will reside in the pre-defined location.
6. Important: To ensure seamless transfer, confirm that the path set for your model file within the scripts is accurate. Specifically, inspect the geoPath variable located in the ```blender2houdini-exporter.py```, ```houdini_import_fbx.py```, and ```houdini_reload_fbx.py``` scripts, making adjustments as necessary.

# Usage in Houdini

For the inverse operation, transferring models from Houdini to Blender:

1. Initiate by placing the Export_to_Blender HDA on your workspace.
2. Connect your desired output to the HDA.
3. Click on the "Save to Disk" button.
4. Switch over to Blender.
5. Reload your model.
6. Important: Paths play a crucial role in ensuring no hitches during the transfer. Double-check the path for your model file in both the Houdini shelf tools and within the houdini_import_fbx.py and houdini_reload_fbx.py scripts. Ensure all path references are correct and updated.

# Image instructions and installation details

<p float="left">
  <img src="https://github.com/Limbicnation/blender2houdini-exporter/blob/main/images/blender2houdini-exporter-Addon.png" width="100%">
  <img src="https://github.com/Limbicnation/blender2houdini-exporter/blob/main/images/reload-import-model.png" width="100%">
</p>

# Versioning

This project uses semantic versioning. The current version is v0.3.

# Contributing

Pull requests and bug reports are welcome! Please open an issue before submitting a pull request.

# License

Apache License 2.0
