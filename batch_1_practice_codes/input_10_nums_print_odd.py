#ask the user to input 10 numbers, used for loop for convenience
#set the total to 0, then for every input, add 1 input until it reaches 10 inputs
total = 0
for i in range (10):
    num = float(input(f"Enter number{i+1}: "))

#define the odd numbers and add the count for odd numbers
if num % 2 != 0:
    total += 1
#print the number of odd numbers