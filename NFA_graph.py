import networkx as nx
import matplotlib.pyplot as plt

# NFA graph
G_nfa = nx.MultiDiGraph()

# Add NFA nodes and edges
G_nfa.add_node('q0')
G_nfa.add_node('q1')
G_nfa.add_node('q2')

G_nfa.add_edge('q0', 'q1', label='a')
G_nfa.add_edge('q1', 'q1', label='a')
G_nfa.add_edge('q1', 'q2', label='λ')
G_nfa.add_edge('q2', 'q0', label='b')

# Layout
pos_nfa = {
    'q0': (0, 0),
    'q1': (2, 1),
    'q2': (4, 0)
}

plt.figure(figsize=(10, 5))

# Draw nodes
nx.draw_networkx_nodes(G_nfa, pos_nfa, node_color='skyblue', node_size=1500)
nx.draw_networkx_labels(G_nfa, pos_nfa, font_size=14)

# Draw edges
nx.draw_networkx_edges(G_nfa, pos_nfa, arrows=True)
edge_labels_nfa = {(u, v): d['label'] for u, v, d in G_nfa.edges(data=True)}
nx.draw_networkx_edge_labels(G_nfa, pos_nfa, edge_labels=edge_labels_nfa, font_size=12)

# Highlight start state
plt.annotate("", xy=pos_nfa['q0'], xytext=(-1, 0),
             arrowprops=dict(arrowstyle="->", lw=2))

# Titles
plt.text(0, 2, "NFA  M", fontsize=18, fontweight='bold', color='blue')
plt.title('Example', fontsize=20, fontweight='bold')
plt.axis('off')
plt.show()
