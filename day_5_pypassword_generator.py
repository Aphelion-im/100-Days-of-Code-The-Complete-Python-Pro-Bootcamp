import random

letters_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
letters_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password_array = []

print("Welcome to PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?: "))
number_of_symbols = int(input("How many symbols would you like in your password?: "))
number_of_numbers = int(input("How many numbers would you like in your password?: "))

# Letters lowercase
for char in range(0, number_of_letters):
    random_char = random.choice(letters_lowercase)
    password_array.append(random_char)

# Symbols
for symbol in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password_array.append(random_symbol)

# Numbers
for number in range(0, number_of_numbers):
    random_number = random.choice(numbers)
    password_array.append(random_number)

random.shuffle(password_array)

password = ""

for entry in password_array:
    password += entry

print(f"Your new password is: {password}")
