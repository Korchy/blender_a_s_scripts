# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# cutting mesh vertices for mirror modifier

import bpy

if bpy.context.object:

    if bpy.context.object.mode == 'EDIT':

        # duplicate
        bpy.ops.mesh.duplicate()

        # separate
        bpy.ops.mesh.separate()

    # for proper undo
    bpy.ops.ed.undo_push()
