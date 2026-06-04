class Fan:
    # Constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        """Constructor with default values."""
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = on

    # Accessors (Getters)
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on

    # Mutators (Setters)
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

def test_fan():
    # First Fan object
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10)
    fan1.set_color("yellow")
    fan1.set_on(True)

    # Second Fan object
    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5)
    fan2.set_color("blue")
    fan2.set_on(False)

    # Display properties
    print("--- Fan 1 Properties ---")
    print(f"Speed: {fan1.get_speed()}")
    print(f"Radius: {fan1.get_radius()}")
    print(f"Color: {fan1.get_color()}")
    print(f"Is On: {fan1.get_on()}\n")

    print("--- Fan 2 Properties ---")
    print(f"Speed: {fan2.get_speed()}")
    print(f"Radius: {fan2.get_radius()}")
    print(f"Color: {fan2.get_color()}")
    print(f"Is On: {fan2.get_on()}")

if __name__ == "__main__":
    test_fan()