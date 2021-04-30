# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# moving object to the center of the scene

import bpy

if bpy.context.object:

    # current mode
    bpy.context.object.location = (0.0, 0.0, 0.0)

    # for proper undo
    bpy.ops.ed.undo_push()
