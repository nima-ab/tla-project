from pda import PDA


pda = PDA(
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
    final_states={'q5'}
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
