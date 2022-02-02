import unittest

from task import DoubleLinkedList, LinkedList, Node


class TestCase(unittest.TestCase):
    def test_insert_in_empty(self):
        # проверка вставки элемента в пустой список, от значения индекса не зависит

        a = DoubleLinkedList([])
        a.insert(0, 1)
        self.assertEqual(str(a), str(DoubleLinkedList([1])))
        b = DoubleLinkedList([])
        b.insert(8, 1)
        self.assertEqual(str(b), str([1]))

    def test_insert_to_end(self):
        #  проверка вставки в конец списка - д.б. ошибка, т.к. вставка только левосторонняя
        a = DoubleLinkedList([1, 2, 3])

        with self.assertRaises(IndexError):
            a.insert(3, 100)

    def test_insert_into_middle(self):
        # проверка вставки в середину списка
        a = DoubleLinkedList([1, 2, 3])
        a.insert(1, 100)

        self.assertEqual(str(a), str([1, 100, 2, 3]))

        b = DoubleLinkedList([1, 2, 3])
        b.insert(2, 100)

        self.assertEqual(str(b), str([1, 2, 100, 3]))

    def test_remove_from_empty(self):
        #  проверка ремув из пустого списка - д.б. ошибка
        a = DoubleLinkedList([])
        with self.assertRaises(ValueError):
            a.remove(3)

        b = LinkedList([])
        with self.assertRaises(ValueError):
            b.remove(3)

    def test_remove_from_begining(self):
        #  проверка ремув первого элемента
        a = DoubleLinkedList([1, 2, 4])
        a.remove(1)
        self.assertEqual(str(a), str([2, 4]))
        self.assertEqual(str(a.head), "2")
        self.assertEqual(repr(a.head), "DoubleLinkedNode(2, DoubleLinkedNode(4), None)")

    def test_remove_from_middle(self):
        #  проверка ремув из середины
        a = DoubleLinkedList([1, 2, 4, 7])
        a.remove(2)
        self.assertEqual(str(a), str([1, 4, 7]))
        self.assertEqual(repr(a.head), "DoubleLinkedNode(1, DoubleLinkedNode(4), None)")
        #  как вызвать репр элемента из середины
        # ll_iter_nodes = a.nodes_iterator()
        # for _ in range(3):
        #     current_node = next(ll_iter_nodes)
        self.assertEqual(repr(a.head.next), "DoubleLinkedNode(4, DoubleLinkedNode(7), DoubleLinkedNode(1))")

    def test_remove_from_end(self):
        #  проверка ремув с конца
        a = DoubleLinkedList([1, 2, 4, 7])
        a.remove(7)
        self.assertEqual(str(a), str([1, 2, 4]))
        #  как вызвать репр элемента из середины
        self.assertEqual(repr(a.head.next.next), "DoubleLinkedNode(4, None, DoubleLinkedNode(2))")


# class LinkedListTest(unittest.TestCase):
#     def test_replace_head(self):
#         ll = LinkedList([1, 2, 3])
#         ll.head = Node(100)
#
#         self.assertEqual(2, ll.head.next)
#
#         # self.assertEqual(str([100, 2, 3]), str(ll))