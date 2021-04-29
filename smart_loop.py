# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# modifying loop selection for edges and faces

import bmesh
import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AS_SCRIPTS_OT_smart_loop(Operator):
    bl_idname = 'as_scripts.smart_loop'
    bl_label = 'Smart Loop'
    bl_description = 'Smart Loop'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print(5)
        if context.tool_settings.mesh_select_mode[0] or context.tool_settings.mesh_select_mode[1]:
            # vertices or edges
            bpy.ops.mesh.loop_multi_select(ring=False)
        else:
            # selected 2 polygons
            # find common edge
            bpy.ops.object.mode_set(mode='OBJECT')
            selected_faces = [face for face in context.object.data.polygons if face.select]
            middle_edge_keys = next(iter((set(selected_faces[0].edge_keys) & set(selected_faces[1].edge_keys))), None)
            if middle_edge_keys:
                print(middle_edge_keys)
                middle_edge = next(iter(edge for edge in context.object.data.edges if set(edge.vertices) == set(middle_edge_keys)), None)
                if middle_edge:
                    # switch to edges
                    bpy.context.tool_settings.mesh_select_mode = (False, True, False)
                    # select middle edge
                    for polygon in context.object.data.polygons:
                        polygon.select = False
                    for edge in context.object.data.edges:
                        edge.select = False
                    for vertex in context.object.data.vertices:
                        vertex.select = False
                    middle_edge.select = True
                    # select loop (ring)
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.loop_multi_select(ring=True)
                    # transform selection to polygons
                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                    bpy.context.tool_settings.mesh_select_mode = (False, False, True)
                else:
                    bpy.ops.object.mode_set(mode='EDIT')
            else:
                bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

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
            keymap_item = keymap.keymap_items.new('as_scripts.smart_loop', 'F', 'PRESS')
            # keymap_item = keymap.keymap_items.new('as_scripts.smart_loop', 'F', 'PRESS', shift=True)
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
