#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_letter = ''
for letter in letters:
    password_letter = random.sample(letters, nr_letters)

for number in numbers:
    password_number = random.sample(numbers, nr_numbers)

for symbol in symbols:
    password_symbol = random.sample(symbols, nr_symbols)

password = password_letter + password_number + password_symbol
random.shuffle(password)
password_random = "".join(password) 
print(f"Your random password is {password_random}")


# second method
# password = ""
# for char in range(1, nr_letters + 1):
#     password +=  random.choice(letters)

# for char in range(1, nr_symbols +1):
#     password +=  random.choice(symbols)  

# for char in range(1, nr_numbers +1):
#     password +=  random.choice(numbers)   

# print(password)      


    