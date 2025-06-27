var = [1, 2.5 , 'hello' , True]
var.append(3) # Output: [1, 2.5, 'hello', True, 3]
var.insert(1, 'world')  # Output: [1, 'world', 2.5, 'hello', True, 3]
var.remove(2.5) # Output: [1, 'world', 'hello', True, 3]
var.pop(0) # Output: ['world', 'hello', True, 3]
print(var)  # Output: ['world', 3, 'hello', True]
var.clear() 
var=[50,2,1,4]
var.sort()  # error with mixed types
print(var)  # Output: [1, 2, 4, 50]
var.reverse()  
print(var)  # Output: [50, 4, 2, 1]

var2=[1, 2, 3]


# concatenating lists using the extend method
var.extend(var2)
print(var)  # Output: [50, 4, 2, 1, 1, 2, 3]


# Using the + operator to concatenate lists
x=[50,2,1,4]
x+=var2
print(x)  # Output: [50, 2, 1, 4, 1, 2, 3]

# List is ordered, so we can access elements by index