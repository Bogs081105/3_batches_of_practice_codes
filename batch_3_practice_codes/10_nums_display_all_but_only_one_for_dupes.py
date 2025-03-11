#create an empty list to append the numbers
nums = [0]
#created an empty set to store duplicates.
dupes = set()
#ask the user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)
#create a function that displays all nums but only 1 copy of nums that has dupes
if num not in dupes:
    dupes.add(num)
    
#display the numbers
print(nums)
    