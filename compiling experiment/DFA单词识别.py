def parse_dfa(definition):
    states = {}
    for line in definition.strip().split("\n"):
        parts = line.split()
        state = parts[0]
        transitions = parts[1:]
        state_transitions = {}
        for trans in transitions:
            if "->" in trans:
                input_char, next_state = trans.split("->")
                state_transitions[input_char[-1]] = next_state
        states[state] = state_transitions
    return states

def process_word(dfa, word):
    current_state = 'X'  # initial state
    for char in word:
        if char == '#':
            break
        if char not in dfa[current_state]:
            return "error"
        current_state = dfa[current_state][char]
    return "pass" if current_state == 'Y' else "error"

# DFA Definition
# # Test Words
# words = ["bba#", "ababb#", "aca#"]
def parse_input():
    dfa_def = ''
    words = []
    while True:
        line = input()
        if line == '':
            break
        dfa_def = dfa_def + '\n' + line
    while True:
        line = input()
        if line == '':
            break
        words.append(line)
    return dfa_def, words

if __name__ == '__main__':
    dfa_def,words = parse_input()
    dfa = parse_dfa(dfa_def)
    for word in words:
        result = process_word(dfa, word)
        print(result)
