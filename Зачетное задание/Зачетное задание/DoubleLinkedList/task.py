from typing import Any, Iterable, Optional, Iterator
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    NODE_CLASS = Node

    def __init__(self, data: Iterable = None):
        type_node = self.NODE_CLASS
        self.__len = 0
        self.__head: Optional[type_node] = None
        self.__tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    @property
    def len(self):
        return self.__len

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, value: NODE_CLASS):
        if not isinstance(value, self.NODE_CLASS):
            raise TypeError(f"Узел д.б. типа {self.__class__.__name__}")
        self.__tail = value

    @head.setter
    def head(self, value: NODE_CLASS):
        if not isinstance(value, self.NODE_CLASS):
            raise TypeError(f"Узел д.б. типа {self.__class__.__name__}")
        self.__head = value

    @len.setter
    def len(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Значение len д.б. только типа int")
        self.__len = value

    def append(self, value: Any) -> None:
        append_node = self.NODE_CLASS(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.link_nodes(self.tail, append_node)
            self.tail = append_node
        self.__len += 1

    @staticmethod
    def link_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """"""
        left_node.next = right_node

    def __len__(self):
        return self.__len

    def is_valid_index(self, index):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.__len:
            raise IndexError("выходит за пределы диапазона значений индекса")

    def step_by_step_on_nodes(self, index: int):
        self.is_valid_index(index)

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        """"""
        return self.step_by_step_on_nodes(index).value

    def __delitem__(self, index: int):  # todo test case
        self.is_valid_index(index)

        if index == 0:
            self.head = self.head.next
        elif 0 < index < (self.__len - 1):
            node_new_left = self.step_by_step_on_nodes(index - 1)
            node_new_right = self.step_by_step_on_nodes(index + 1)
            node_new_left.next = node_new_right
        else:
            node_new_last = self.step_by_step_on_nodes(index - 1)
            node_new_last.next = None

        self.__len -= 1

    def __setitem__(self, index: int, value: Any):
        set_node = self.step_by_step_on_nodes(index)
        set_node.value = value

    def insert(self, index: int, value: Any) -> None:
        self.is_valid_index(index)

        inserted_node = self.NODE_CLASS(value)
        if index > (self.__len - 1) or self.head is None:
            self.append(value)
        elif index == 0:
            self.link_nodes(inserted_node, self.step_by_step_on_nodes(0))
            self.head = inserted_node
            self.__len += 1
        else:
            inserted_node.next = self.step_by_step_on_nodes(index)
            self.step_by_step_on_nodes(index - 1).next = inserted_node
            self.__len += 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def nodes_iterator(self) -> Iterator[NODE_CLASS]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def __iter__(self) -> Iterator[Any]:
        print("вызван метод __iter__")
        for current_node in self.nodes_iterator():
            yield current_node.value

    def __contains__(self, item: Any) -> bool:
        result = False
        for node in self:
            if item == node:
                result = True
        # for _ in range(self.len):  # fixme for value in self: # todo
        #     if item == self.step_by_step_on_nodes(_).value:
        #         result = True
        return result

    def __reversed__(self) -> list:
        reversed_list = []
        for i in range(1, self.len + 1):
            reversed_list.append(self.step_by_step_on_nodes(self.len - i).value)
        return reversed_list

    def count(self, value: Any) -> int:
        count = 0
        for node in self:
            if value == node:
                count += 1
        # for _ in range(self.len):
        #     if value == self.step_by_step_on_nodes(_).value:
        #         count += 1
        return count

    def __str__(self):
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        # return f"{[self.NODE_CLASS.__repr__(node) for node in self]}"
        return f"{self.__class__.__name__}{self.to_list()}"  # todo for node in self.iterator_node


class DoubleLinkedList(LinkedList):
    NODE_CLASS = DoubleLinkedNode

    @staticmethod
    def link_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

    def __delitem__(self, index: int):
        self.is_valid_index(index)

        if index == 0:
            self.head = self.head.next
            self.head.prev = None

        elif 0 < index < (self.len - 1):
            node_new_left = self.step_by_step_on_nodes(index - 1)
            node_new_right = self.step_by_step_on_nodes(index + 1)
            self.link_nodes(node_new_left, node_new_right)
        else:
            node_new_last = self.step_by_step_on_nodes(index - 1)
            node_new_last.next = None

        self.len -= 1

    def insert(self, index: int, value: Any) -> None:

        inserted_node = self.NODE_CLASS(value)

        if self.head is None:
            self.append(value)
        elif index == 0:
            self.link_nodes(inserted_node, self.head)
            self.head = inserted_node
            self.len += 1
        else:
            self.is_valid_index(index)
            self.link_nodes(inserted_node, self.step_by_step_on_nodes(index))
            self.link_nodes(self.step_by_step_on_nodes(index - 1), inserted_node)
            self.len += 1

    def pop(self):
        last = self.step_by_step_on_nodes(self.len - 1).value
        self.__delitem__(self.len - 1)
        return last

    def extend(self, values: Iterable) -> None:
        if not isinstance(values, (list, dict, set, tuple)):  # как включить сюда итератор?
            raise TypeError(f"метод ожидает в кач аргумента итерируемую посл-ть, по факту:{type(values)}")
        for value in values:
            self.append(value)

    def remove(self, value: any) -> None:
        count = 0
        find = False
        for val in self:
            if val == value:
                self.__delitem__(count)
                find = True
            count += 1
        if not find:
            raise ValueError("элемент с таким значением не найден")

    def index(self, value: Any, start: int = 0, stop: int = 2147483647) -> int:
        if stop > (self.len - 1):
            stop = self.len
        find = False
        find_index = None
        for index in range(start, stop):
            val = self.step_by_step_on_nodes(index).value
            if val == value:
                find_index = index
                find = True
                break
        if not find:
            raise ValueError("элемент с таким значением не найден")
        return find_index


if __name__ == "__main__":
    # a = []
    b = DoubleLinkedList([])

    print(b.insert(800, 1))

    print(b)

    # todo coverage test insert, найти момент когда не работает setter head
    # вместе setter head сделать protected _head, rename in Dll, getter оставить
