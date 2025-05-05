import networkx as nx
import matplotlib.pyplot as plt
import json

# Load DFA from output.json
with open("output.json", "r") as file:
    dfa = json.load(file)

# Convert list to state name
def list_to_state_name(state_list):
    return "Ø" if not state_list else "{" + ",".join(sorted(state_list)) + "}"

# Extract DFA components
dfa_transitions = {}
states = set()

for trans in dfa["t_func"]:
    from_state = list_to_state_name(trans[0])
    symbol = trans[1]
    to_state = list_to_state_name(trans[2])
    dfa_transitions[(from_state, symbol)] = to_state
    states.update([from_state, to_state])

dfa_states = list(states)
dfa_start = list_to_state_name([dfa["start"]])
dfa_final = [list_to_state_name(f) for f in dfa["final"]]

# Create graph
G = nx.DiGraph()
G.add_nodes_from(dfa_states)
G.add_node("fake_start")  # Invisible dummy for initial arrow
G.add_edge("fake_start", dfa_start, label="start")

# Add DFA transitions
for (src, symbol), dest in dfa_transitions.items():
    G.add_edge(src, dest, label=symbol)

# Manual positioning
pos = {
    "fake_start": (-2, 0),
    dfa_start: (0, 0),
}
# Space out other states
x, y = 1, 1
for state in dfa_states:
    if state not in pos:
        pos[state] = (x, y)
        y -= 2
        if y < -5:
            x += 2
            y = 1

# Color nodes
node_colors = []
for node in G.nodes():
    if node == "fake_start":
        node_colors.append("white")
    elif node == dfa_start:
        node_colors.append("lightgreen")
    elif node in dfa_final:
        node_colors.append("lightcoral")
    else:
        node_colors.append("lightblue")

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, edgecolors='black')

# Labels (skip fake_start)
labels = {n: n for n in G.nodes() if n != "fake_start"}
nx.draw_networkx_labels(G, pos, labels, font_size=12)

# Draw curved edges
for u, v, data in G.edges(data=True):
    rad = 0.2 if u != "fake_start" else 0.0
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[(u, v)],
        connectionstyle=f'arc3,rad={rad}',
        arrows=True,
        arrowstyle='-|>',
        arrowsize=20,
        edge_color='black'
    )

# Edge labels (skip dummy)
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True) if u != "fake_start"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Clean DFA Diagram")
plt.axis('off')
plt.tight_layout()
plt.show()
