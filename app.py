import networkx as nx
import matplotlib.pyplot as plt

# Opprett en rettet graf (for å vise hierarki)
G = nx.DiGraph()

# Legg til noder (personer)
G.add_nodes_from(['Skrue Duck', 'Donald Duck', 'Anton Duck', 'Bestemor Duck'])

# Legg til kanter (forhold)
G.add_edges_from([('Skrue Duck', 'Donald Duck'), ('Skrue Duck', 'Anton Duck'), ('Skrue Duck', 'Bestemor Duck')])

# Tegn grafen
pos = nx.spring_layout(G)  # Posisjonere nodene
nx.draw(G, pos, with_labels=True, font_weight='bold')

# Vis grafen
plt.show()