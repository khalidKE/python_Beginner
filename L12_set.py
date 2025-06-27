# set unique values
# cnn't accwess by index
# ordered 
# remove duplicates

var = {1, 2, 3, 4, 5,5,5}
# add an element
var.add(6)  # Output: {1, 2, 3, 4, 5, 6}
# remove an element     
var.remove(3)  # Output: {1, 2, 4, 5, 6}
print(var)  # Output: {1, 2, 4, 5, 6}

var.union({7, 8})  # Output: {1, 2, 4, 5, 6, 7, 8}

# set is unordered, so we cannot access elements by index