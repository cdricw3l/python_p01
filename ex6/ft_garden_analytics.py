class Plant:
    _name: str
    _height: float
    _age: int
    _analytic: dict = {str: int}

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._analytic = {"grow": 0, "age": 0, "show": 0, "shade": 0}

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

    def age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__set_age(new_age)

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
    # La methode older than est static car
    # elle ne depend d'aucune cvariable de la classe

    @staticmethod
    def older_than_one(days: int) -> bool:
        return days > 365

    # la methode ci dessous est une class methode .
    # Il est possible d'apeller cette methode
    # directement par Plant.class_test()

    @classmethod
    def anonymous(cls):
        return cls("Unknown plan", 0, 0)


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

    def show(self):
        self._seed = self._blooming_status * 42
        super().show()
        print(f"seeds: {self._seed}")


class Tree(Plant):
    _trunk_diameter: float
    _shade: int

    def __init__(
            self, name: str, height: float, age: int, diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter
        self._shade = 0

    def show(self):
        super().show([f"Trunk diameter: {round(self._trunk_diameter)}cm"])

    def produce_shade(self, long: float, wide: float):
        print(
            f"Tree Oak now produces a shade of {round(long, 2)}cm long",
            f"and {round(wide, 2)}cm wide."
        )
        self._analytic['shade'] += 1


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

    grow: int = plant._analytic['grow']
    age: int = plant._analytic['age']
    show: int = plant._analytic['show']
    print(f"Stats: {grow} grow, {age} age, {show} show")
    if plant.__class__.__name__ == 'Tree':
        print(f"{plant._analytic['shade']} shade")


if __name__ == "__main__":

    print("=== Garden Security System ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", Plant.older_than_one(30))
    print("Is 400 days more than a year? -> ", Plant.older_than_one(400))
    print(end="\n")

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    display_stat(flower)
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.grow(8)
    flower.show()
    print(f"[statistics for {flower.get_name()}]")
    display_stat(flower)
    print(end="\n")

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5)
    tree.show()
    print(f"[statistics for {tree.get_name()}]")
    display_stat(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade(200.0, 5)
    print(f"[statistics for {tree.get_name()}]")
    display_stat(tree)
    print(end="\n")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.bloom()
    sunflower.age(20)
    sunflower.show()
    display_stat(sunflower)
    print(end="\n")

    print("=== Anonymous")
    anonyme_plant = Plant.anonymous()
    anonyme_plant.show(None)
    print(f"[statistics for {anonyme_plant.get_name()}]")
    display_stat(anonyme_plant)
