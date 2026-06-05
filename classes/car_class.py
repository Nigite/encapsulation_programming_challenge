class Car:
    def __init__(self, year_model, make):
        """Initialize the car with year, make, and starting speed of 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Adds 5 to the speed data attribute."""
        self.__speed += 5

    def brake(self):
        """Subtracts 5 from the speed data attribute."""
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        """Returns the current speed."""
        return self.__speed

def test_car():
    my_car = Car(2026, "Toyota")

    print("Accelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Current Speed: {my_car.get_speed()}")

    print("\nBraking...")
    for i in range(5):
        my_car.brake()
        print(f"Current Speed: {my_car.get_speed()}")

if __name__ == "__main__":
    test_car()