#initialize an empty list to store the numbers
nums = []
#ask the user to input nums continuously using while 
while True:
    try:
        num = int(input("Enter a number(input invalid item to stop): "))
#append the numbers to the list
        nums.append(num)
#add a function that excludes invalid inputs
    except ValueError:
        print("Invalid Input")
        break
#find and display the highest number