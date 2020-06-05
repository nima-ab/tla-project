from pda.npda import NPDA


pda = NPDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    stack_symbols={'$', '0', '1'},
    transitions={
        'q0': {
            '0': {
                'a': ('q0', (None, '0')),
                'b': ('q0', (None, '1')),
                'c': ('q1', (None, None))
            },
            '1': {
                'a': ('q0', (None, '0')),
                'b': ('q0', (None, '1')),
                'c': ('q1', (None, None))
            },
            '$': {
                'a': ('q0', (None, '0')),
                'b': ('q0', (None, '1')),
                'c': ('q1', (None, None))
            }
        },
        'q1': {
            '$': {
                '': ('q2', (None, None))
            },
            '0': {
                'a': ('q1', ('0', None))
            },
            '1': {
                'b': ('q1', ('1', None))
            }
        }
    },
    init_state='q0',
    init_stack_symbol='$',
    final_states={'q2'}
)
