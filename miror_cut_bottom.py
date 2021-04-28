# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# cutting mesh vertices for mirror modifier

import bmesh
import bpy

if bpy.context.object:

    # current mode
    current_mode = bpy.context.object.mode
    if current_mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # cut geometry
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    # bm.verts.ensure_lookup_table()
    vertices = (vert for vert in bm.verts if vert.co[2] < 0)
    for vert in vertices:
        bm.verts.remove(vert)
    bm.to_mesh(bpy.context.object.data)
    bpy.context.object.data.update()
    bm.free()

    # for proper undo
    bpy.ops.ed.undo_push()

    # return mode
    bpy.ops.object.mode_set(mode=current_mode)
