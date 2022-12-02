import bpy
from typing import Set
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty, EnumProperty, CollectionProperty
from bpy.types import Operator
from ..lib import pkginfo
from ..lib import util
from ..lib import blender_deepcopy_lib

if "_LOADED" in locals():
    import importlib

    for mod in (pkginfo, util, blender_deepcopy_lib):  # list all imports here
        importlib.reload(mod)
_LOADED = True

package_name = pkginfo.package_name()


def generate_enum_items(self, context) -> list[tuple[str, str, str]]:
    result = []
    for sign in "+-":
        for axis in "XYZ":
            result.append((f"{sign}{axis}", f"Align {sign}{axis}", f"Align something on the {sign}{axis} axis"))
    return result


class DeepCopyOperator(Operator):
    """Demonstration and debug tool for blender_deep_copy_lib"""
    bl_idname = "deepcopy_demo.an_operator"
    bl_label = "Deep Copy"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context) -> bool:
        return bool(bpy.context.selected_objects)

    def execute(self, context) -> Set[str]:
        blender_deepcopy_lib.deep_copy_objects(bpy.context.selected_objects, 'copy')
        return {'FINISHED'}


REGISTER_CLASSES = [DeepCopyOperator]
