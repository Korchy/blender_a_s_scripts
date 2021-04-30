# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# move freeze transform - move object to saved freeze transform point

import bpy

if bpy.context.object:

    # return to saved object location
    if 'freeze_transform_point_0_0' in bpy.context.object:
        for i in range(4):
            for j in range(4):
                bpy.context.object.matrix_world[i][j] = bpy.context.object['freeze_transform_point_' + str(i) + '_' + str(j)]

    # for proper undo
    bpy.ops.ed.undo_push()
