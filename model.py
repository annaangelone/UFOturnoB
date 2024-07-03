import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._states = DAO.getStates()
        self._idMap = {}

        for s in self._states:
            self._idMap[s.id] = s


    def buildGraph(self, anno, giorni):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._states)

        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u!=v:
                    peso = DAO.getPeso(u.id, v.id, anno, giorni)

                    if (DAO.getEdges(u.id, v.id)):

                        self._grafo.add_edge(u, v, weight=0)

                        if peso:
                            self._grafo[u][v]["weight"] = peso[0]



    def stampaPesiVicini(self):
        vicini = []

        for n in self._grafo.nodes:
            peso = 0
            for v in self._grafo.neighbors(n):
                peso += self.getPeso(n, v)

            vicini.append((n, peso))

        return vicini



    def getPeso(self, n1, n2):
        return self._grafo[n1][n2]["weight"]

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
