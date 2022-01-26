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

    def step_by_step_on_nodes(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        """"""
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        return self.step_by_step_on_nodes(index).value

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif 0 < index < (self.len - 1):
            node_new_left = self.step_by_step_on_nodes(index - 1)
            node_new_right = self.step_by_step_on_nodes(index + 1)
            node_new_left.next = node_new_right
        else:
            node_new_last = self.step_by_step_on_nodes(index - 1)
            node_new_last.next = None

        self.len -= 1

    def __setitem__(self, index, value):
        set_node = self.step_by_step_on_nodes(index)
        set_node.value = value

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index:
            raise IndexError()

        inserted_node = Node(value)
        if index > (self.len - 1) or self.head is None:
            self.append(value)
        elif index == 0:
            self.link_nodes(inserted_node, self.step_by_step_on_nodes(0))
            self.head = inserted_node
            self.len += 1
        else:
            inserted_node.next = self.step_by_step_on_nodes(index)
            self.step_by_step_on_nodes(index - 1).next = inserted_node
            self.len += 1

    def __str__(self):
        return f"{[linked_list_value for linked_list_value in self]}"


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    b = LinkedList(a)

    b.insert(7,100)
    print(b)
