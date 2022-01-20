
class Parent:
    atr_cls1 = 1
    _atr_cls2 = 2
    __atr_cls3 = 3

    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.__atr3 = atr3
        self._atr2 = atr2

    @classmethod
    def meth(cls):
        print(cls.atr_cls1)

    @classmethod
    def _meth2(cls):
        print(cls.atr_cls1)

    @classmethod
    def __meth3(cls):
        print(cls.atr_cls1)


if __name__ == "__main__":
    # Write your solution here
    pass
