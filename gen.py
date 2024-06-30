import string
import random

uppercase = string.ascii_uppercase
numbers = [str(y) for y in range(11)]  # Creating a list of strings '0' to '10'
special = string.punctuation

random_pass = ""

for i in range(8):
    random_lett = random.choice(uppercase)  # Choose a random uppercase letter
    random_num = random.choice(numbers)     # Choose a random number
    random_special = random.choice(special)
    random_pass += random_lett + random_num + random_special # Append both to the password and the specials characters

print(f"The random password of uppercase letters and random numbers is: {random_pass}")
