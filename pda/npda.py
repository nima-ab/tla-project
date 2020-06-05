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

    def _get_transition(self, current_state, input_symbol, stack_symbol):
        if (current_state in self.transitions and
                stack_symbol in self.transitions[current_state] and
                input_symbol in self.transitions[current_state][stack_symbol]):

            return self.transitions[current_state][stack_symbol][input_symbol]

    def _get_next_config(self, transition, old_config):
        next_state, pop_push_symbols = transition
        pop_symbol, push_symbol = pop_push_symbols
        new_stack = old_config.stack.copy()
        
        if pop_symbol is not None and new_stack[-1] == pop_symbol:
            new_stack.pop()

        if push_symbol is not None:
            new_stack.append(push_symbol)

        new_state = PDAConfig(next_state, new_stack)

        return new_state, next_state


class PDAConfig(
    namedtuple(
        'PDAConfig',
        ['state', 'stack']
)):

    def __str__(self):
        return f'({self.state} {self.stack})'