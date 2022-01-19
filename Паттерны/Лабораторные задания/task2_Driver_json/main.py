import json
from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


# Реализовать класс JsonFileDriver

class JsonFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            input_ = json.load(f)
        if not isinstance(input_, list):
            raise TypeError
        return input_

    def write(self, data: Iterable) -> None:
        data = [value for value in data]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


if __name__ == "__main__":
    write_data = [1, 2, 3]
    driver = JsonFileDriver('output.json')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
