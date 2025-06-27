class Shape:
    def area(self):
        pass

    def greating(self):
        print("Hello from Shape!")


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

obj = Circle()
obj.greating()
print(obj.area(5))