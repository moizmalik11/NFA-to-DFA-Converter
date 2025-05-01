import json

# Load the DFA
with open('output.json') as file:
    dfa = json.load(file)

# DFA ka structure
transitions = dfa["t_func"]
start_state = dfa["start"]
final_states = dfa["final"]

# Function to simulate DFA
def simulate_dfa(input_string):
    current_state = (start_state,)

    for symbol in input_string:
        found = False
        for trans in transitions:
            if list(current_state) == trans[0] and symbol == trans[1]:
                current_state = tuple(trans[2])
                found = True
                break
        if not found:
            return False
    return list(current_state) in final_states

# Example
test_string = input("Enter a string to test: ")
if simulate_dfa(test_string):
    print("String accepted by DFA!")
else:
    print("String rejected by DFA.")
