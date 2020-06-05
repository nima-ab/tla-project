from dfa import DFA


dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0':{'a': 'q1', 'b': 'q2', 'c': 'q0'},
        'q1':{'a': 'q2', 'b': 'q0', 'c': 'q1'},
        'q2':{'a': 'q0', 'b': 'q1', 'c': 'q2'}
    },
    init_state='q0',
    final_states={'q1'}
)
