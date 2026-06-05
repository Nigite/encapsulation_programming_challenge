from classes.pet_class import Pet

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