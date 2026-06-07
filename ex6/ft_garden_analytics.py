class Plant:
    _name: str
    _height: float
    _age: int
    _analytic: dict;{str:int}

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._analytic =  {"grow": 0, "age": 0, "show": 0}

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def __set_height(self, grow: float) -> None:
            self._height += grow
            self._analytic["grow"] += 1

    def __set_age(self, age: int) -> None:
            self._age += age
            self._analytic["age"] += 1
            
    
    def grow(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__set_height(height)
            print(f"Height updated: {self.get_height()}cm")


    def age(self, new_age:int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__set_age(new_age)
            print(f"Age updated: {self.get_age()} days")

    def show(self, custom_msg: list[str]) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._age} days old"
        )
        if custom_msg:
            for msg in custom_msg:
                print(msg)
        self._analytic["show"] += 1

    @staticmethod
    def older_than_one(age: int) -> bool:
        return age > 1

    @classmethod
    def class_test(cls):
        return Plant("Unknown", 0, 0)

class Flower(Plant):
    _color: str
    _blooming_status: int

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming_status = 0

    def show(self):
        if self._blooming_status == 0:
            super().show([
                f"Color: {self._color}",
                f"{self._name} has not bloomed yet"
            ])
        else:
            super().show([
                f"Color: {self._color}",
                f"{self.get_name()} is blooming beautifully!"
            ])

    def bloom(self) -> None:
        self._blooming_status = 1

class Seed(Flower):
    _seed: int
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed = 0

    def bloom(self) -> None:
        super().bloom()
        

class Tree(Plant):
    _trunk_diameter: float

    def __init__(
            self, name: str, height: float, age: int, diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter

    def show(self):
        super().show([f"Trunk diameter: {round(self._trunk_diameter)}cm"])

    def produce_shade(self, long: float, wide: float):
        print(
            f"Tree Oak now produces a shade of {round(long, 2)}cm long",
            f"and {round(wide, 2)}cm wide."
        )


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
            self, name: str, height: float, age: int,
            harvest_season: str, nutritional_value: int
            ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show([
            f"Harvest season: {self._harvest_season}",
            f"Nutritional value: {self._nutritional_value}"
        ])

    def set_nutritional_value(self, value: int) -> None:
        self._nutritional_value += value

    def grow(self, height: float, age: int) -> None:
        super().grow(height)
        super().age(age)
        self.set_nutritional_value(self.get_age() - 10)

def display_stat(plant: Plant):
    grow: int = plant._analytic["grow"]
    age: int = plant._analytic["age"]
    show: int = plant._analytic["show"]
    print(f"Stats: {grow} grow, {age} age, {show} show")

# if __name__ == "__main__":

#     print("=== Garden Security System ===")
#     print("=== Flower")
#     flower = Flower("rose", 15.0, 13, "red")
#     flower.show()
#     print("[asking the rose to bloom]")
#     flower.bloom()
#     flower.show()
#     print(end="\n")
#     print("=== Tree")
#     tree = Tree("Oak", 200.0, 365, 5)
#     tree.show()
#     print("[asking the oak to produce shade]")
#     tree.produce_shade(200, 5)
#     print(end="\n")
#     print("=== Vegetable")
#     vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
#     vegetable.show()
#     print("[make tomato grow and age for 20 days]")
#     vegetable.grow(42, 20)
#     vegetable.show()
