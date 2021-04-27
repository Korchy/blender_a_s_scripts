# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# subdivision modifier visibility and show/hide overlays in viewport

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_modifiers_subd_mode'):
    WindowManager.a_s_scripts_modifiers_subd_mode = BoolProperty(
        name='modifiers_subd_mode',
        default=False
    )

# change modifiers visibility
if bpy.context.window_manager.a_s_scripts_modifiers_subd_mode:
    # True
    objects = (obj for obj in bpy.context.scene.objects if obj.type == 'MESH')
    for obj in objects:
        # enable modifiers
        modifiers = (modifier for modifier in obj.modifiers if modifier.type == 'SUBSURF')
        for modifier in modifiers:
            modifier.show_viewport = True
    # hide overlays
    bpy.context.space_data.overlay.show_overlays = False
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_subd_mode = False
else:
    # False
    objects = (obj for obj in bpy.context.scene.objects if obj.type == 'MESH')
    for obj in objects:
        # disable modifiers
        modifiers = (modifier for modifier in obj.modifiers if modifier.type == 'SUBSURF')
        for modifier in modifiers:
            modifier.show_viewport = False
    # show overlays
    bpy.context.space_data.overlay.show_overlays = True
    # toggle mode
    bpy.context.window_manager.a_s_scripts_modifiers_subd_mode = True
