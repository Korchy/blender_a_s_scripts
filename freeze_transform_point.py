# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# point freeze transform - save current position of the object

# import copy
import bpy

if bpy.context.object:

    # save object location
    for i, row in enumerate(bpy.context.object.matrix_world):
        for j, col in enumerate(row):
            bpy.context.object['freeze_transform_point_' + str(i) + '_' + str(j)] = col
