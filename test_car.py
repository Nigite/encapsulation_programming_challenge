from classes.car_class import Car

def test_car():
    my_car = Car(2026, "Toyota")
    print(f"Car: {my_car._Car__year_model} {my_car._Car__make}")

    print("\nAccelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Current Speed: {my_car.get_speed()}")

    print("\nBraking...")
    for i in range(5):
        my_car.brake()
        print(f"Current Speed: {my_car.get_speed()}")

if __name__ == "__main__":
    test_car()