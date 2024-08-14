"""Task #2

    Create a program , take 2 inputs from the user num1, num2 and give them
    max
    pow num1 to num2
    sub, mul, sum, div.
    Format your out with f{""}"""

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2 : "))

print("Maximum of two numbers:",max(num1,num2))
print("power num1 to num2 :",pow(num1,num2))
print("Sum of two numbers:",(num1+num2))
print("Differance of two numbers:",(num1-num2))
print("Multiplication of two numbers:",(num1*num2))
print("Division of two numbers:",(num1/num2))

print("Formated_num1 is : ", f"{num1 : .5f}")
print("Formated_num2 is : ", f"{num2 : .5f}")