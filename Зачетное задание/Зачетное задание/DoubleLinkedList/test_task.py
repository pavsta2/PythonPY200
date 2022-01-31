import unittest

from task import DoubleLinkedList


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
