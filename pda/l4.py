from pda.npda import NPDA


pda = NPDA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b', 'c'},
    stack_symbols={'$', '0', '1'},
    transitions={
        'q0': {
            '$': {'a': ('q1', (None, '0'))}
        },
        'q1': {
            '0': {
                'a': ('q1', (None, '0')),
                'b': ('q2', ('0', None))
            }
        },
        'q2': {
            '0': {'b': ('q2', ('0', None))},
            '$': {'b': ('q3', (None, '1'))}
        },
        'q3': {
            '1': {
                'b': ('q3', (None, '1')),
                'a': ('q4', ('1', None))
            }
        },
        'q4': {
            '1': {'a': ('q4', ('1', None))},
            '$': {'': ('q5', ('$', '$'))}
        },
    },
    init_state='q0',
    init_stack_symbol='$',
    final_states={'q5'}
)
