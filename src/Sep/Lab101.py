#  Class Variable.
#  Method
#      # Public - Variable - Don't Mention anything
#      # Protected - _
#      # Private - __
# Inheritance
# Polymorphism
# Abstraction,
# Encapsulation
# Static Method
# Variables


# Variables
# 1. Local Variable (within the functionc / block
# 2. global
# 3. instance variable (within the class
# 4. static variable ( in future)

a = 10


class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class

    def print_infor(self):
        global a # Declare it as global
        a = "Hello"
        print(self.b)
        print(self.c)



object_Ref = Person()
object_Ref.print_infor()
print(a)
# print(b)