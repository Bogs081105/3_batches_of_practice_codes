#initialize an empty list
nums = []
#using for loop, ask the user for 10 nums
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
#append the inputs inside the set
    nums.append(num)
#find the duplicates
dupes = set([num for num in nums if nums.count(num > 1)])
#print results