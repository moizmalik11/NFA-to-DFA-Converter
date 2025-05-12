# import networkx as nx
# import matplotlib.pyplot as plt

# # JSON input
# nfa = {
#   "states": 3,
#   "letters": ["a", "b"],
#   "t_func": [
#     ["q0", "a", ["q0", "q1"]],
#     ["q0", "b", ["q0"]],
#     ["q1", "b", ["q2"]]
#   ],
#   "start": "q0",
#   "final": ["q2"]
# }


# # Convert transitions to edge list
# edges = []
# for from_state, symbol, to_states in nfa["t_func"]:
#     for to_state in to_states:
#         edges.append((from_state, to_state, symbol))

# # Create MultiDiGraph
# G = nx.MultiDiGraph()

# # Add edges
# for u, v, label in edges:
#     G.add_edge(u, v, label=label)

# # Define custom positions (optional)
# pos = {
#     'q0': (0, 0),
#     'q1': (2, 1),
#     'q2': (4, 1),
#     'q3': (6, 0)
# }

# # Draw the graph
# plt.figure(figsize=(8, 5))
# nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, arrows=True)

# # Edge labels
# edge_labels = nx.get_edge_attributes(G, 'label')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# # Final state (double circle look)
# nx.draw_networkx_nodes(G, pos, nodelist=nfa["final"], node_size=2000, node_color='lightgreen', linewidths=3)

# # Start state indicator
# start_pos = pos[nfa["start"]]
# plt.annotate("", xy=start_pos, xytext=(start_pos[0] - 1, start_pos[1] + 0.5),
#              arrowprops=dict(arrowstyle="->", color='black', lw=2))

# plt.title("NFA Visualization from JSON Input")
# plt.axis('off')
# plt.tight_layout()
# plt.show()
import json
import networkx as nx
import matplotlib.pyplot as plt

with open("input.json", "r") as file:
    nfa = json.load(file)

# Convert transitions to edge list
edges = []
for from_state, symbol, to_states in nfa["t_func"]:
    for to_state in to_states:
        edges.append((from_state, to_state, symbol))

G = nx.MultiDiGraph()

# Add edges
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define positions manually (optional)
pos = {
    'q0': (0, 0),
    'q1': (1.5, 0),
    'q2': (3, 0)
}

# Draw the graph
plt.figure(figsize=(6, 4))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Final state: double circle
nx.draw_networkx_nodes(G, pos, nodelist=['q2'], node_size=2000, node_color='lightgreen', linewidths=3)

plt.title("NFA Visualization (Alternative)")
plt.axis('off')
plt.show()
