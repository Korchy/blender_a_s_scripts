# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# quick align by X,Y, or Z axis

import bpy

if bpy.context.object:

    bpy.ops.transform.resize(value=(0, 1, 1))

    # for proper undo
    bpy.ops.ed.undo_push()
