# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_a_s_scripts

import bpy

value = kwargs.get('value', None)

if bpy.context.object and bpy.context.object.mode == 'EDIT':
    # selected edge
    bpy.ops.object.mode_set(mode='OBJECT')
    selected_edge = next((edge for edge in bpy.context.object.data.edges if edge.select), None)
    bpy.ops.object.mode_set(mode='EDIT')
    if selected_edge:
        # cut selected edge
        bpy.ops.mesh.loopcut_slide(
            MESH_OT_loopcut={
                'number_cuts': 2,
                'smoothness': 0,
                'falloff': 'INVERSE_SQUARE',
                'object_index': 0,
                'edge_index': selected_edge.index,
                'mesh_select_mode_init': (True, False, False)
            },
            # TRANSFORM_OT_edge_slide={
            #     'value': 0,
            #     'single_side': False,
            #     'use_even': True,
            #     'flipped': False,
            #     'use_clamp': True,
            #     'mirror': True,
            #     'snap': False,
            #     'snap_target': 'CLOSEST',
            #     'snap_point': (0, 0, 0),
            #     'snap_align': False,
            #     'snap_normal': (0, 0, 0),
            #     'correct_uv': True,
            #     'release_confirm': False,
            #     'use_accurate': False
            # }
        )
    # fix data or vert_slige works wrong
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    # slide to borders
    bpy.ops.transform.vert_slide(
        value=value,
        use_even=False,
        mirror=True,
        correct_uv=True
    )

    # for proper undo
    bpy.ops.ed.undo_push()
