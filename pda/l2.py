from dfa import DFA


dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0':{'a': 'q1', 'b': 'q1', 'c': 'q1'},
        'q1':{'a': 'q0', 'b': 'q0', 'c': 'q0'}
    },
    init_state='q0',
    final_states={'q0'}
)