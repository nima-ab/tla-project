from copy import copy
from collections import namedtuple


class PDA:
    def __init__(self, states, input_symbols, stack_symbols, init_state, init_stack_symbol, transitions, final_states):
        """
        :param states: A `set` of the PDA states' names which are strings.
        :param input_symbols: A `set` of valid alphabets.
        :param stack_symbols: A `set` of valid symbols for PDA stack.
        :param init_state: A string for the name of the initial state.
        :param init_stack_symbol: A string for the first item in the PDA stack.
        :param transitions: A `dictionary` consisting of the transitions for each state.
        The Format is { start state: { stack top symbol: { input symbol: ( next state, (pop symbol, push symbol ) ) } } }.
        :param final_states: A `set` of the PDA final states.
        """
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.init_state = init_state
        self.init_stack_symbol = init_stack_symbol
        self.transitions = transitions
        self.final_states = final_states

    def _get_transition(self, current_state, input_symbol, stack_symbol):
        """
        :param current_state: The name of the PDA current state.
        :param input_symbol: The alphabet that maps the current state to the next.
        :param stack_symbol: The stack symbol that is supposed to be on top of the stack.
        :return: The transition tha matches the given parameter which contains
        the next state and the pop and push stack symbol.
        """
        if (current_state in self.transitions and
                stack_symbol in self.transitions[current_state] and
                input_symbol in self.transitions[current_state][stack_symbol]):

            return self.transitions[current_state][stack_symbol][input_symbol]

    def _get_next_config(self, transition, old_config):
        """
        :param transition: A `tuple` which contains the next state and the pop and push symbol.
        :param old_config: A `PDAConfig` that is contains the current state and PDA stack in that state.
        :return: The next state's config and its name.
        """
        next_state, pop_push_symbols = transition
        pop_symbol, push_symbol = pop_push_symbols
        new_stack = old_config.stack.copy()
        
        if pop_symbol is not None and new_stack[-1] == pop_symbol:
            new_stack.pop()

        if push_symbol is not None:
            new_stack.append(push_symbol)

        new_state = PDAConfig(next_state, new_stack)

        return new_state, next_state

    def read_input_str(self, input_str):
        """
        Reads the input string step by step.
        :param input_str:  A string given by the user to be checked by the PDA.
        :return:  A list of the states as PDAConfigs which have been visited in every step.
        """
        current_state = self.init_state
        current_stack = [self.init_stack_symbol]
        current_config = PDAConfig(current_state, current_stack)
        states = [current_config]

        try:
            for char in input_str:
                transition = self._get_transition(current_state=current_state, input_symbol=char, stack_symbol=current_config.stack[-1])
                current_config, current_state = self._get_next_config(transition=transition, old_config=current_config)
                states.append(current_config)

            transition = self._get_transition(current_state=current_state, input_symbol='', stack_symbol='$')
            current_config, current_state = self._get_next_config(transition=transition, old_config=current_config)
            states.append(current_config)
            last_state = current_config

            return states, last_state

        except Exception:
            last_state = current_config

            return states, last_state

    def accepts_input_str(self, input_str):
        """
        :param input_str: A string given by the user to be checked by the DFA.
        :return: Whether a string is accepted by the PDA or not.
        """
        states, last_state = self.read_input_str(input_str=input_str)
        state, stack = last_state

        if state in self.final_states and stack == ['$']:
            return True

        else:
            return False


class PDAConfig(namedtuple(
        'PDAConfig',
        ['state', 'stack'])):
    """
    A class which inherits the builtin namedtuple datatype.
    It's used to show the PDA state and that state's stack easier and better.
    """

    def __str__(self):
        return f'({self.state} {self.stack})'
