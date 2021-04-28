# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# quick align by X,Y, or Z axis

import bpy

axis = kwargs.get('axis', None)

if axis and bpy.context.object:

    if axis == 'X':
        bpy.ops.transform.resize(value=(0, 1, 1))
    elif axis == 'Y':
        bpy.ops.transform.resize(value=(1, 0, 1))
    elif axis == 'Z':
        bpy.ops.transform.resize(value=(1, 1, 0))

    # for proper undo
    bpy.ops.ed.undo_push()
