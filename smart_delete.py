# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# quick deleting vertices in vertex select mode, edges - in edges select mode, faces - in faces select

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AS_SCRIPTS_OT_smart_delete(Operator):
    bl_idname = 'as_scripts.smart_delete'
    bl_label = 'Smart delete'
    bl_description = 'Smart Delete'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.tool_settings.mesh_select_mode[0]:
            # vertex select
            bpy.ops.mesh.delete(type='VERT')
        elif context.tool_settings.mesh_select_mode[1]:
            # edges select
            bpy.ops.mesh.delete(type='EDGE')
        elif context.tool_settings.mesh_select_mode[2]:
            # faces select
            bpy.ops.mesh.delete(type='FACE')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.object and context.object.mode == 'EDIT')


class AS_SCRIPTS_SMART_DELETE_KeyMap:
    _keymaps = []

    @classmethod
    def register(cls, context):
        # add new key map
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='Mesh')
            # add keys
            keymap_item = keymap.keymap_items.new('as_scripts.smart_delete', 'DEL', 'PRESS')
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    register_class(AS_SCRIPTS_OT_smart_delete)
    AS_SCRIPTS_SMART_DELETE_KeyMap.register(context=bpy.context)


def unregister():
    AS_SCRIPTS_SMART_DELETE_KeyMap.unregister()
    unregister_class(AS_SCRIPTS_OT_smart_delete)


register()
