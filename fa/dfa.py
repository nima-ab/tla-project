class DFA:  # TODO add description to the readme.md file and comment the damn code
    def __init__(self, states, input_symbols, transitions, init_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.init_state = init_state
        self.final_states = final_states

    def _get_next_state(self, current_state, input_symbol):
        if input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]
        else:
            raise Exception('Invalid Symbol!')

    def read_input_str(self, input_str):
        current_state = self.init_state
        visited_states = [current_state]

        for char in input_str: 
            current_state = self._get_next_state(current_state=current_state, input_symbol=char)
            visited_states.append(current_state)

        return visited_states, current_state