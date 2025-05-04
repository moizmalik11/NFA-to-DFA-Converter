import networkx as nx
import matplotlib.pyplot as plt

# Create the NFA graph as a MultiDiGraph
G_nfa = nx.MultiDiGraph()

# Add nodes
G_nfa.add_nodes_from(['q0', 'q1', 'q2'])

# Add transitions (edges)
G_nfa.add_edge('q0', 'q1', label='a')
G_nfa.add_edge('q1', 'q1', label='a')
G_nfa.add_edge('q1', 'q2', label='λ')
G_nfa.add_edge('q2', 'q0', label='b')

# Define positions
pos_nfa = {
    'q0': (0, 0),
    'q1': (2, 1),
    'q2': (4, 0)
}

plt.figure(figsize=(10, 5))

# Draw nodes and labels
nx.draw_networkx_nodes(G_nfa, pos_nfa, node_color='skyblue', node_size=1500)
nx.draw_networkx_labels(G_nfa, pos_nfa, font_size=14)

# Draw directed edges with visible arrowheads
nx.draw_networkx_edges(
    G_nfa, pos_nfa, arrows=True,
    arrowstyle='->', arrowsize=20, connectionstyle='arc3,rad=0.1'
)

# Draw edge labels (with keys for MultiDiGraph)
edge_labels_nfa = {(u, v, k): d['label'] for u, v, k, d in G_nfa.edges(keys=True, data=True)}
nx.draw_networkx_edge_labels(G_nfa, pos_nfa, edge_labels=edge_labels_nfa, font_size=12)

# Mark start state
plt.annotate("", xy=pos_nfa['q0'], xytext=(-1, 0),
             arrowprops=dict(arrowstyle="->", lw=2))

# Add title and remove axes
# plt.text(0, 2, "NFA :", fontsize=10, fontweight='bold', color='blue')
plt.title('Example NFA', fontsize=20, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
