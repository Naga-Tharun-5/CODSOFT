import random
import string #we imported this module to use the methods such as string.ascii_letters, string.digits, string.punctuation

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password_length = int(input("Enter the desired length of the password: "))


password = generate_password(password_length)


print("Generated Password:", password)