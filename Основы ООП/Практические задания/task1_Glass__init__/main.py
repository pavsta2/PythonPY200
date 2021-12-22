from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("сообщение об ошибке")
        if capacity_volume <= 0:
            raise ValueError("сщщбщение об ошибке 2")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume



if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass(250, 50)
    glass_3 = Glass(50, 50)

    print(glass_1, glass_2, glass_3, sep="\n")
     инициализировать не корректные объекты
