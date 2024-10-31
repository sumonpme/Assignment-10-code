 #Accessing and modifying elements in a dictionary with nested structures.
nested_dict = {
    "employee": {
        "name": "Ahmed",
        "age": 50,
        "birth place": "Khulna"
    }
}
# Accessing the employee's birth place
employee_birth_place = nested_dict["employee"]["birth place"]
# Modifying elements
nested_dict["employee"]["age"] = 51
print("Employee Birth Place:", employee_birth_place) 
print("Updated Employee Dictionary:", nested_dict["employee"])