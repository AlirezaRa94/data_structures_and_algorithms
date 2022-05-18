"""
Implementing Undirected Weighted Graph using Adjacency List
"""
from collections import deque
from queue import PriorityQueue
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

    @staticmethod
    def _min_distance(distances: dict, not_visited: set):
        min_dist = float("inf")
        min_dist_node = None
        for node in not_visited:
            if distances[node] < min_dist:
                min_dist = distances[node]
                min_dist_node = node
        return min_dist_node

    @staticmethod
    def _build_path(node: str, previous: dict):
        stack = deque()
        curr = node
        while curr:
            stack.append(curr)
            curr = previous.get(curr)
        path = ""
        while len(stack) > 0:
            path += stack.pop()
        return path

    def find_shortest_path(self, source: str, to: str):
        self._check_and_error_node_not_exists(source)
        self._check_and_error_node_not_exists(to)
        not_visited = set(self.adjacency_list.keys())
        distances = {node: float("inf") for node in not_visited}
        distances[source] = 0
        previous = dict()
        for i in range(len(not_visited)):
            curr = self._min_distance(distances, not_visited)
            if curr is None:
                break
            not_visited.remove(curr)
            for edge in self.get_edges(curr):
                neighbor = edge.v2
                if neighbor in not_visited:
                    dist = edge.weight + distances[curr]
                    if dist < distances[neighbor]:
                        distances[neighbor] = dist
                        previous[neighbor] = curr
        return self._build_path(to, previous)

    def find_shortest_path_using_priority_queue(self, source: str, to: str):
        self._check_and_error_node_not_exists(source)
        self._check_and_error_node_not_exists(to)
        visited = set()
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[source] = 0
        previous = dict()
        priority_queue = PriorityQueue()
        priority_queue.put((distances[source], source))
        while not priority_queue.empty():
            curr = priority_queue.get()[1]
            visited.add(curr)
            for edge in self.adjacency_list[curr]:
                neighbor = edge.v2
                if neighbor not in visited:
                    dist = distances[curr] + edge.weight
                    if dist < distances[neighbor]:
                        distances[neighbor] = dist
                        previous[neighbor] = curr
                        priority_queue.put((dist, neighbor))
        return self._build_path(to, previous)
