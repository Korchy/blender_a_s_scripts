# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# enable/disable auto merge and snapping by vertices

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_auto_merge_mode'):
    WindowManager.a_s_scripts_auto_merge_mode = BoolProperty(
        name='auto_merge_mode',
        default=True
    )

if bpy.context.object:

    # mode
    if bpy.context.object.mode == 'OBJECT':
        bpy.ops.object.mode_set(mode='EDIT')

    # changes
    if bpy.context.window_manager.a_s_scripts_auto_merge_mode:
        # True
        # enable auto merge
        bpy.context.scene.tool_settings.use_mesh_automerge = True
        # enable snapping
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}
        # toggle mode
        bpy.context.window_manager.a_s_scripts_auto_merge_mode = False
    else:
        # False
        # disable auto merge
        bpy.context.scene.tool_settings.use_mesh_automerge = False
        # disable snapping
        bpy.context.scene.tool_settings.use_snap = False
        # toggle mode
        bpy.context.window_manager.a_s_scripts_auto_merge_mode = True
