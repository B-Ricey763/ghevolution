from secrets import randbits, token_hex
import numpy as np
import bitstruct
from random import choice, randrange, uniform, getrandbits
import string

# The format has a couple values:
# Boolean: whether it comes from sensory or internal neuron
# Unsigned int: the id of the neuron it comes from
# Boolean: whether or not it goes to inner or ouput neuron
# Unsigned int: the id of the neuron it comes from
# Float: weight of connection (16 bits is overkill but the package can't do less)
CONN_FORMAT = 'b1u7b1u7s16'
CONN_SIZE = bitstruct.calcsize(CONN_FORMAT)
CONN_NUM = 1
TOTAl_BYTES = CONN_SIZE // 8 * CONN_NUM


def encode(geneList):
    arr = bytearray(TOTAl_BYTES)
    for i, gene in enumerate(geneList):
        bitstruct.pack_into(CONN_FORMAT, arr, CONN_SIZE * i, *gene)
    return arr.hex()


def generate():
    return token_hex(TOTAl_BYTES)


def mutate(genes):
    # Since hex has 16 digits, we just want to get one random one as a string
    randHex = choice('0123456789abcdef')
    i = randrange(0, len(genes))
    # We get two seperate slices of the string and mash them together with
    # the new random hex value
    return (genes[:i] + randHex + genes[i+1:])


def decode(genes):
    # List comprehension getting each connection as tuple
    # I know its ugly but its elegant
    return [bitstruct.unpack_from(
        CONN_FORMAT, bytearray.fromhex(genes), CONN_SIZE * i)
        for i in range(CONN_NUM)]
