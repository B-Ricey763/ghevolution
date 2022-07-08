from enum import Enum

from ghevolution.settings import X_SIZE, Y_SIZE


class Senses(Enum):
    X_POS = 0
    Y_POS = 1


display_names = {
    Senses.X_POS: "X",
    Senses.Y_POS: "Y",
}

sense_funcs = {
    Senses.X_POS: lambda pos: pos.x / X_SIZE,
    Senses.Y_POS: lambda pos: pos.y / Y_SIZE,
}
