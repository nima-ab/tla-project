from copy import copy
from collections import namedtuple


class NPDA:
    def __init__(self, states, input_symbols, stack_symbols, init_state, init_stack_symbol, transitions, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.init_state = init_state
        self.init_stack_symbol = init_stack_symbol
        self.transitions = transitions
        self.final_states = final_states