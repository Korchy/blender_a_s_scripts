# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

# cutting mesh vertices for mirror modifier

print('miror cut')


import bmesh
import bpy

print('miror cut')

axis = kwargs.get('axis', None)

print('axis', axis)

if axis and bpy.context.object:

    # current mode
    current_mode = bpy.context.object.mode
    if current_mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # cut geometry
    bm = bmesh.new()
    bm.from_mesh(bpy.context.object.data)
    # bm.verts.ensure_lookup_table()
    if axis == 'LEFT':
        vertices = (vert for vert in bm.verts if vert.co[0] < 0)
    elif axis == 'RIGHT':
        vertices = (vert for vert in bm.verts if vert.co[0] > 0)
    elif axis == 'TOP':
        vertices = (vert for vert in bm.verts if vert.co[2] > 0)
    elif axis == 'BOTTOM':
        vertices = (vert for vert in bm.verts if vert.co[2] < 0)
    elif axis == 'BACKWARD':
        vertices = (vert for vert in bm.verts if vert.co[1] > 0)
    elif axis == 'FORWARD':
        vertices = (vert for vert in bm.verts if vert.co[1] < 0)
    for vert in vertices:
        bm.verts.remove(vert)
    bm.to_mesh(bpy.context.object.data)
    bpy.context.object.data.update()
    bm.free()

    # for proper undo
    bpy.ops.ed.undo_push()

    # return mode
    bpy.ops.object.mode_set(mode=current_mode)
