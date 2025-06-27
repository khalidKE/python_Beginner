counter = 0
while counter < 5:
    print("Counter is:", counter)
    counter += 1


for i in range(5):
    print("Counter is:", i)


for char in "Hello":
    print("Character is:", char)



# Nested loops example with a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print("Element is:", col)