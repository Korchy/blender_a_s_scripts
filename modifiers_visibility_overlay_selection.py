# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# Same as modifiers_visibility_overlay but only for selected objects

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_modifiers_visibility_overlay_mode'):
    WindowManager.a_s_scripts_modifiers_visibility_overlay_mode = BoolProperty(
        name='modifiers_visibility_overlay_mode',
        default=False
    )

# change modifiers visibility
if bpy.context.window_manager.a_s_scripts_modifiers_visibility_overlay_mode:
    # True
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # enable modifiers
        for modifier in obj.modifiers:
            modifier.show_viewport = True
    # hide overlays
    bpy.context.space_data.overlay.show_overlays = False
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_visibility_overlay_mode = False
else:
    # False
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # disable modifiers
        for modifier in obj.modifiers:
            modifier.show_viewport = False
    # show overlays
    bpy.context.space_data.overlay.show_overlays = True
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_visibility_overlay_mode = True
