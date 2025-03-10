#ask the user to input 10 numbers, used for loop for convenience
#set the total to 0, then for every input, add 1 input until it reaches 10 inputs
total = 0
for i in range (10):
    num = float(input(f"Enter number{i+1}: "))

#add all the numbers
    total += num

#print the sum of the 10 numbers