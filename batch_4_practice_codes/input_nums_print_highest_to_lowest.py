#create an empty list to store numbers
nums = []
#input continuously using for loop
while True:
    try:
        num = int(input("Enter a number(input an invalid item to stop): "))
#append numbers into list
        nums.append(num)
#check if invalid input
    except ValueError:
        print("Invalid Input")
        break
#sort in descending order
#display results