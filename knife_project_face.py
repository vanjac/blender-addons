bl_info = {
    "name": "Knife Project Face",
    "description": "Use a face to project knife cuts onto the rest of the mesh.",
    "author": "Jacob van't Hoog",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "category": "Mesh",
    }

import bpy
import bmesh


class KnifeProjectFace(bpy.types.Operator):
    """Project knife cuts from selected faces onto the rest of the mesh."""
    bl_idname = "mesh.knife_project_face"
    bl_label = "Knife Project Face"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_MESH'
    
    def execute(self, context):
        old_selected = list(context.selected_objects)

        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.mesh.knife_project()

        added_objects = [o for o in context.selected_objects if o not in old_selected]
        for o in added_objects:
            bpy.data.objects.remove(o, do_unlink=True)
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(KnifeProjectFace)

def unregister():
    bpy.utils.unregister_class(KnifeProjectFace)

if __name__ == "__main__":
    register()
