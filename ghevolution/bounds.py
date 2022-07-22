from settings import *

bound_presets = (
    (Point(0, 0), Point(30, Y_SIZE)),  # Left side
    (Point(0, 0), Point(30, 30)),  # Top left corner
    (Point(0, Y_SIZE // 2 - 20), Point(30, Y_SIZE // 2 + 20)),  # Mid left
    (Point(0, Y_SIZE - 20), Point(30, Y_SIZE)),  # Bottom left
    (Point(X_SIZE // 2 - 20, 0),
     Point(X_SIZE // 2 + 20, Y_SIZE)),  # Center
)

bound_index = 0
bounds = bound_presets[bound_index]


def cycle_bounds():
    global bound_index, bounds
    bound_index = (bound_index + 1) % len(bound_presets)
    bounds = bound_presets[bound_index]


def get_bounds():
    return bounds
