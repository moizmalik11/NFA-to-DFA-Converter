import networkx as nx
import matplotlib.pyplot as plt
import json

# Load NFA from input.json
with open("input4.json", "r") as file:
    nfa = json.load(file)

# Convert transitions to edge list with combined labels
edge_dict = {}


# Create MultiDiGraph
G = nx.MultiDiGraph()
for (u, v), symbols in edge_dict.items():
    label = ",".join(symbols)
    G.add_edge(u, v, label=label)

# Generate positions dynamically based on states
state_names = sorted(set([f"q{i}" for i in range(nfa["states"])]))
pos = {state: (i * 1.8, 0) for i, state in enumerate(state_names)}

# Draw base graph
plt.figure(figsize=(8, 4))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=12, arrows=True)

# Final state: draw with border for double-circle effect
for state in nfa["final"]:
    nx.draw_networkx_nodes(G, pos, nodelist=[state], node_size=1500, node_color='lightgreen', edgecolors='black', linewidths=2)

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

# Start state arrow
start = pos[nfa["start"]]
plt.annotate("", xy=start, xytext=(start[0] - 1, start[1] + 0.5),
             arrowprops=dict(arrowstyle="->", lw=2))

plt.title("Dynamic NFA Visualization ")
plt.axis('off')
plt.tight_layout()
plt.show()
