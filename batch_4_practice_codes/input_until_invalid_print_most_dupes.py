#create an empty list to store dupes
nums = []
#continuously ask the user for nums until invalid input
while True:
    try:
        num = int(input("Enter a number (enter an invalid item to stop): "))
#append to list
        nums.append(num)
#stop if an invalid input is entered
    except ValueError:
        print("Invalid Input")
        break
#find the number with the most duplicates
#print the result