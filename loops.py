# PYTHON DISCUSSION QUESTIONS
# Loops

# 1. Basic: 
# Write a Python program that prints all even numbers between 1 and 20 using a for loop.

# def even_numbers():
#     for num in range(1, 21):
#         if num % 2 != 1:
#             print(num)
# even_numbers()

def even_numbers():
    for num in range(2, 21, 2):
            print(num)
even_numbers()



# 2. Intermediate: 
# Use a while loop to ask the user to input a number until they provide a number greater than 10.

def num_greater():
    number = int(input("Enter a number: "))
    while number  < 11:
        number = int(input("Enter a number greater than ten to exit: ")) 
    else:
        print(f"{number} is greater than ten.")   
num_greater()
        
        

# Advanced: 
# Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

def multiplication_table():
    for num in range(1, 6):  
        print(f"Multiplication table for {num}") 
        for int in range(1, 11):  
            print(f"{num}  x  {int} = {num * int}") 
        print("\n")   
multiplication_table()




# Challenge: 
# Given a list of integers, [4, 7, 2, 9, 12, 15], 
# write a program using a for loop to find the sum of all odd numbers and print the result.

def sum_of_odd_num():
    integers = [4, 7, 2, 9, 12, 15]
    sum_odd = 0
    for num in integers:
        if num % 2 != 0:
            sum_odd += num
    print(f"The sum of all odd numbers is: {sum_odd}")
sum_of_odd_num()            
