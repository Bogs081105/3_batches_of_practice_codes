#create an empty list to append the numbers
nums = [0]
#ask the user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)
#create a function that displays all nums but only 1 copy of nums that has dupes
repeating = [num for num in nums if nums.count(num) != 1]
#print all the numbers
print(repeating)