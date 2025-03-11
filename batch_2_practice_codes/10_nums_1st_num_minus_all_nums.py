#using for loop, input 10 numbers
#added an empty set to store the numbers
nums = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
#added append function to add the numbers into the empty set
    nums.append(num)
#program it to subtract all of the remaining numbers to the first number
#added a first num function which only gets the first number inside the index
first_num = nums[0]
#print the result