from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Метод для инициализации узла односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self._next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError("Присоединяемый узел д.б. объектом класса Node")

    @property
    def next(self):
        print("Вызван getter")
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        print("Вызван setter")
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value, next_= None, prev = None):
        """
        Наследуем от базового класса все атрибуты и добавляем новый - prev
        """
        super().__init__(value, next_)
        self._prev = prev

    def __repr__(self) -> str:
        next_ = str(None) if self.next is None else f"{self.__class__.__name__}({self.next.value})"
        prev = str(None) if self.prev is None else f"{self.__class__.__name__}({self.prev.value})"
        return f"{self.__class__.__name__}({self.value}, {next_}, {prev})"

    @property
    def prev(self):
        print("Вызван getter")
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        print("Вызван setter")
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    Node1 = DoubleLinkedNode(1)
    Node2 = DoubleLinkedNode(2)
    Node3 = DoubleLinkedNode(3)

    Node4 = Node(2)

    print(repr(Node2))
    print(repr(Node4))

    Node1.next = Node2
    Node2.next = Node3
    Node2.prev = Node1
    Node3.prev = Node2

    a = [Node1, Node2, Node3]

    for _ in a:
        print(_)

    print(a)
    print(Node2.next)
