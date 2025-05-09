import json

# Load the DFA from a JSON file
try:
    with open('output.json') as file:
        dfa = json.load(file)
except FileNotFoundError:
    print("❌ Error: 'output.json' file not found.")
    exit(1)

# Extract DFA components
transitions = dfa.get("t_func", [])
start_state = dfa.get("start")
final_states = dfa.get("final", [])

# DFA Simulation Function
def simulate_dfa(input_string):
    current_state = (start_state,)

    for symbol in input_string:
        transition_found = False
        for trans in transitions:
            if list(current_state) == trans[0] and symbol == trans[1]:
                current_state = tuple(trans[2])
                transition_found = True
                break
        if not transition_found:
            print(f"⚠️ No transition found for symbol '{symbol}' from state {current_state}.")
            return False

    return list(current_state) in final_states

# User input
print("🔄 DFA Simulator 🔄")
test_string = input("Enter a string using the DFA's alphabet: ").strip()

# Run simulation
if simulate_dfa(test_string):
    print("✅ String ACCEPTED by the DFA!")
else:
    print("❌ String REJECTED by the DFA.")
