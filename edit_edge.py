# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# switch to edit mode, edge selection

import bpy

if bpy.context.object:

    # mode
    if bpy.context.object.mode == 'OBJECT':
        bpy.ops.object.mode_set(mode='EDIT')

    # selection - edges
    bpy.context.tool_settings.mesh_select_mode = (False, True, False)
