class DFA:  # TODO add description to the readme.md file and comment the damn code
    def __init__(self, states, input_symbols, transitions, init_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.init_state = init_state
        self.final_states = final_states