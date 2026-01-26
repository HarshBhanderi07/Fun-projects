class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_details(self):
        print("Name:",self.name)
        print("Age:",self.age,"\n")
        
class employee(person):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id = id
        self.salary = salary
        
    def set_id(self,id):
        self.id = id
        
    def get_id(self):
        return self.id
    
    def set_salary(self,salary):
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    @classmethod
    def from_name_age(cls,name,age):
        return cls(name,age)
    
    @classmethod
    def from_full_data(cls,name,age,id,salary):
        return cls(name,age,id,salary)
    
    def display_details(self):
        super().display_details()
        print("Employee ID:",self.id)
        print("Salary:",self.salary,"\n") 
        
class manager(employee):
    def __init__(self,name,age,id,salary,department):
        super().__init__(name,age,id,salary)
        self.department = department
        
    def display(self):
        super().display_details()
        print("Department:",self.department,"\n")
        
def create_person():
    name = input("Enter name:")
    age = input("Enter age:")
    return person(name,age)

def create_employee():
    name = input("Enter name:")
    age = input("Enter age:")
    id = input("Enter employee ID:")
    salary = input("Enter salary:")
    return employee(name,age,id,salary)

def create_manager():
    name = input("Enter name:")
    age = input("Enter age:")
    id = input("Enter manager ID:")
    salary = input("Enter salary:")
    department = input("Enter department:")
    return manager(name,age,id,salary,department)

def show_details(person,employee,manager):
    print("choose details to show:")
    print("1. Person details")
    print("2. Employee details")
    print("3. Manager details")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        if person:
            print("\n--- Person Details ---\n")
            person.display_details()
        else:
            print("No person data available.\n")
    elif choice == 2:
        if employee:
            print("\n--- Employee Details ---\n")
            employee.display_details()
        else:
            print("No employee data available.\n")
    elif choice == 3:
        if manager:
            print("\n--- Manager Details ---\n")
            manager.display()
        else:
            print("No manager data available.\n")
    else:
        print("Invalid choice.\n")
        
        

def main():
    person = None
    employee = None
    manager = None
    print("\n----------------- Employee Management System ----------------\n")
    while True:
        print("""choose an operation:
        1. Add person
        2. Create an employee
        3. Create a manager
        4. Show details
        5. Exit\n""")

        choice = int(input("Enter your choice:"))
        
        if choice == 1:
            person = create_person()
            print("\nPerson added successfully!\n")
        elif choice == 2:
            employee = create_employee()
            print("\nEmployee created successfully!\n")
        elif choice == 3:
            manager = create_manager()
            print("\nManager created successfully!\n")
        elif choice == 4:
            show_details(person,employee,manager)
        elif choice == 5:
            print("Exiting the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
