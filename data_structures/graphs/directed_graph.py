"""
Implementing Directed Graph Data Structure Using Adjacency List
"""
from typing import Dict, Set


class DirectedGraph:
    def __init__(self):
        self.adjacency_list: Dict[str, Set] = dict()

    def __contains__(self, item):
        return item in self.adjacency_list

    def _check_and_error_node_not_exists(self, label: str):
        if label not in self:
            raise ValueError(f"{label} doesn't exists in the graph!")

    def _check_and_error_node_exists(self, label: str):
        if label in self:
            raise ValueError(f"{label} already exists in the graph!")

    def add_node(self, label: str):
        self._check_and_error_node_exists(label)
        self.adjacency_list[label] = set()

    def remove_node(self, label: str):
        if label not in self:
            return
        del self.adjacency_list[label]
        for v, adj_list in self.adjacency_list.items():
            if label in adj_list:
                adj_list.remove(label)

    def get_connected_nodes(self, label: str):
        self._check_and_error_node_not_exists(label)
        return self.adjacency_list[label]

    def add_edge(self, v1: str, v2: str):
        self._check_and_error_node_not_exists(v1)
        self._check_and_error_node_not_exists(v2)
        neighbors = self.adjacency_list[v1]
        if v2 not in neighbors:
            self.adjacency_list[v1].add(v2)

    def remove_edge(self, v1: str, v2: str):
        if v1 not in self or v2 not in self:
            return
        neighbors = self.adjacency_list[v1]
        if v2 in neighbors:
            self.adjacency_list[v1].remove(v2)

    def print_graph(self):
        for node in self.adjacency_list:
            print(f"{node} is connected with: {self.adjacency_list[node]}")
