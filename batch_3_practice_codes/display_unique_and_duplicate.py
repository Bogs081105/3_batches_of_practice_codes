#use set function to store numbers that have been entered
seen_nums = set()
#using while loop, continuously ask for the user until invalid input
while True:
    user_input = input("Please enter a number(or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
#check if the number is a duplicate or unique
    try:
        num = float(user_input)
        
        if num in seen_nums:
            print("Duplicate")
        else:
            print("Unique")
            seen_nums.add(num)
#check if the input is a valid number
#print invalid if the number is invalid
    except ValueError:
        print("Invalid input.")
        break