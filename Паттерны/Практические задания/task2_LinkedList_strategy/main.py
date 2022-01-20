from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  # наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)  # расширяем конструктор, чтобы в связном списке был driver
        self.driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        read_data = self.driver.read()  # считать данные из драйвера
        for value in read_data:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)  # записать данные с помощью драйвера


if __name__ == '__main__':
    ll = LinkedListWithDriver()  # инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    # инициализировать драйвер и считать данные
    driver = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver
    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    # заменить драйвер и записать данные
    default_driver = SimpleFileFactoryMethod.get_driver()
    ll.driver = default_driver
    ll.write()
