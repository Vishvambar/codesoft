# Task 3: Password Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
