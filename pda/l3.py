from npda import NPDA


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

input_string = input('Enter the string you wanna check: ')
print('===============================')

if pda.accepts_input_str(input_string):
    print(f'String \'{input_string}\' is accepted by this language and the transitions are:')
    visited_states, _ = pda.read_input_str(input_string)

    print(' -> ', end='')
    for i in range(len(visited_states)):
        print(visited_states[i], end='')

        if i != len(visited_states) - 1:
            print(' => ', end='')

else:
    print(f'String \'{input_string}\' is not accepted by this language!')
