import csv

#Task 3: List Comprehensions Practice

try: 
    with open("./csv/employees.csv", "r") as file:
        reader = csv.reader(file)
        employee_list = list(reader)

        # create a list of the employee names, first_name + space + last_name. The list comprehension should iterate through the items in the list read from the csv file
        employee_names = [f"{row[1]} {row[2]}" for row in employee_list[1:]]
        print(employee_names)

        #Using a list comprehension, create another list from the previous list of names. This list should include only those names that contain the letter "e". Print this list
        e_names = [name for name in employee_names if "e" in name.lower()]
        print(e_names)
except Exception as e:
    print(f"An exception occurred {e}")

