bl_info = {
    "name": "Mesh Origin Exporter",
    "author": "YourName",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Mesh Origin Exporter",
    "description": "WIP: Operator skeleton for exporting meshes",
    "warning": "",
    "category": "Import-Export",
}

import bpy

# 1) Create an operator class
class MESHORIGINEXPORTER_OT_Export(bpy.types.Operator):
    """Exports each selected mesh (stub)"""
    bl_idname = "meshoriginexporter.export"
    bl_label = "Export Meshes (Stub)"

    def execute(self, context):
        # Right now, just print and finish
        self.report({'INFO'}, "Stub operator called!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MESHORIGINEXPORTER_OT_Export)
    print("Mesh Origin Exporter: registered")

def unregister():
    bpy.utils.unregister_class(MESHORIGINEXPORTER_OT_Export)
    print("Mesh Origin Exporter: unregistered")

if __name__ == "__main__":
    register()
