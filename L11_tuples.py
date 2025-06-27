# Tuples Like Lists but not edit
var = (1, 2, 3, 4, 5)


# to ediit a tuple you need to convert it to a list
var_list = list(var)  # Convert tuple to list
var_list[0] = 10  # Modify the list
var = tuple(var_list)  # Convert list back to tuple 
print(var)  # Output: (10, 2, 3, 4, 5)