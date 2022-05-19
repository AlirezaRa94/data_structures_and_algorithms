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

    def base_test_shortest_path(self):
        nodes = ["A", "B", "C", "D", "E"]
        self.add_nodes(nodes)
        self.graph.add_edge("A", "B", 3)
        self.graph.add_edge("A", "C", 4)
        self.graph.add_edge("A", "D", 2)
        self.graph.add_edge("B", "D", 6)
        self.graph.add_edge("C", "D", 1)
        self.graph.add_edge("B", "E", 1)
        self.graph.add_edge("D", "E", 5)

    def test_find_shortest_path(self):
        self.base_test_shortest_path()
        self.assertEqual("ADC", self.graph.find_shortest_path("A", "C"))
        self.assertEqual("CDAB", self.graph.find_shortest_path("C", "B"))

    def test_find_shortest_path_using_priority_queue(self):
        self.base_test_shortest_path()
        self.assertEqual(
            "ADC",
            self.graph.find_shortest_path_using_priority_queue("A", "C")
        )
        self.assertEqual(
            "CDAB",
            self.graph.find_shortest_path_using_priority_queue("C", "B")
        )

    def test_has_not_cycle(self):
        nodes = ["A", "B", "C"]
        self.add_nodes(nodes)
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("B", "C", 1)
        self.assertFalse(self.graph.has_cycle())

    def test_has_cycle(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("B", "C", 1)
        self.graph.add_edge("C", "D", 1)
        self.graph.add_edge("C", "A", 1)
        self.assertTrue(self.graph.has_cycle())

    def test_find_minimum_spanning_tree(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge("A", "B", 3)
        self.graph.add_edge("B", "D", 4)
        self.graph.add_edge("C", "D", 5)
        self.graph.add_edge("A", "C", 1)
        self.graph.add_edge("B", "C", 2)
        tree = self.graph.find_minimum_spanning_tree()
        tree.print_graph()

    def test_find_minimum_spanning_tree_not_connected(self):
        nodes = ["A", "B", "C", "D"]
        self.add_nodes(nodes)
        self.graph.add_edge("A", "B", 3)
        self.graph.add_edge("A", "C", 1)
        self.graph.add_edge("B", "C", 2)
        self.assertIsNone(self.graph.find_minimum_spanning_tree())

    def test_find_minimum_spanning_tree_no_nodes(self):
        self.assertIsNone(self.graph.find_minimum_spanning_tree())
