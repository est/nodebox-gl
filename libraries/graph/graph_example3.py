try:
    graph = ximport("graph")
except ImportError:
    graph = ximport("__init__")
    reload(graph)

size(500, 500)

g = graph.create(iterations=1000, distance=1.2, layout="spring")

# Add nodes with a random id,
# connected to other random nodes.
for i in range(30):
    node1 = g.add_node(random(500))
    if random() > 0.5:
        for i in range(choice((1, 4))):
            node2 = choice(g.nodes)
            g.add_edge(node1.id, node2.id, weight=random())

g.prune()
g.styles.apply()

speed(30)
def draw():
    
    # If the graph layout is done,
    # show the shortest path between random nodes.
    path = []
    if g.done:
        id1 = choice(g.keys())
        id2 = choice(g.keys())
        path = g.shortest_path(id1, id2)    
        
    # Draw the graph and display the shortest path.
    g.draw(highlight=path, traffic=4, weighted=True, directed=True)
