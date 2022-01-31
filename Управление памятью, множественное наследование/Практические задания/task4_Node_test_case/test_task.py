import unittest

from task import Node


class TestCase(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)

        self.assertIsNone(node.next)
        #  self.assertIs(None, node.next) - можно так
        self.assertEqual(5, node.value)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right node")
        left_node = Node("left node", next_= right_node)  # проверить что узлы связались

        self.asserIs(right_node, left_node.next)
        self.assertEqual("left node", left_node.value)

        self.assertIsNone(right_node.next)
        self.assertEqual("right node", right_node.value)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
          # проверить метод __repr__ без следующего узла
        node = Node(5)
        expected_repr = "Node(5, None)"
        self.assertEqual(expected_repr, repr(node))

      # пропустить тест с помощью декоратора unittest.skip
    @unittest.skip("будет дорабатываться")
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))

        expected_repr = "Node(5, Node(10))"
        self.assertEqual(expected_repr, repr(node))

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        # проверить строковое представление
        self.assertEqual(str(some_value), str(node))

    def test_is_valid(self):
        # проверить метод is_valid при корректных узлах
        Node.is_valid(Node("test"))
        Node.is_valid(None)


        #  с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
        with self.assertRaises(TypeError):
            Node.is_valid(5)
