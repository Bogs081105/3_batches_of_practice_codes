#create an empty list
nums = []
#ask continuously for numbers using while loop
while True:
    try:
        num = int(input("Enter a number(Input an invalid item to stop): "))
#append numbers into list
        nums.append(num)
#stop if invalid number
    except ValueError:
        print("The input is invalid")
        break
#calculate the average
#print the result