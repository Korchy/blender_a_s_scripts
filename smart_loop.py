# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# modifying loop selection for edges and faces
# with using the following hack:
#   mesh.loop_select - throws an error when try to execute from tis operator
#   so
#       1. remap the default system shortcode from mouse-left-click + alt to the same button F-press
#       2. when edges or vertices selection mode - executed this operator and finished
#       3. when face selection mode - here we path through and the default system operator will be executed
#   but this without the guarantee of right order of executing (first this operator - next default system operator)
#       so if order will be not right - this may not works

import bpy
from bpy.props import BoolProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AS_SCRIPTS_OT_smart_loop(Operator):
    bl_idname = 'as_scripts.smart_loop'
    bl_label = 'Smart Loop'
    bl_description = 'Smart Loop'
    bl_options = {'REGISTER', 'UNDO'}

    ring: BoolProperty(
        default=False
    )

    def execute(self, context):
        if context.tool_settings.mesh_select_mode[0] or context.tool_settings.mesh_select_mode[1]:
            # vertices or edges
            bpy.ops.mesh.loop_multi_select(ring=self.ring)
            return {'FINISHED'}
        else:
            # bpy.ops.mesh.loop_select() - can't be called, throws an error
            # so try to pass to execute it from the default system shortcode (must be remapped to the same keymap as this)
            return {'PASS_THROUGH'}

    @classmethod
    def poll(cls, context):
        return bool(context.object and context.object.mode == 'EDIT')


class AS_SCRIPTS_SMART_LOOP_KeyMap:
    _keymaps = []

    @classmethod
    def register(cls, context):
        # add new key map
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='Mesh')
            # add keys
            # keymap_item = keymap.keymap_items.new('as_scripts.smart_loop', 'F', 'PRESS', shift=True)
            keymap_item = keymap.keymap_items.new('as_scripts.smart_loop', 'F', 'PRESS')
            keymap_item.properties.ring = False
            keymap_item = keymap.keymap_items.new('as_scripts.smart_loop', 'F', 'PRESS', ctrl=True, alt=True)
            keymap_item.properties.ring = True
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    register_class(AS_SCRIPTS_OT_smart_loop)
    AS_SCRIPTS_SMART_LOOP_KeyMap.register(context=bpy.context)


def unregister():
    AS_SCRIPTS_SMART_LOOP_KeyMap.unregister()
    unregister_class(AS_SCRIPTS_OT_smart_loop)


register()
