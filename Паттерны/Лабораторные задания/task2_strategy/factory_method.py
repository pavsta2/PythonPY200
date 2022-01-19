from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver, JsonFileDriver


class DriverFactoryMethod(ABC):
    @classmethod
    @abstractmethod
    def get_driver(cls) -> IStructureDriver:
        ...


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.txt)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


class JsonFileDriverFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        json_filename = input('Введите название json файла: (.json)').strip()
        json_filename = json_filename or cls.DEFAULT_NAME
        if not json_filename.endswith('.json'):
            json_filename = f'{json_filename}.json'

        return JsonFileDriver(json_filename)


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()
    print(driver)
