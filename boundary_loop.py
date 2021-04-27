# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

import bpy

current_mode = bpy.context.object.mode if bpy.context.object else 'OBJECT'
if current_mode == 'EDIT':
    # switch to vertex selection
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
    # select boundary loops
    bpy.ops.mesh.region_to_loop()
