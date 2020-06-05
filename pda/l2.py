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

input_string = input('Enter the string you wanna check: ')
print('===============================')

if dfa.accept_input_str(input_string):
    print(f'String \'{input_string}\' is accepted by this language and the transitions are:')
    visited_states, _ = dfa.read_input_str(input_string)

    print(' -> ', end='')
    for i in range(len(visited_states)):
        print(visited_states[i], end='')

        if i != len(visited_states) - 1:
            print(' => ', end='')

else:
    print(f'String \'{input_string}\' is not accepted by this language!')
