# Object-Oriented Programming (OOP)

# Basic: 
# Create a class called Car with attributes brand and color. 
# Instantiate an object of the Car class and print its attributes.

# Intermediate: 
# Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. 
# Create an instance of Car and call the method.

class Car: 
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print(f"The car brand is {self.brand} and it has a {self.color} color.")  
        
    def start_engine(self):
        print(f"The engine of the car has started.")
         
car_1 = Car("Toyota", "Silver")
car_1.start_engine()





# Advanced: 
# Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

class BankAccount:
    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Remaining balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def print_balance(self):
        print(f"Account Balance: {self.balance}")



# Challenge: 
# Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. 
# The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).


class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Books are available by default

    def _str_(self):
        status = "Available" if self.is_available else "Unavailable"
        return f"'{self.title}' by {self.author} - {status}"


# Define the Library class
class Library:
    def _init_(self):
        self.books = []  # List to store books in the library

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def is_book_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.is_available
        print(f"Book '{title}' not found in the library.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"'{title}' has been returned and is now available.")
                else:
                    print(f"'{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


