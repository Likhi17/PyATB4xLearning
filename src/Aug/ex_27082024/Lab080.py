#__init__.py

# create dir - normal folder - python doesn't serach the files here or code here.


# python is very, foler with file __int__.py - python will search the code here
# __init__.py -> dir -> module (where python will search better)

# from src.ex_27082024.normal_dir import sum_91
from src.Aug.ex_27082024.Python_Package.Lab082 import sum_two

op = sum_two(3, 4)
print(op)