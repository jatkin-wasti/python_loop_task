# Tasks
## Task: Make loop that prints out hello 10 times
```
for _ in range(10):  # loops 10 times
    print("Hello!")  # prints the hello string
```
## Task: Make loop that asks for names and appends them to a list
```
list_names = []  # Creating an empty list that we can add to
for _ in range(5):  # Looping 5 times as the number was not specified in the task
    name = input("Please enter a name:  ")  # Receiving user input and storing the name given in the name variable
    list_names.append(name)  # Adding the name given to the list
print(list_names)  # Printing the list to make sure that the program ran successfully
```
## Task: Make a loop that converts those names to lowercase and appends them to another list
```
list_names_lower = []  # Creating an empty list that we can add to
for names in list_names:  # Looping through each item stored in the list_names list
    lower_name = names.lower()  # Converting the names to lowercase and saving this in a new variable
    list_names_lower.append(lower_name)  # Adding this lowercased name into our new list
print(list_names_lower)  # Printing the list to make sure that the program ran successfully
```
## Task: Make a loop that determines whether numbers in a list are even or odd
```
num_list = [1, 2, 3, 4, 5, 6, 7, 8]  # Creating a list of even and odd numbers
for num in num_list:  # Looping through the entire list
    if num % 2 == 0:  # If the number can be cleanly divided by 0
        print("Even")  # It must be even
    else:  # Otherwise
        print("Odd")  # It must be odd
```