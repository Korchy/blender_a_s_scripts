# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# Same as modifiers_subd but only for selected meshes

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_modifiers_subd_mode_selected'):
    WindowManager.a_s_scripts_modifiers_subd_mode_selected = BoolProperty(
        name='modifiers_subd_mode_selected',
        default=False
    )

# change modifiers visibility
if bpy.context.window_manager.a_s_scripts_modifiers_subd_mode_selected:
    # True
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # enable modifiers
        modifiers = (modifier for modifier in obj.modifiers if modifier.type == 'SUBSURF')
        for modifier in modifiers:
            modifier.show_viewport = True
    # hide overlays
    bpy.context.space_data.overlay.show_overlays = False
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_subd_mode_selected = False
else:
    # False
    objects = (obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
    for obj in objects:
        # disable modifiers
        modifiers = (modifier for modifier in obj.modifiers if modifier.type == 'SUBSURF')
        for modifier in modifiers:
            modifier.show_viewport = False
    # show overlays
    bpy.context.space_data.overlay.show_overlays = True
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_subd_mode_selected = True
