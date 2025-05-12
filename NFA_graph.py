# import networkx as nx
# import matplotlib.pyplot as plt
# import json

# # Load NFA from input.json
# with open("input.json", "r") as file:
#     nfa = json.load(file)

# # Convert list to state name
# def list_to_state_name(state_list):
#     return "Ø" if not state_list else "{" + ",".join(sorted(state_list)) + "}"

# # Extract NFA components
# nfa_transitions = {}
# states = set()

# # For each transition in NFA, handle the state transitions
# for trans in nfa["t_func"]:
#     from_state = trans[0]
#     symbol = trans[1]
#     to_states = trans[2]

#     from_state_name = list_to_state_name([from_state])

#     # Each destination in the to_states list corresponds to a separate state in NFA
#     for to_state in to_states:
#         to_state_name = list_to_state_name([to_state])
#         nfa_transitions[(from_state_name, symbol)] = to_state_name

#     # Add states to the set
#     states.add(from_state_name)
#     states.update([list_to_state_name([to_state]) for to_state in to_states])

# # Start and final states of NFA
# nfa_states = list(states)
# nfa_start = list_to_state_name([nfa["start"]])
# nfa_final = [list_to_state_name([f]) for f in nfa["final"]]

# # Create graph
# G = nx.DiGraph()
# G.add_nodes_from(nfa_states)
# G.add_node("fake_start")  # Invisible dummy for initial arrow
# G.add_edge("fake_start", nfa_start, label="start")

# # Add NFA transitions
# for (src, symbol), dest in nfa_transitions.items():
#     G.add_edge(src, dest, label=symbol)

# # Manual positioning
# pos = {
#     "fake_start": (-2, 0),
#     nfa_start: (0, 0),
# }

# # Space out other states
# x, y = 1, 1
# for state in nfa_states:
#     if state not in pos:
#         pos[state] = (x, y)
#         y -= 2
#         if y < -5:
#             x += 2
#             y = 1

# # Color nodes
# node_colors = []
# for node in G.nodes():
#     if node == "fake_start":
#         node_colors.append("white")
#     elif node == nfa_start:
#         node_colors.append("lightgreen")
#     elif node in nfa_final:
#         node_colors.append("lightcoral")
#     else:
#         node_colors.append("lightblue")

# # Draw nodes
# nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, edgecolors='black')

# # Labels (skip fake_start)
# labels = {n: n for n in G.nodes() if n != "fake_start"}
# nx.draw_networkx_labels(G, pos, labels, font_size=12)

# # Draw curved edges
# for u, v, data in G.edges(data=True):
#     rad = 0.2 if u != "fake_start" else 0.0
#     nx.draw_networkx_edges(
#         G, pos,
#         edgelist=[(u, v)],
#         connectionstyle=f'arc3,rad={rad}',
#         arrows=True,
#         arrowstyle='->',
#         arrowsize=20,
#         edge_color='black'
#     )

# # Edge labels (skip dummy)
# edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True) if u != "fake_start"}
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# plt.title("Clean NFA Diagram")
# plt.axis('off')
# plt.tight_layout()
# plt.show()
