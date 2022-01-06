class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            if not year % 100 == 0:
                result = 1
            else:
                if year // 100 % 4 == 0:
                    result = 1
                else:
                    result = 0
        else:
            result = 0
        return result

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        max_days = self.DAY_OF_MONTH[self.is_leap_year(year)][month - 1]
        return max_days

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if day <= 0 or month <= 0 or year <= 0:
            raise ValueError("Не может быть нулем и отрицат")
        elif month > 12:
            raise ValueError("Месяцев в году 12")

        elif day > self.get_max_day(month, year):
            raise ValueError("В этом месяце нет столько дней по календярю")


if __name__ == "__main__":
    # Write your solution here
    date1 = Date("j",13, 1981)
