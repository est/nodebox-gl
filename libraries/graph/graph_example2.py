try:
    graph = ximport("graph")
except ImportError:
    graph = ximport("__init__")
    reload(graph)

size(600, 600)

# A graph object.
g = graph.create(iterations=500, distance=1.0)

# Add nodes with a random id,
# connected to other random nodes.
for i in range(50):
    node1 = g.add_node(random(500))
    if random() > 0.5:
        for i in range(choice((2, 3))):
            node2 = choice(g.nodes)
            g.add_edge(node1.id, node2.id, weight=random())

# We leave out any orphaned nodes.
g.prune()

# Colorize nodes.
# Nodes with higher importance are blue.
g.styles.apply()

# Update the graph layout until it's done.
g.solve()

# Show the shortest path between two random nodes.
path = []
id1 = choice(g.keys())
id2 = choice(g.keys())
path = g.shortest_path(id1, id2)

# Draw the graph and display the shortest path.
g.draw(highlight=path, weighted=True, directed=True)
