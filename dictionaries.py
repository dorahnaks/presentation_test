# Dictionaries

#1. Basic: 
# Create a dictionary with three key-value pairs representing a student's information:
# name, age, and grade. Print each key-value pair on a new line.

def student_info():
    stud_dict = {"name": "Dorothy", "age": 20, "grade": "A"}
    for key, value in stud_dict.items():
        print(f"{key}: {value}")
student_info()

# def student_info():
#     stud_dict = {"name": "Dorothy", "age": 20, "grade": "A"}
#     for item  in stud_dict:
#         print(item)
# student_info()



#2. Intermediate: 
# Write a function that takes a dictionary of people's names and their ages, 
# {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.

def people_older():
    dct = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
    older_people = []
    for key, value in dct.items():
        if value > 21:
            older_people.append(key)
    print(f"The people older than 21 are: {older_people}")
people_older()




# Advanced: 
# Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, 
# write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.

def cost_of_items():
    store_dict = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
    items_bought = ['apple', 'orange', 'banana', 'banana']
    total_cost = 0
    
    for item in items_bought:
        total_cost += store_dict[item]
    print(f"The total cost is:  {total_cost}")
    
cost_of_items()       




# Challenge: 
# Write a program that counts the occurrences of each word in a given sentence. 
# Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

def word_occurrences(sentence):
    words = sentence.split()
    occurrences = {}
    
    for word in words:
        if word in occurrences:
            occurrences[word] += 1 
        else:
            occurrences[word] = 1 
    
    print(occurrences)
sentence = "hello world hello" 
word_occurrences(sentence)