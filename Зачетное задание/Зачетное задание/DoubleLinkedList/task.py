from abc import ABC
from typing import Any, Iterable, Optional
from _collections_abc import MutableSequence

from node import Node


class LinkedList(MutableSequence, ABC):
    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any) -> None:
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.link_nodes(self.tail, append_node)
            self.tail = append_node
        self.len += 1

    @staticmethod
    def link_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """"""
        left_node.next = right_node

    def __len__(self):
        return self.len

    def __getitem__(self, index: int) -> Any:
        """"""
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value

    def __delitem__(self, key):
        ...

    def __setitem__(self, key, value):
        ...

    def insert(self, index: int, value) -> None:
        ...

    def __str__(self):
        return f"{[linked_list_value for linked_list_value in self]}"


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    b = LinkedList(a)

    print(b[0])
