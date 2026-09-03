class Siec:
    class Edge:
        def __init__(self, t, capacity) -> None:
            self.t = t
            self.capacity = capacity
            self.flow = 0

        @property
        def flow(self):
            return self.flow

        @flow.setter
        def flow(self, flow):
            if flow < 0:
                raise ValueError("Flow cannot be less than 0")
            if flow > self.capacity:
                raise ValueError("Flow cannot be greater than capacity")
            self.flow = flow

    def __init__(self) -> None:
        self.edges = dict()
        self.source = "s"

    def addEdge(self, f, to, capacity):
        if self.edges[f] is None:
            self.edges[f] = list()
        self.edges[f].append(Siec.Edge(to, capacity))

class SiecResidualna:
    def __init__(self, siec:Siec):
        self.edges = dict()
        for f, edge in siec.edges.items():
            if self.edges[f] is None:
                self.edges[f] = list()
            if self.edges[edge.t] is None:
                    self.edges[edge.t] = list()

            if edge.capacity - edge.flow != 0:
                self.edges[f].append((edge.t, edge.capacity - edge.flow))
            if edge.flow != 0:
                self.edges[edge.t].append((f, edge.flow))

    def sciezkaResidualna(self):

    def min

