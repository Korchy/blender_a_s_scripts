# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# The same as viewport_visibility_custom but only for selected meshes

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_viewport_visibility_selection_mode'):
    WindowManager.a_s_scripts_viewport_visibility_selection_mode = BoolProperty(
        name='viewport_visibility_selection_mode',
        default=False
    )

current_mode = bpy.context.object.mode if bpy.context.object else 'OBJECT'
if current_mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')

# change custom visibility
if bpy.context.window_manager.a_s_scripts_viewport_visibility_selection_mode:
    # True
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # smooth
        obj.data.polygons.foreach_set('use_smooth', [True] * len(obj.data.polygons))
        obj.data.update()
        # enable modifiers
        for modifier in obj.modifiers:
            modifier.show_viewport = True
    # show overlays
    bpy.context.space_data.overlay.show_overlays = False
    # toggle mode
    bpy.context.window_manager.a_s_scripts_viewport_visibility_selection_mode = False
else:
    # False
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # flat
        obj.data.polygons.foreach_set('use_smooth', [False] * len(obj.data.polygons))
        obj.data.update()
        # disable modifiers
        for modifier in obj.modifiers:
            modifier.show_viewport = False
    # show overlays
    bpy.context.space_data.overlay.show_overlays = True
    # toggle mode
    bpy.context.window_manager.a_s_scripts_viewport_visibility_selection_mode = True

bpy.ops.object.mode_set(mode=current_mode)
