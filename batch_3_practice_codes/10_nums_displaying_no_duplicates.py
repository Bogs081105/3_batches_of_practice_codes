#ask the user to input 10 nums using for loop
#added an empty set
nums = []
for i in range (10):
    num = int(input(f"Enter number{i+1}: "))
#check if the numbers have duplicates
#append the numbers first in the list
nums.append(num)