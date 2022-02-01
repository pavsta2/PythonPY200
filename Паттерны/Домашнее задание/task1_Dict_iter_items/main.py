from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):  # Наследование от класса dict

    def __iter__(self) -> Iterator:
        # for pair in zip(self.keys(), self.values()):
        #     yield pair
        return zip(self.keys(), self.values())


if __name__ == "__main__":
    my_dict = MyDict({
        1: "a",
        2: "b",
        3: "c"
    })
    for keys, values in my_dict:
        print(keys, values)
    # print(len(my_dict))
