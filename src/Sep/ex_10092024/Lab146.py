import os

full_path_file = os.path.join(r"C:\Users\likhi\PycharmProjects\PyATB4xLearning\src\Sep\ex_10092024", "Likhith.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)