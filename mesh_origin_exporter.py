bl_info = {
    "name": "Mesh Origin Exporter",
    "author": "YourName",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Mesh Origin Exporter",
    "description": "WIP: Skeleton for an add-on to export selected meshes",
    "warning": "",
    "category": "Import-Export",
}

import bpy

def register():
    print("Mesh Origin Exporter: registered")

def unregister():
    print("Mesh Origin Exporter: unregistered")

if __name__ == "__main__":
    register()
