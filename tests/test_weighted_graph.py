from unittest import TestCase

from data_structures.graphs.weighted_graph import WeightedGraph


class TestWeightedGraph(TestCase):
    def setUp(self) -> None:
        self.graph = WeightedGraph()

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
        self.graph.add_edge(nodes[0], nodes[1], 1)
        self.graph.remove_node(nodes[1])
        self.assertIn(nodes[0], self.graph)
        self.assertNotIn(nodes[1], self.graph)
        self.assertNotIn(
            f"{nodes[0]}->{nodes[1]}",
            self.graph.get_edges(nodes[0])
        )

    def test_add_edge(self):
        nodes = ["A", "B", "C"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1], 2)
        self.graph.add_edge(nodes[0], nodes[2], 3)
        self.assertEqual(
            {str(WeightedGraph.Edge(nodes[0], nodes[1], 2)),
             str(WeightedGraph.Edge(nodes[0], nodes[2], 3))},
            {str(edge) for edge in self.graph.get_edges(nodes[0])}
        )
        self.assertEqual(
            {str(WeightedGraph.Edge(nodes[1], nodes[0], 2))},
            {str(edge) for edge in self.graph.get_edges(nodes[1])}
        )
        self.assertEqual(
            {str(WeightedGraph.Edge(nodes[2], nodes[0], 3))},
            {str(edge) for edge in self.graph.get_edges(nodes[2])}
        )

    def test_add_edge_node_not_exists(self):
        nodes = ["A", "B"]
        self.graph.add_node(nodes[0])
        with self.assertRaises(ValueError) as error:
            self.graph.add_edge(nodes[0], nodes[1], 2)
            self.assertTrue(
                f"{nodes[1]} doesn't exists in the graph!" in error.exception
            )
            self.assertNotIn(
                str(WeightedGraph.Edge(nodes[0], nodes[1], 2)),
                {str(edge) for edge in self.graph.get_edges(nodes[0])},
            )

    def test_remove_edge(self):
        nodes = ["A", "B", "C"]
        self.add_nodes(nodes)
        self.graph.add_edge(nodes[0], nodes[1], 1)
        self.graph.add_edge(nodes[0], nodes[2], 1)
        self.graph.remove_edge(nodes[0], nodes[1])
        self.assertNotIn(
            "A->B",
            {str(edge) for edge in self.graph.get_edges(nodes[0])}
        )
        self.assertNotIn(
            "B->A",
            {str(edge) for edge in self.graph.get_edges(nodes[1])}
        )
        self.assertIn(
            "A->C",
            {str(edge) for edge in self.graph.get_edges(nodes[0])}
        )
        self.assertIn(
            "C->A",
            {str(edge) for edge in self.graph.get_edges(nodes[2])}
        )
