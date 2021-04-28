# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# enable/disable "affect only origin" mode and snapping by vertices

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_only_origin_mode'):
    WindowManager.a_s_scripts_only_origin_mode = BoolProperty(
        name='only_origin_mode',
        default=True
    )

current_mode = bpy.context.object.mode if bpy.context.object else 'OBJECT'
if current_mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')

# change custom visibility
if bpy.context.window_manager.a_s_scripts_only_origin_mode:
    # True
    # enable affect only origin
    bpy.context.scene.tool_settings.use_transform_data_origin = True
    # snapping - vertex
    bpy.context.scene.tool_settings.use_snap = True
    bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}
    # toggle mode
    bpy.context.window_manager.a_s_scripts_only_origin_mode = False
else:
    # False
    # disable affect only origin
    bpy.context.scene.tool_settings.use_transform_data_origin = False
    # disable snapping
    bpy.context.scene.tool_settings.use_snap = False
    # toggle mode
    bpy.context.window_manager.a_s_scripts_only_origin_mode = True
