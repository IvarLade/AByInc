import plotly.graph_objects as go

# Legg til noder med jobbtitler
nodes = [
    ('Skrue Duck', 'Sjef'),
    ('Donald Duck', 'Arbeider'),
    ('Anton Duck', 'PR-sjef'),
    ('Bestemor Duck', 'HR-sjef')
]

# Opprette et Plotly-diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [node for node, _ in nodes],
      color = ["blue", "green", "red", "purple"]  # Tilpass farger
    ),
    link = dict(
      source = [0, 0, 0],  # Indekser til kildenoden
      target = [1, 2, 3],  # Indekser til målnoden
      value = [1, 1, 1]  # Verdi for hver link
  ))])

fig.show()