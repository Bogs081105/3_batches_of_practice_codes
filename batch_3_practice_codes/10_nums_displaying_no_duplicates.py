#ask the user to input 10 nums using for loop
#added an empty set
nums = []
for i in range (10):
    num = int(input(f"Enter number{i+1}: "))
#append the numbers first in the list
nums.append(num)
#check if the numbers have duplicates
#set a new list named no duplicates to insert the numbers with no duplicates
#this checks each numbers if it is the only number inside the list.
no_duplicates = [num for num in nums if nums.count(num) == 1]
print(f"The numbers with no duplicates is/are: {no_duplicates}")