from collections import namedtuple
import bitstruct

Y_SIZE = 100
X_SIZE = 100
WEIGHT_DIV = 10000
NUM_ORGANISMS = 300
STEPS_PER_GEN = 300
CELL_SIZE = 10
NUM_GENERATIONS = 100
CONN_FORMAT = 'u8u8s16'
CONN_SIZE = bitstruct.calcsize(CONN_FORMAT)
CONN_NUM = 4
TOTAL_BYTES = CONN_SIZE // 8 * CONN_NUM
INNER_NEURONS = 1
MUTATION_CHANCE = 0.05
STEP_DISPLAY_TIME = 5  # millis
SHOULD_DISPLAY = True

Point = namedtuple("Point", "x, y")
