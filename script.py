import json
from collections import OrderedDict

# Load input NFA
with open('input.json') as file:
    data = json.load(file)

dfa_letters = data["letters"]
dfa_start = data["start"]
dfa_t_func = []
dfa_final = []
q = []

q.append((dfa_start,))  # Initial DFA state as a tuple

# Build NFA transition dictionary
nfa_transitions = {}
dfa_transitions = {}

for transition in data["t_func"]:
    nfa_transitions[(transition[0], transition[1])] = transition[2]
    


# Subset construction to convert NFA to DFA
for in_state in q:
    print("Current state:", in_state)
    for symbol in dfa_letters:
        print("Current symbol:", symbol)
        dest = []
        final_dest = []   
        for state in in_state:
            print("State:", state)
            targets = nfa_transitions.get((state, symbol), [])
            print("Targets:", targets)
            for next_state in targets:
                print("Next state:", next_state)
                if next_state not in final_dest:
                    final_dest.append(next_state)

        final_dest.sort()  # Optional: for consistent state names

        if final_dest:
            dfa_transitions[(in_state, symbol)] = final_dest
            next_state = tuple(final_dest)
            if next_state not in q:
                q.append(next_state)

# Build DFA transition function list
for key, value in dfa_transitions.items():
    dfa_t_func.append([list(key[0]), key[1], value])

# Identify DFA final states
dfa_final = []
for q_state in q:
    for f_state in data["final"]:
        if f_state in q_state and list(q_state) not in dfa_final:
            dfa_final.append(list(q_state))

# Build DFA dictionary
dfa = OrderedDict()
dfa["states"] = len(q)
dfa["letters"] = dfa_letters
dfa["t_func"] = dfa_t_func
dfa["start"] = dfa_start
dfa["final"] = dfa_final

# Write to output file
with open('output.json', 'w') as output_file:
    json.dump(dfa, output_file, indent=2)
