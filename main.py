# Loop tasks
# Task 1: Create a loop that says hello 10 times
for _ in range(10):  # loops 10 times
    print("Hello!")  # prints the hello string

# Task 2: Create another loop that asks for names and appends them to a list of names
list_names = []  # Creating an empty list that we can add to
for _ in range(5):  # Looping 5 times as the number was not specified in the task
    name = input("Please enter a name:  ")  # Receiving user input and storing the name given in the name variable
    list_names.append(name)  # Adding the name given to the list
print(list_names)  # Printing the list to make sure that the program ran successfully

# Task 3: Create a loop that iterates over the list created in the previous task and
# formats it into lowercase, saving these new lowercase names into a new list
list_names_lower = []  # Creating an empty list that we can add to
for names in list_names:  # Looping through each item stored in the list_names list
    lower_name = names.lower()  # Converting the names to lowercase and saving this in a new variable
    list_names_lower.append(lower_name)  # Adding this lowercased name into our new list
print(list_names_lower)  # Printing the list to make sure that the program ran successfully

# Task 4: Loop over a list of values to see if they are even
num_list = [1, 2, 3, 4, 5, 6, 7, 8]  # Creating a list of even and odd numbers
for num in num_list:  # Looping through the entire list
    if num % 2 == 0:  # If the number can be cleanly divided by 0
        print("Even")  # It must be even
    else:  # Otherwise
        print("Odd")  # It must be odd
