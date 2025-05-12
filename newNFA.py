import networkx as nx
import matplotlib.pyplot as plt

# JSON input
nfa = {
    "states": 4,
    "letters": ["a", "b", "λ"],
    "t_func": [
        ["q0", "a", ["q0", "q1"]],
        ["q0", "b", ["q0"]],
        ["q1", "a", ["q2"]],
        ["q2", "b", ["q3"]],
        ["q3", "a", ["q3"]],
        ["q1", "λ", ["q3"]],
        ["q2", "λ", ["q0"]]
    ],
    "start": "q0",
    "final": ["q3"]
}

# Convert transitions to edge list
edges = []
for from_state, symbol, to_states in nfa["t_func"]:
    for to_state in to_states:
        edges.append((from_state, to_state, symbol))

# Create MultiDiGraph
G = nx.MultiDiGraph()

# Add edges
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define custom positions (optional)
pos = {
    'q0': (0, 0),
    'q1': (2, 1),
    'q2': (4, 1),
    'q3': (6, 0)
}

# Draw the graph
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, arrows=True)

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Final state (double circle look)
nx.draw_networkx_nodes(G, pos, nodelist=nfa["final"], node_size=2000, node_color='lightgreen', linewidths=3)

# Start state indicator
start_pos = pos[nfa["start"]]
plt.annotate("", xy=start_pos, xytext=(start_pos[0] - 1, start_pos[1] + 0.5),
             arrowprops=dict(arrowstyle="->", color='black', lw=2))

plt.title("NFA Visualization from JSON Input")
plt.axis('off')
plt.tight_layout()
plt.show()
