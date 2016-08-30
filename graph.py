class graph:

    class node:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        # if node is defined by its position
        def __eq__(self, other):
            return (self.x, self.y) == (other.x, other.y)

        def __hash__(self):
            return 8 * self.x - self.y

    def __init__(self):
        self.nodes = dict()

    def __contains__(self, n):
        return n in self.nodes

    def addNodeAtPos(self, x, y):
        new = graph.node(x, y)
        if new not in self.nodes:
            self.nodes[new] = set()
            return new
        else: return 

    def addEdge(self, edge):
        ax, ay, bx, by = edge
        n1 = self.addNodeAtPos(ax, ay)
        n2 = self.addNodeAtPos(bx, by)
        self.nodes[n1].add(n2)
        self.nodes[n2].add(n1)
