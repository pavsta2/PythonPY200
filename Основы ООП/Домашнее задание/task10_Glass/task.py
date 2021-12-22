class Glass:
    def __init__(self, material: str = None):
        self.material = None
        self.set_material(material)

    def set_material(self, material):
        if not isinstance(material, (type(None), str)):
            raise TypeError("Материал передается только в строке")
        self.material = material

    def get_material(self):
        return self.material


# написать класс Glass согласно условию


if __name__ == "__main__":
    glass1 = Glass()
    glass1.set_material("plastic")
    print(glass1.material)
    print(glass1.get_material())
