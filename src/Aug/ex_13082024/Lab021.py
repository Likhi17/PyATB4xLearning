my_shopping_list = ["milk", "bread", "apple"]
my_10th_marks = [90, 91, 92, 56]

# Strings
name = "Likhith"
# str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))  # 7

a = "90"
age = 90
print(type(a))
print(type(age))

name = "This is a Big line"
print(type(name))
name = name + str(1)
print(name)


first_name = "Likhith"
last_name = " Gowda"
full_name = first_name+last_name # CONCAT
print(full_name)


how_many_planes_i_have = None
print(type(how_many_planes_i_have)) # NoneType
# null is not present in Python

val = 0 # This is int

# id
age = 10
age2 = 11
print(id(age)) # 4336051480
print(id(age2)) # 433603232