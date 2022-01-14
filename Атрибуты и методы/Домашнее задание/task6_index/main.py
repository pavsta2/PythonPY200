from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for current_node = self.head
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.__next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.__next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index:
            raise IndexError()  # проверка индекса

        inserted_node = Node(value)
        if index > (self.len - 1) or self.head is None:
            self.append(value)
        elif index == 0:
            self.linked_nodes(inserted_node, self.step_by_step_on_nodes(0))
            self.head = inserted_node
            self.len += 1
        else:
            inserted_node.next = self.step_by_step_on_nodes(index)
            self.step_by_step_on_nodes(index - 1).next = inserted_node
            self.len += 1

    def index(self, value: Any, start: Optional[int] = None, stop: Optional[int] = None) -> int:
        """Метод возвращает индекс указанного значения.
        Можно задавать диапазон поиска в виде начального и конечного индексов"""
        if not isinstance(start, int) or not isinstance(stop, (int, type(None))):
            raise TypeError

        if start is not None and not 0 <= start < (self.len - 1):
            raise ValueError("значение индекса выходит за диапазон списка")

        if stop is not None and not 0 <= stop < (self.len - 1):
            raise ValueError("значение индекса выходит за диапазон списка")

        if stop is not None and start is not None and stop <= start:
            raise ValueError("начало диапазона поиска не должно ровнятся или превышать его конец")

        current_node = self.head
        index = 0
        if start is None and stop is None:
            while current_node.value != value:
                current_node = current_node.next
                index += 1
                if current_node is None:
                    raise ValueError("значение не найдено")
        elif start is not None and stop is None:
            current_node = self.step_by_step_on_nodes(start)
            index = start
            while current_node.value != value:
                current_node = current_node.next
                index += 1
                if current_node is None:
                    raise ValueError("значение не найдено")
        elif start is not None and stop is not None:
            current_node = self.step_by_step_on_nodes(start)
            index = start
            while current_node.value != value:
                current_node = current_node.next
                index += 1
                if current_node is None:
                    raise ValueError("значение не найдено")
                if current_node == self.step_by_step_on_nodes(stop):
                    if current_node != value:
                        raise ValueError("значение не найдено")
                    break
        return index


if __name__ == "__main__":
    list_ = [1, "f", 3, 1, 2, "f", 1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    print(linked_list.index("f", 4))
