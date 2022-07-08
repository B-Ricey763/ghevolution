from collections import namedtuple
import bitstruct

Y_SIZE = 100
X_SIZE = 100
WEIGHT_DIV = 10000
NUM_ORGANISMS = 300
STEPS_PER_GEN = 300
CELL_SIZE = 8
NUM_GENERATIONS = 10
CONN_FORMAT = 'u8u8s16'
CONN_SIZE = bitstruct.calcsize(CONN_FORMAT)
CONN_NUM = 3
TOTAL_BYTES = CONN_SIZE // 8 * CONN_NUM
INNER_NEURONS = 1
MUTATION_CHANCE = 0.05
STEP_DISPLAY_TIME = 10  # millis
LEFT_BOUND = X_SIZE
TOP_BOUND = 20
SHOULD_DISPLAY = False

Point = namedtuple("Point", "x, y")
