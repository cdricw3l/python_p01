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


if __name__ == "__main__":
    plan = Plant("Rose", 25, 30)
    initial_heigth = plan.Height
    print("=== Garden Plant Growth ===")
    plan.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plan.age(1)
        plan.grow(0.8)
        plan.show()
    print(f"Growth this week: {round(plan.Height - initial_heigth, 2)}cm")
