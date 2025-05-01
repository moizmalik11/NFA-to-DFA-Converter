import networkx as nx
import matplotlib.pyplot as plt

# DFA definition
dfa_states = ['{q0}', '{q1}', '{q1,q2}', 'Ø']
dfa_start = '{q0}'
dfa_final = ['{q1,q2}']
dfa_transitions = {
    ('{q0}', 'a'): '{q1}',
    ('{q0}', 'b'): '{q0}',
    ('{q1}', 'a'): '{q1,q2}',
    ('{q1}', 'b'): 'Ø',
    ('{q1,q2}', 'a'): '{q1,q2}',
    ('{q1,q2}', 'b'): 'Ø',
    ('Ø', 'a'): 'Ø',
    ('Ø', 'b'): 'Ø'
}

G = nx.DiGraph()

# Add nodes
for state in dfa_states:
    G.add_node(state)

# Add transitions
for (src, symbol), dest in dfa_transitions.items():
    G.add_edge(src, dest, label=symbol)

# Layout settings (shell_layout for better circular view)
pos = nx.shell_layout(G)

# Color settings
node_colors = []
for node in G.nodes():
    if node == dfa_start:
        node_colors.append('lightgreen')  # Start state
    elif node in dfa_final:
        node_colors.append('lightcoral')  # Final state
    else:
        node_colors.append('lightblue')   # Other states

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500, edgecolors='black')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, connectionstyle='arc3, rad=0.2', arrows=True, arrowsize=20)

# Draw edge labels
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title('DFA Graph')
plt.axis('off')
plt.show()