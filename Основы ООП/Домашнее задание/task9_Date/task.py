# TODO class Date

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        if not isinstance(day, int):
            raise TypeError("день выражается только в двузначных цифрах")
        if not isinstance(month, int):
            raise TypeError("день выражается только в двузначных цифрах")
        if not isinstance(year, int):
            raise TypeError("день выражается только в четырехзначных цифрах")

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year}"

    def __str__(self):
        return f"{self.day}".rjust(2, '0') + '/' + f"{self.month}".rjust(2, '0') + '/' + f"{self.year}"


if __name__ == "__main__":
    date1 = Date(10, 2, 1999)
    print(date1)
