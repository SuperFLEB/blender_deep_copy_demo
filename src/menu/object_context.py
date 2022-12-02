import bpy
from ..operator import deep_copy

if "_LOADED" in locals():
    import importlib

    for mod in (deep_copy,):  # list all imports here
        importlib.reload(mod)
_LOADED = True


class DeepCopyDemoSubmenu(bpy.types.Menu):
    bl_idname = 'deepcopy_demo.deepcopy_demo'
    bl_label = 'Deep Copy Demo'

    def draw(self, context) -> None:
        self.layout.operator(deep_copy.DeepCopyOperator.bl_idname)


REGISTER_CLASSES = [DeepCopyDemoSubmenu]
