import networkx as nx
import matplotlib.pyplot as plt

# Opprett en rettet graf
G = nx.DiGraph()

# Legg til noder med jobbtitler
nodes = [
    ('Skrue Duck', 'Sjef'),
    ('Donald Duck', 'Arbeider'),
    ('Anton Duck', 'PR-sjef'),
    ('Bestemor Duck', 'HR-sjef')
]
G.add_nodes_from(nodes)

# Legg til kanter
edges = [
    ('Skrue Duck', 'Donald Duck'),
    ('Skrue Duck', 'Anton Duck'),
    ('Skrue Duck', 'Bestemor Duck')
]
G.add_edges_from(edges)

# Tegn grafen med firkantede noder og jobbtitler
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_shape='s', node_size=1500, font_weight='bold')

# Legg til jobbtitler som node-etiketter
node_labels = nx.get_node_attributes(G, 'Jobbtittel')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, verticalalignment='bottom')

plt.show()