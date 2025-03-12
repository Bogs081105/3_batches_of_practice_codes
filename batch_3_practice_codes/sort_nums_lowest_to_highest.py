#initialize an emptylist
nums = []
#using while loop, ask the user to input the numbers
while True:
    num = int(input("Enter a number(enter non-numeric value to stop): "))
#append into list
    nums.append(num)
#stop if invalid number
    try:
        float(num)
    except ValueError:
        print("Invalid input")
        break
#sort the numbers from lowest to highest
nums.sort()
#print the sorted numbers