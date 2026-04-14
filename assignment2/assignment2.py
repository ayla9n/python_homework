import csv
import os
import custom_module
from datetime import datetime

#Task 2: Read a CSV File
def read_employees():
    
    employees_dict = {}
    rows = []
    try: 
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                #if its the first row, store in dictionary; otherwise store in the list
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)
            
            employees_dict["rows"] = rows

    except Exception as e:
        print(f"An exception occurred {e}")

    return employees_dict


employees = read_employees()
#print(employees)


#Task 3: Find the Column Index
def column_index(string):
    return employees["fields"].index(string)

employee_id_column = column_index("employee_id")
# print(employee_id_column)


#Task 4: Find the Employee First Name 
def first_name(row_num):
    row_index = column_index("first_name")
    return employees["rows"][row_num][row_index]

#print(first_name(1))


#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    #return the rows with the matching employee id
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches
    
#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key= lambda row: row[last_name_index])
    return employees["rows"]

#print(sort_by_last_name())


#Task  8:Create a dict for an Employee
def employee_dict(row):
    employee_dict = {}

    for col in range(1,len(employees["fields"])):
        employee_dict[employees["fields"][col]] = row[col]

    return employee_dict


#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    results = {}
    employee_id_index = column_index("employee_id")
    for row in employees["rows"]:
        results[row[employee_id_index]] = employee_dict(row)
    return results

#print(all_employees_dict())


#Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

#print(get_this_value())


#Task 11: Creating Your Own Module        
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("GF cookies")  
#print(custom_module.secret)                


#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}
    minutes_list = []

    files = ["../csv/minutes1.csv", "../csv/minutes2.csv"]
    try: 
        for file_name in files: 
            minutes = {}
            minutes_rows = []
            with open(file_name, "r") as file:
                reader = csv.reader(file)

                for i, row in enumerate(reader):
                    #if its the first row, store in dictionary; otherwise store in the list
                    if i == 0:
                        minutes["fields"] = row
                    else:
                        minutes_rows.append(tuple(row))
                
                minutes["rows"] = minutes_rows
                minutes_list.append(minutes)
        
        minutes1, minutes2 = minutes_list

    except Exception as e:
        print(f"An exception occurred {e}")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()


#Task 13: Create minutes_set
def create_minutes_set():
    min1_set = set(minutes1["rows"])
    min2_set = set(minutes2["rows"])
    return min1_set | min2_set

minutes_set = create_minutes_set()


#Task 14: Convert to datetime
def create_minutes_list():
    min_list = list(minutes_set)
    result = list(map(lambda row: (row[0], datetime.strptime(row[1],"%B %d, %Y")), min_list))
    return result 

minutes_list = create_minutes_list()
print(minutes_list)


#Task 15:Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda row: row[1])
    converted_list = list(map(lambda row: (row[0], datetime.strftime(row[1], "%B %d, %Y")), sorted_list))

    try: 
        with open("./minutes.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_list)

    except Exception as e:
        print(f"An exception occurred {e}")
    
    return converted_list

write_sorted_list()