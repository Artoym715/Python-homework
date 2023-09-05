from classes.Employee import Employee
from classes.Fish import Fish


class Factory:
    def create_animal(self, animal_type, weight: int, height: int, pet: bool, species: str):
        if animal_type.lower() == "fish":
            return Fish(weight, height, pet, species)
        else:
            raise ValueError("Invalid type")


    def create_employee(self, employee_type, name, surname, patronymic, age, id):
        if employee_type.lower() == "employee":
            return Employee(name, surname, patronymic, age, id)
        else:
            raise ValueError("Invalid type")