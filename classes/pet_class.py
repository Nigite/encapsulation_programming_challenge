class Pet:
    def __init__(self, name="", animal_type="", age=0):
        """Initialize the pet attributes."""
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def test_pet():
    my_pet = Pet()

    pet_name = input("Enter the name of your pet: ")
    pet_type = input("Enter the type of animal (e.g., Dog, Cat, Bird): ")
    pet_age = int(input("Enter the age of your pet: "))

    my_pet.set_name(pet_name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(pet_age)

    print("\n--- Pet Information ---")
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_animal_type()}")
    print(f"Age: {my_pet.get_age()}")

if __name__ == "__main__":
    test_pet()