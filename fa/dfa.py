class DFA:
    def __init__(self, states, input_symbols, transitions, init_state, final_states):
        """ 
        :param states: A `set` of the DFA states' names which are strings.
        :param input_symbols: A `set` of valid alphabets.
        :param transitions: A `dictionary` consisting of the transitions for each state.
        The format is { start state: { input symbol: next state } }
        :param init_state: A string for the name of the initial state.
        :param final_states: A `set` of the DFA final states.
        """
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.init_state = init_state
        self.final_states = final_states

    def _get_next_state(self, current_state, input_symbol):
        """
        :param current_state: The name of the DFA current state.
        :param input_symbol: The alphabet that maps the current state to the next.
        :return: next state
        """
        if input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]
        else:
            raise Exception('Invalid Symbol!')

    def read_input_str(self, input_str):
        """
        Reads the input string step by step.
        :param input_str: A string given by the user to be checked by the DFA.
        :return: A list of the states which have been visited in every step.
        """
        current_state = self.init_state
        visited_states = [current_state]

        for char in input_str: 
            current_state = self._get_next_state(current_state=current_state, input_symbol=char)
            visited_states.append(current_state)

        return visited_states, current_state

    def accept_input_str(self, input_str):
        """
        :param input_str: A string given by the user to be checked by the DFA.
        :return: Whether a string is accepted by the DFA or not.
        """
        visited_states, last_state = self.read_input_str(input_str=input_str)

        if last_state in self.final_states:
            return True

        else:
            return False
