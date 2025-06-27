# متعددة الاشكال
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # Overriding the speak method
    def speak(self):
        print("Dog barks")

obj = Dog()
obj.speak()  # Output: Dog barks
