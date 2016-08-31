
# node id is a dict key: it musts be hashable (__eq__ and __hash__ should be define)

class graph:

    def __init__(self):
        self.nodes = dict()

    def __contains__(self, n):
        return n in self.nodes

    def _getNode(self, nodeId):
        ''' return node with nodeId (initialize new node if nodeId does not exist)'''
        if nodeId not in self.nodes:
            self.nodes[nodeId] = {'neigh' : set(),
                                  'pos' : None}
        return self.nodes[nodeId]

    def addNode(self, nodeId, position=None, neighbour=set()):
        node = self._getNode(nodeId)
        if node['pos'] and node['pos'] != position:
            raise Exception('node {} already defined, position conflict'.format(nodeId))
        node['pos'] = position
        for n in neighbour: self.addEdge(nodeId, n)

    def addEdge(self, nId1, nId2):
        n1, n2 = self._getNode(nId1), self._getNode(nId2)
        n1['neigh'].update((nId2,))
        n2['neigh'].update((nId1,))

