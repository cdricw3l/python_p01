class Plant:
    Name: str
    Height: float
    Age: int

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self.Name = name
        self.Height = height
        self.Age = age

    def show(self: "Plant") -> None:
        print(f"{self.Name}: {round(self.Height, 1)}cm, {self.Age} days old")

    def grow(self: "Plant", grow: float) -> None:
        self.Height += grow

    def age(self: "Plant", age: int) -> None:
        self.Age += age

# le f = placeholders


def created_msg() -> None:
    print("Created:", end=" ")


if __name__ == "__main__":
    list_plants: list[Plant] = [
        Plant("Rose", 25.0, 30), Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 365), Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for plant in list_plants:
        created_msg()
        plant.show()
