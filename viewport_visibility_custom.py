# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

import bpy
from bpy.props import BoolProperty
from bpy.types import WindowManager


# toggle status
if not hasattr(bpy.context.window_manager, 'a_s_scripts_viewport_visibility_custom_mode'):
    WindowManager.a_s_scripts_viewport_visibility_custom_mode = BoolProperty(
        name='viewport_visibility_custom_mode',
        default=False
    )

# change custom visibility
if bpy.context.window_manager.a_s_scripts_viewport_visibility_custom_mode:
    # True
    objects = (obj for obj in bpy.context.scene.objects if obj.type == 'MESH')
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
    bpy.context.window_manager.a_s_scripts_viewport_visibility_custom_mode = False
else:
    # False
    objects = (obj for obj in bpy.context.scene.objects if obj.type == 'MESH')
    for obj in objects:
        obj.data.polygons.foreach_set('use_smooth', [False] * len(obj.data.polygons))
        obj.data.update()
        # disable modifiers
        for modifier in obj.modifiers:
            modifier.show_viewport = False
    # show overlays
    bpy.context.space_data.overlay.show_overlays = True
    # toggle mode
    bpy.context.window_manager.a_s_scripts_viewport_visibility_custom_mode = True
