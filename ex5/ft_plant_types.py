class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self._name}:", end=" ")
        print(f"{round(self._height, 2)}cm, {self._age} days old")

    def get_height(self: "Plant") -> float:
        return self._height

    def get_age(self: "Plant") -> int:
        return self._age
    
    def get_name(self: "Plant") -> str:
        return self._name

    def set_height(self: "Plant", grow: float) -> None:
        if grow < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height += grow
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self: "Plant", age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age += age
            print(f"Age updated: {self.get_age()} days")
    
    def show(self: "Plant") -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

class Flower(Plant):
    _color: str
    _blooming_status: int
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming_status = 0

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._blooming_status == 0:
                print(f"{self._name} has not bloomed yet")
        else :
            print(f"{self.get_name()} is blooming beautifully!")

    def bloom(self) -> None:
        self._blooming_status = 1
        #self.show()

class Tree(Plant):
    _trunk_diameter: float
    def __init__(self, name: str, height: float, age: int,  trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
    
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter)}cm")
    
    def produce_shade(self, long: float, wide: float):
        print(f"Tree Oak now produces a shade of {round(long, 2)}cm long and {round(wide, 2)}cm wide.")

class Vegetable:
    _harvest_season: str
    _nutritional_value: int
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
    
    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    flower = Flower("rose", 10.5, 13, "red")
    tree= Tree("Oak", 200, 365, 5)
    print(end="\n")
    flower.show()
    print(end="\n")
    flower.bloom()
    flower.show()
    print(end="\n")
    tree.show()
    print(end="\n")
    tree.produce_shade(200, 5)
    print(end="\n")