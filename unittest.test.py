import unittest
from node import Node

from nodeFactory import NodeFactory


class TestNodeFactory(unittest.TestCase):
    def setUp(self):
        self.factory = NodeFactory()

    def test_create_node(self):
        node = self.factory.create_node("test", "test description")
        self.assertIsInstance(node, Node)
        self.assertEqual(node.name, "test")
        self.assertEqual(node.description, "test description")
        self.assertIsNone(node.parent)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])

    def test_create_node_with_parent(self):
        parent = self.factory.create_node("parent", "parent description")
        node = self.factory.create_node("child", "child description", "parent")
        self.assertIsInstance(node, Node)
        self.assertEqual(node.name, "child")
        self.assertEqual(node.description, "child description")
        self.assertEqual(node.parent, "parent")
        self.assertIsNone(node.value)
        self.assertEqual(parent.children, [node])

    def test_create_node_with_existing_name(self):
        node1 = self.factory.create_node("test", "test description")
        node2 = self.factory.create_node("test", "test description")
        self.assertIsNone(node2)
        self.assertEqual(len(self.factory.nodes), 1)

    def test_create_node_with_nonexistent_parent(self):
        node = self.factory.create_node("child", "child description", "parent")
        self.assertIsNone(node)
        self.assertEqual(len(self.factory.nodes), 0)

    def test_delete_node(self):
        node = self.factory.create_node("test", "test description")
        self.factory.delete_node("test")
        self.assertNotIn("test", self.factory.nodes)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.children, [])

    def test_delete_nonexistent_node(self):
        self.factory.delete_node("test")
        self.assertEqual(len(self.factory.nodes), 0)

    def test_get_nodes(self):
        node1 = self.factory.create_node("test1", "test1 description")
        node2 = self.factory.create_node("test2", "test2 description")
        nodes = self.factory.get_nodes()
        self.assertEqual(len(nodes), 2)
        self.assertIn(node1, nodes)
        self.assertIn(node2, nodes)

    def test_get_node_by_name(self):
        node = self.factory.create_node("test", "test description")
        self.assertEqual(self.factory.get_node_by_name("test"), node)

    def test_get_nonexistent_node_by_name(self):
        self.assertIsNone(self.factory.get_node_by_name("test"))


unittest.main()
