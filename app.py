# app.py

import organisasjon
import plotly.graph_objects as go

# Hent person-objektene
# personer = organisasjon.personer
personer = organisasjon.les_organisasjon_fra_json()

# Forbered data for Plotly (enklere eksempel)
nodes = [person.navn for person in personer]
links = []
for person in personer:
    if person.sjef:
        links.append(dict(source=nodes.index(person.navn), target=nodes.index(person.sjef)))

# Opprett figuren
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = nodes,
      color = "blue"
    ),
    link = dict(
      source = [i for i in range(len(links))], # indices correspond to labels in `node`
      target = [links[i]['target'] for i in range(len(links))],
      value = [1]*len(links)
  ))])

fig.update_layout(title_text="Organisasjonskart", font_size=10)
fig.show()