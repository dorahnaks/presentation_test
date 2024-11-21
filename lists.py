# Lists

# Basic: 
# Create a list of 5 fruits and print each fruit on a new line using a for loop.

def fruit_list():
    fruits = ["Apples", "Mangoes","Oranges", "Pineapples", "Grapes"]
    for fruit in fruits:
        print(f"{fruit} \n")
fruit_list()


# Intermediate: 
# Write a function that takes a list of numbers and returns a new list with each number squared. 
# Example: [1, 2, 3] should become [1, 4, 9].

def squaring_list():
    original_list = [1,2,3,4,5]
    squared_list = []
    for int in original_list:
        squared_list.append(int ** 2)
    print(f"The new list with each number squared is: {squared_list}")
squaring_list()



# # Advanced: 
# # Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], 
# # and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

def combining_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = list1 + list2
    print(f"The combined list is: {combined_list}")
combining_lists()



# Challenge: 
# Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], 
# write a program to find and print the two largest numbers in the list without using the max() function.

def largest_numbers():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    
    numbers.sort(reverse=True)
    largest = numbers[0]
    sec_largest = numbers[1]
    
    print(numbers)
    print(f"The largest number is: {largest}")
    print(f"The second largest number is: {sec_largest}")
largest_numbers()