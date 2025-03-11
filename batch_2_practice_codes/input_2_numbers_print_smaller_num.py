#ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#see which number is the smaller number
#print the smaller number
if num1 < num2:
    print(f"{num1} is the smaller number")
elif num2 < num1:
    print(f"{num2} is the smaller number")
else:
    print("the numbers are equal")