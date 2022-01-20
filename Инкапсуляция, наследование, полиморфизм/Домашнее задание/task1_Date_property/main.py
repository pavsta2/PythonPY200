class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            if not year % 100 == 0:
                result = True
            else:
                if year // 100 % 4 == 0:
                    result = True
                else:
                    result = False
        else:
            result = False
        return result

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        max_days = cls.DAY_OF_MONTH[cls.is_leap_year(year)][month - 1]
        return max_days

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError
        if day <= 0 or month <= 0 or year <= 0:
            raise ValueError("Не может быть нулем и отрицат")
        elif month > 12:
            raise ValueError("Месяцев в году 12")
        elif day > cls.get_max_day(month, year):
            raise ValueError("В этом месяце нет столько дней по календярю")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("День должен быть целочисленным")
        if not 0 < day <= 31:
            raise ValueError("День д.б. больше 0 и не больше 31")
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Мес должен быть целочисленным")
        if not 1 <= month <= 12:
            raise ValueError("Мес д.б. больше 1 и не больше 12")
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Год должен быть целочисленным")
        if not 0 < year:
            raise ValueError("Год д.б. больше 0")
        self._year = year


if __name__ == "__main__":
    a = Date(12,12,1981)
    print(a)
    a.month = 13

