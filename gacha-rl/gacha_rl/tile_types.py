from typing import Tuple

import numpy as np #type: ignore

#Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #unicode codepoint
        ("fg", "3B"), #3 unsigned bytes, for RGB colors
        ("bg", "3B")
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #can this be walked over
        ("transparent", np.bool), #does this block fov
        ("dark", graphic_dt) #what does this look like out of fov
    ]
)

def new_tile(*, walkable:int, transparent:int, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> np.ndarray:
    """
    Helper function for definining individual tile types
    """
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord(' '), (255,255,255), (50,50,150)))
wall = new_tile(walkable=False, transparent=False, dark=(ord(' '), (255,255,255), (0,0,100)))