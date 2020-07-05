from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gacha_rl.engine import Engine
    from gacha_rl.entity import Entity

class Action:
    def perform (self, engine:Engine, entity:Entity) -> None:
        """Perform this action with the objects needed to determine its scope.
        Engine is the scope.
        Entity is the object performing the action.
        This MUST be overridden"""
        raise NotImplementedError()
class EscapeAction(Action):
    def perform(self, engine, entity):
        raise SystemExit()
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy
    
    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        if not engine.game_map.in_bounds(dest_x, dest_y):
            return #Destination out of bounds
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return #destination blocked
        entity.move(self.dx, self.dy)