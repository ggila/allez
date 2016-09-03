
import heapq
from itertools import count

# node id is a dict key: it musts be hashable (__eq__ and __hash__ should be define).
# it should also have __str__ for graph.__repr__

# if some time some day, change node and edge representation (dict -> namedtuple)

class graph:

    def __init__(self, nodes=[], edges=[]):
        self.nodes, self.edges = dict(), dict()
        for n in nodes: self.addNode(n)
        self.addEdges(edges)

    def __repr__(self):
        def getEdgesRepr(self):
            return ', '.join(['({}, True, {})'.format(a, c) for a, b in self.edges.items() for c in b])

        return '{0}(nodes=({1}), edges=({2}))'.format(self.__class__.__name__,
                                                      ', '.join([str(a) for a in self.nodes]),
                                                      getEdgesRepr(self))

    def __str__(self):
        def getWeight(self, nodeId, neighbours):
            return ', '.join(['{} {}'.format(n, tuple(self.edges[(nodeId, n)])) for n in neighbours])
        l = [(k, v['pos'], v['neigh']) for (k,v) in self.nodes.items()]
        return '\n'.join(['{} ({}): {}'.format(str(a),b,getWeight(self, a, c)) for (a, b, c) in l])

    def __getitem__(self, nodeId):
        return self.nodes[nodeId]

    def __contains__(self, n):
        return n in self.nodes

    def _getNode(self, nodeId):
        ''' return node with nodeId (initialize new node if nodeId does not exist) '''
        if nodeId not in self.nodes:
            self.nodes[nodeId] = {'neigh' : set(),
                                  'pos' : None}
        return self.nodes[nodeId]

    def _getEdge(self, edge):
        ''' return edge, initialize new edge if it does not exist '''
        if edge not in self.edges:
            self.edges[edge] = []
        return self.edges[edge]

    def getNeighbour(self, nodeId):
        return self.nodes[nodeId]['neigh']

    def addNode(self, nodeId, position=None, neighbour=set()):
        node = self._getNode(nodeId)
        if node['pos'] and node['pos'] != position:
            raise Exception('node {} already defined, position conflict'.format(nodeId))
        node['pos'] = position
        for n in neighbour: self.addEdge(nodeId, n)

    def addNodes(self, nodes):
        for n in nodes: self.addNode(n)

    def addDirectedEdge(self, nId1, nId2, weight=1):
        edge = self._getEdge((nId1, nId2))
        edge.append(weight)
        n1 = self._getNode(nId1)
        n1['neigh'].update((nId2,))

    def addEdge(self, nId1, nId2, directed=False, weight=1):
        self.addDirectedEdge(nId1, nId2, weight)
        if not directed:
            self.addDirectedEdge(nId2, nId1, weight)

    def addEdges(self, edges=[], directed_edges=[]):
        for e in edges: self.addEdge(*e)
        for e in directed_edges: self.addEdge(*e, directed=True)

    def _findCircuit(self, start, way, remain):
        neighbour = self.nodes[way[-1]]['neigh']
        if not remain and start in neighbour:
            yield way + [start]
        for n in neighbour:
            if n != start and n not in way:
                yield from self._findCircuit(start, way + [n], remain - 1)

    def findCircuit(self):
        ''' genrator which yield circuit in random order '''
        for k, v in self.nodes.items():
            yield from self._findCircuit(k, [k], len(self.nodes) - 1)
        yield []

    def findEulerianPath(self):
        pass

    def _findPath(self, start, end, h, counter):
        if not h: return
        W, _, way, wway = heapq.heappop(h)
        if way[-1] == end:
            yield (way, wway)
        else:
            for n in self.getNeighbour(way[-1]):
                if n not in way:
                    for w in self.edges[(way[-1], n)]:
                        heapq.heappush(h, (W + w, next(counter), way + [n], wway + [w]))
        yield from self._findPath(start, end, h, counter)

    def findPath(self, start, end):
        counter = count()  # counter is used to sort stability (tuple comparison)
        h = [(0, next(counter), [start], [])]
        yield from self._findPath(start, end, h, counter)

    def getCircuit(self):
        return list(self.findCircuit())[:-1]

