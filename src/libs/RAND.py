# libs/rand.py

import random

def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def get_random_float():
    return random.random()

def get_random_range(min_val, max_val, step):
    return random.randrange(min_val, max_val, step)

# Connecting
LIB_FUNCS["rand.integer"] = get_random_int
LIB_FUNCS["rand.floating"] = get_random_float
LIB_FUNCS["rand.ranges"] = get_random_range
