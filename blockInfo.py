
#
# remember to modify texcoords
#

BLOCKS={
    "GRASS" : {
        "special" : True,
        "texture-coords-top" : (
            (0, 0.95),
            (0.05, 0.95),
            (0.05, 1),
            (0, 1)
        ),
        "texture-coords-sides" : (
            (0.05, 0.95),
            (0.1, 0.95),
            (0.1, 1),
            (0.05, 1)
        ),
        "texture-coords-bottom" : (
            (0.1, 0.95),
            (0.15, 0.95),
            (0.15, 1),
            (0.1, 1)
        ),
    },
    "DIRT" : {
        "special" : False,
        "texture-coords" : (
            (0.15, 0.95),
            (0.2, 0.95),
            (0.2, 1),
            (0.15, 1)
        )
    },
    "TALLGRASS" : {
        "special" : True,
        "texture-coords" : (
            (0.2, 0.95),
            (0.25, 0.95),
            (0.25, 1),
            (0.2, 1)
        )
    }
}