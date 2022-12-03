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


class DeepCopyOperator(Operator):
    """Demonstration and debug tool for blender_deep_copy_lib"""
    bl_idname = "deepcopy_demo.an_operator"
    bl_label = "Deep Copy"
    bl_options = {'REGISTER', 'UNDO'}

    prefix: StringProperty(name="Prefix", default='copy')
    prefer_existing_materials: BoolProperty(name="Use existing materials/node groups", default=False, description="If materials or node groups with this prefix exist in the document already, use them instead of copying.")

    @classmethod
    def poll(cls, context) -> bool:
        return bool(bpy.context.selected_objects)

    def draw(self, context) -> None:
        self.layout.prop(self, "prefix")
        self.layout.prop(self, "prefer_existing_materials")

    def invoke(self, context, event) -> Set[str]:
        util.reset_operator_defaults(self, [
            "prefix",
            "prefer_existing_materials"
        ])

        return self.execute(context)

    def execute(self, context) -> Set[str]:
        obj_copies = blender_deepcopy_lib.deep_copy_objects(bpy.context.selected_objects, self.prefix)
        material_copies = blender_deepcopy_lib.deep_copy_materials(obj_copies, self.prefix, self.prefer_existing_materials)
        blender_deepcopy_lib.deep_copy_material_nodegroups(material_copies, self.prefix, self.prefer_existing_materials)
        return {'FINISHED'}


REGISTER_CLASSES = [DeepCopyOperator]
