#set total to 0 to represent the start of the count for even numbers
total = 0
#input 10 numbers using for loop
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
#function to count even numbers
#for every number that is divisible by 2(even numbers are also divisible by 2) add into total
    if num % 2 == 0:
        total += 1
#print the amount of even numbers
print(f"The number of even numbers is/are: {total}")