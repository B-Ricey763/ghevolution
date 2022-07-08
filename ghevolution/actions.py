
from enum import Enum
from settings import *


class Actions(Enum):
    MOVE_LEFT = 0
    MOVE_RIGHT = 1
    MOVE_UP = 2
    MOVE_DOWN = 3


display_names = {
    Actions.MOVE_LEFT: "Left",
    Actions.MOVE_RIGHT: "Right",
    Actions.MOVE_UP: "Up",
    Actions.MOVE_DOWN: "Down",
}


action_funcs = {
    Actions.MOVE_LEFT: lambda pos: Point((pos.x - 1) % X_SIZE, pos.y),
    Actions.MOVE_RIGHT: lambda pos: Point((pos.x + 1) % X_SIZE, pos.y),
    Actions.MOVE_UP: lambda pos: Point(pos.x, (pos.y - 1) % Y_SIZE),
    Actions.MOVE_DOWN: lambda pos: Point(pos.x, (pos.y + 1) % Y_SIZE),
}
