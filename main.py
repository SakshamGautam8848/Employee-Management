from database import *

def main():
    create_table() # initialize database

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            position = input("Position: ")
            department = input("Department: ")
            salary = float(input("Salary: "))
            add_employee(name, position, department, salary)
            print("Employee Added Successfully!!!")
        
        elif choice == "2":
            employees = get_all_employees()
            if not employees:
                print("No Employees Found!!!")
            else:
                print("\nEmployee List:")
                for emp in employees:
                    print(f"ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Department: {emp[3]}, Salary: Rs.{emp[4]: .2f}")
        elif choice == "3":
            emp_id = int(input("Enter employee ID to update: "))
            name = input("New Name: ")
            position = input("New Position: ")
            department = input("New Department: ")
            salary = float(input("New Salary: "))
            update_employee(emp_id, name, position, department, salary)
            print("Employee Updated Successfully!!!")
        
        elif choice == "4":
            emp_id = int(input("Enter employees ID to delete: "))
            delete_employee(emp_id)
            print("Employee Deleted Successfully!!!")
        
        elif choice == "5":
            emp_id = int(input("Enter employee ID to search: "))
            employee = search_employee(emp_id)
            if employee:
                print(f"\nEmployee Found: ")
                print(f"ID: {employee[0]}")
                print(f"Name: {employee[1]}")
                print(f"Position: {employee[2]}")
                print(f"Department: {employee[3]}")
                print(f"Salary: {employee[4]}")
            else:
                print("Employee Not Found!!!")
        
        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()