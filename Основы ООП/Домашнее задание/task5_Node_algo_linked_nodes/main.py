from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return f"{self.value}" #метод должен возвращать значение текущего узла

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
    """
    Функция, которая связывает между собой два узла.

    :param left_node: Левый или предыдущий узел
    :param right_node: Правый или следующий узел
    """
    left_node.set_next(right_node)

def nodes_connect(list_nodes: list) -> list:
    prev_node = list_nodes[0]
    for node in list_nodes[1:]:
        prev_node.next = node
        prev_node = node
    return list_nodes

if __name__ == "__main__":
    list_nodes = [Node(value) for value in range(5)]
    print(list_nodes)

    #реализуйте алгоритм, который свяжет между собой узлы в списке

    nodes_connect(list_nodes)

    print(list_nodes)
