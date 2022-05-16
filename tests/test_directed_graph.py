from unittest import TestCase

from data_structures.graphs.directed_graph import DirectedGraph


class TestDirectedGraph(TestCase):
    def setUp(self) -> None:
        self.graph = DirectedGraph()

    def add_nodes(self, nodes: list):
        for node in nodes:
            self.graph.add_node(node)

    def test_add_node_already_exists(self):
        node = "A"
        self.graph.add_node(node)
        with self.assertRaises(ValueError) as context:
            self.graph.add_node(node)
            self.assertTrue(
                f"{node} already exists in the graph!" in context.exception
            )

    def test_add_node(self):
        node = "A"
        self.graph.add_node(node)
        self.assertIn(node, self.graph.adjacency_list)
        self.assertSetEqual(self.graph.adjacency_list[node], set())

    def test_remove_node_not_exists(self):
        node = "A"
        self.assertIsNone(self.graph.remove_node(node))

    def test_remove_node(self):
        nodes = ["A", "B"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.remove_node(nodes[1])
        self.assertIn(nodes[0], self.graph)
        self.assertNotIn(nodes[1], self.graph)
        self.assertNotIn(nodes[1], self.graph.get_neighbors(nodes[0]))

    def test_add_edge(self):
        nodes = ["A", "B"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.assertIn(nodes[1], self.graph.get_neighbors(nodes[0]))
        self.assertNotIn(nodes[0], self.graph.get_neighbors(nodes[1]))

    def test_add_edge_node_not_exists(self):
        nodes = ["A", "B"]
        self.graph.add_node(nodes[0])
        with self.assertRaises(ValueError) as error:
            self.graph.add_edge(nodes[0], nodes[1])
            self.assertTrue(
                f"{nodes[1]} doesn't exists in the graph!" in error.exception
            )
            self.assertNotIn(
                nodes[1],
                self.graph.get_neighbors(nodes[0]),
            )

    def test_remove_edge(self):
        nodes = ["A", "B"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.add_edge(nodes[1], nodes[0])
        self.graph.remove_edge(nodes[0], nodes[1])
        self.assertNotIn(nodes[1], self.graph.get_neighbors(nodes[0]))
        self.assertIn(nodes[0], self.graph.get_neighbors(nodes[1]))

    def base_test_traversal(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.add_edge(nodes[0], nodes[2])
        self.graph.add_edge(nodes[1], nodes[3])
        self.graph.add_edge(nodes[3], nodes[2])

    def test_depth_first_traversal(self):
        self.base_test_traversal()
        self.graph.depth_first_traversal("A")

    def test_depth_first_traversal_iterative(self):
        self.base_test_traversal()
        self.graph.depth_first_traversal_iterative("C")

    def test_breadth_first_traversal(self):
        self.base_test_traversal()
        self.graph.breadth_first_traversal("A")

    def test_topological_sorting(self):
        nodes = ["X", "A", "B", "P"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.add_edge(nodes[0], nodes[2])
        self.graph.add_edge(nodes[1], nodes[3])
        self.graph.add_edge(nodes[2], nodes[3])
        sorted_graph = self.graph.topological_sorting()
        self.assertEqual(set(sorted_graph), set(nodes))
        self.assertTrue(nodes[0] == sorted_graph[0])
        self.assertTrue(nodes[-1 == sorted_graph[-1]])

    def test_has_cycle(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.add_edge(nodes[1], nodes[2])
        self.graph.add_edge(nodes[2], nodes[0])
        self.graph.add_edge(nodes[3], nodes[0])
        self.assertTrue(self.graph.has_cycle())

    def test_has_not_cycle(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1])
        self.graph.add_edge(nodes[1], nodes[2])
        self.graph.add_edge(nodes[0], nodes[2])
        self.graph.add_edge(nodes[3], nodes[0])
        self.assertFalse(self.graph.has_cycle())
