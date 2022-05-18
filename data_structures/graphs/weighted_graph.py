"""
Implementing Undirected Weighted Graph using Adjacency List
"""
from typing import Dict, Set


class WeightedGraph:
    class Edge:
        def __init__(self, v1, v2, weight):
            self.v1 = v1
            self.v2 = v2
            self.weight = weight

        def __str__(self):
            return self.v1 + "->" + self.v2

    def __init__(self):
        self.adjacency_list: Dict[str, Set] = dict()

    def __contains__(self, item):
        return item in self.adjacency_list

    def _check_and_error_node_exists(self, label: str):
        if label in self:
            raise ValueError(f"{label} already exists in the graph!")

    def _check_and_error_node_not_exists(self, label: str):
        if label not in self:
            raise ValueError(f"{label} doesn't exists in the graph!")

    def get_edges(self, label: str):
        self._check_and_error_node_not_exists(label)
        return self.adjacency_list[label]

    def add_node(self, label: str):
        self._check_and_error_node_exists(label)
        self.adjacency_list[label] = set()

    def _remove_edge_of_node(self, v1: str, v2: str):
        for edge in self.adjacency_list[v1]:
            if edge.v2 == v2:
                self.adjacency_list[v1].remove(edge)
                break

    def remove_node(self, label: str):
        if label not in self.adjacency_list:
            return
        for edge in self.adjacency_list[label]:
            self._remove_edge_of_node(edge.v2, label)
        del self.adjacency_list[label]

    def add_edge(self, v1: str, v2: str, weight):
        self._check_and_error_node_not_exists(v1)
        self._check_and_error_node_not_exists(v2)
        self.adjacency_list[v1].add(self.Edge(v1, v2, weight))
        self.adjacency_list[v2].add(self.Edge(v2, v1, weight))

    def remove_edge(self, v1: str, v2: str):
        if v1 not in self.adjacency_list or v2 not in self.adjacency_list:
            return
        self._remove_edge_of_node(v1, v2)
        self._remove_edge_of_node(v2, v1)

    def print_graph(self):
        for node in self.adjacency_list:
            print(f"The edges of {node} are: {self.get_edges(node)}")
