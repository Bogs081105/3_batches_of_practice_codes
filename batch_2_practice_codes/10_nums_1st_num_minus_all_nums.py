#using for loop, input 10 numbers
#added an empty set to store the numbers
nums = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
#added append function to add the numbers into the empty set
    nums.append(num)
#program it to subtract all of the remaining numbers to the first number
#added first num function for the first number
first_num = nums[0]
#used slice 1 up until the last number to subtract the first num and the numbers
for num in nums[1:]:
    first_num -= num

#print the result