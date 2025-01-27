# Mesh Origin Exporter ??

**A handy Blender add-on that takes each selected mesh, moves it to the world origin, and exports it as an individual FBX with a custom scale — then snaps everything back.** Perfect for modular assets, kitbashing, or quickly prepping geometry for game engines like Unreal or Unity.

---

## ? Features

- **Batch Export** multiple meshes in a single click.  
- **Zeroing Out**: Temporarily sets each mesh’s location to (0,?0,?0) so your exported FBX is “pivot?perfect” at the origin.  
- **Custom Scale**: Set a global scale factor to automatically size your assets.  
- **Non-Destructive**: Original scene transforms remain intact after export.  
- **Simple UI**: Access it from the 3D View’s Side Panel (N?Panel) under “Mesh Origin Exporter.”

---

## ?? Requirements

- Blender **2.93+** (should work on newer versions as well).  
- Windows, macOS, or Linux (wherever Blender runs).  
- A sense of adventure! ?????

---

## ?? Installation

1. **Download** or **clone** this repository.  
2. In Blender, go to **Edit ? Preferences ? Add-ons ? Install...**  
3. Select the `.py` file you downloaded (e.g., `mesh_origin_exporter.py`).  
4. Check the box to **Enable** the add-on.  

That’s it! You’ll now see a **Mesh Origin Exporter** tab in the right?hand sidebar of the 3D Viewport.

---

## ?? Usage

1. **Open** a Blender scene.  
2. **Select** the meshes you’d like to export.  
3. In the 3D View, press **N** to open the right Sidebar.  
4. Click the **Mesh Origin Exporter** tab.  
5. Adjust the **export path** and **scale** values if needed.  
6. Click **Export**.  

The add-on will:  
- Isolate each selected mesh,  
- Temporarily move it to the origin,  
- Export it as `YourMeshName.fbx` at your chosen scale,  
- Then restore it back to its original location.

---

## ?? Example Code Snippet

Below is a simplified portion of the operator’s core logic:

```python
for obj in selected_meshes:
    # Save transforms
    orig_loc = obj.location.copy()

    # Move to origin
    obj.location = (0.0, 0.0, 0.0)

    # Export
    bpy.ops.export_scene.fbx(
        filepath=os.path.join(export_folder, f"{obj.name}.fbx"),
        use_selection=True,
        global_scale=self.global_scale
    )

    # Restore transform
    obj.location = orig_loc
```

---

## ?? Customization

- **Add more export options**: You can edit the `bpy.ops.export_scene.fbx()` call to customize smoothing, tangents, or other FBX properties.  
- **Change the UI**: The panel is defined in `MESHORIGINEXPORTER_PT_Panel`. Modify the draw function to fit your workflow.

---

## ?? Known Issues / Limitations

- **Names**: If two objects share the same name, they’ll overwrite each other’s FBX file. Make sure your object names are unique.  
- **No advanced pivot editing**: This just sets the world origin; you may still need to do `Object ? Set Origin` if you want the pivot at the mesh’s center.  
- **FBX only**: The script uses `bpy.ops.export_scene.fbx`; you could adapt it for other formats if needed.

---

## ?? Contributions

Got improvements or bug fixes? Pull requests welcome! Feel free to submit an issue on GitHub if you find any quirks or have suggestions.

---

## ?? License

This project is provided under the **MIT License** (or any license you choose). You’re free to fork, extend, or integrate it into your pipeline.

---

**Happy exporting!** ? 