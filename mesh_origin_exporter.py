bl_info = {
    "name": "Mesh Origin Exporter",
    "author": "YourName",
    "version": (1, 2),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Mesh Origin Exporter",
    "description": "Exports each selected mesh to FBX at world origin, with UI for folder & scale",
    "warning": "",
    "category": "Import-Export",
}

import bpy
import os

class MESHORIGINEXPORTER_OT_Export(bpy.types.Operator):
    """Exports each selected mesh to FBX at the world origin."""
    bl_idname = "meshoriginexporter.export"
    bl_label = "Export Meshes"

    # Properties (exposed in the panel)
    export_folder: bpy.props.StringProperty(
        name="Export Folder",
        description="Folder where FBX files will be saved",
        default=r"C:\MyExports",
        subtype='DIR_PATH'
    )
    global_scale: bpy.props.FloatProperty(
        name="Global Scale",
        description="Scale factor for export",
        default=0.1,
        min=0.0001,
        max=100.0
    )

    def execute(self, context):
        if not os.path.isdir(self.export_folder):
            try:
                os.makedirs(self.export_folder, exist_ok=True)
            except Exception as e:
                self.report({'ERROR'}, f"Could not create folder: {str(e)}")
                return {'CANCELLED'}

        selected_meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not selected_meshes:
            self.report({'WARNING'}, "No mesh objects selected.")
            return {'CANCELLED'}

        for obj in selected_meshes:
            # Store original transforms
            orig_loc = obj.location.copy()
            orig_rot = obj.rotation_euler.copy()
            orig_scale = obj.scale.copy()

            # Move to origin
            obj.location = (0.0, 0.0, 0.0)

            # Temporarily isolate selection
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj

            # Build filepath
            fbx_path = os.path.join(self.export_folder, f"{obj.name}.fbx")

            # Export FBX
            bpy.ops.export_scene.fbx(
                filepath=fbx_path,
                use_selection=True,
                global_scale=self.global_scale,
                apply_unit_scale=True,
                use_space_transform=True
            )

            # Restore transforms
            obj.location = orig_loc
            obj.rotation_euler = orig_rot
            obj.scale = orig_scale

        # Reselect them all
        bpy.ops.object.select_all(action='DESELECT')
        for o in selected_meshes:
            o.select_set(True)

        self.report({'INFO'}, f"Exported {len(selected_meshes)} mesh(es) to {self.export_folder}")
        return {'FINISHED'}

class MESHORIGINEXPORTER_PT_Panel(bpy.types.Panel):
    """Creates a Panel in the 3D View Sidebar"""
    bl_label = "Mesh Origin Exporter"
    bl_idname = "MESHORIGINEXPORTER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mesh Origin Exporter"

    def draw(self, context):
        layout = self.layout

        # Draw a heading
        layout.label(text="Batch Export to FBX at Origin:")

        # Create an Operator property layout
        op = layout.operator("meshoriginexporter.export", text="Export")
        op.export_folder = r"C:\MyExports"  # Could read from a global, context, etc.
        op.global_scale = 0.1

def register():
    bpy.utils.register_class(MESHORIGINEXPORTER_OT_Export)
    bpy.utils.register_class(MESHORIGINEXPORTER_PT_Panel)
    print("Mesh Origin Exporter: registered")

def unregister():
    bpy.utils.unregister_class(MESHORIGINEXPORTER_PT_Panel)
    bpy.utils.unregister_class(MESHORIGINEXPORTER_OT_Export)
    print("Mesh Origin Exporter: unregistered")

if __name__ == "__main__":
    register()
