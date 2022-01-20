from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod, JsonFileDriverFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self._driver = driver

    #свойство для driver (getter + setter)

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver: IStructureDriver):
        if not isinstance(driver, IStructureDriver):
            raise TypeError
        self._driver = driver


    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self._driver.read()

        for value in data_from_driver:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self._driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    ll.driver = SimpleFileFactoryMethod.get_driver()  #инициализировать SimpleFileDriver
    ll.read()
    print(ll)

    ll.driver = JsonFileDriverFactoryMethod.get_driver()  #инициализировать JsonFileDriver
    ll.write()
