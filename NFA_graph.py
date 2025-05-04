import json
import networkx as nx
import matplotlib.pyplot as plt

# Load NFA from input.json
with open("input.json", "r") as file:
    nfa = json.load(file)

# Extract all unique states from transitions
states_set = set()
for from_state, symbol, to_states in nfa["t_func"]:
    states_set.add(from_state)
    for to_state in to_states:
        states_set.add(to_state)
states_set.add(nfa["start"])
states_set.update(nfa["final"])
states = sorted(states_set)

# Create MultiDiGraph
G = nx.MultiDiGraph()
for state in states:
    G.add_node(state)
for from_state, symbol, to_states in nfa["t_func"]:
    for to_state in to_states:
        G.add_edge(from_state, to_state, label=symbol)

# Position the nodes manually for better control
pos = {
    "q0": (0, 0),
    "q1": (2, 1.5),
    "q2": (4, 0)
}
# Auto fallback if more states exist
for state in states:
    if state not in pos:
        pos[state] = (len(pos) * 2, 0)

# Node colors (final state = red)
node_colors = ['red' if state in nfa["final"] else 'skyblue' for state in states]
node_border_colors = ['darkred' if state in nfa["final"] else 'black' for state in states]

# Draw nodes with borders
for state, color, border in zip(states, node_colors, node_border_colors):
    nx.draw_networkx_nodes(G, pos, nodelist=[state],
                           node_color=color, edgecolors=border,
                           linewidths=2, node_size=1500)

# Draw state labels
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

# Draw curved edges for clarity
nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.25',
                       arrows=True, arrowstyle='->', width=2)

# Edge labels
edge_labels = {(u, v, k): d['label'] for u, v, k, d in G.edges(keys=True, data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Better positioned start arrow (bottom-left of start state)
start_pos = pos[nfa["start"]]
arrow_start = (start_pos[0] - 0.8, start_pos[1] - 0.5)
plt.annotate("",
             xy=start_pos, xytext=arrow_start,
             arrowprops=dict(arrowstyle="->", lw=2))

# Title and layout
plt.title("NFA", fontsize=18, fontweight='bold', color='navy')
plt.axis('off')
plt.tight_layout()
plt.show()
