import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user complexity choice
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    elif length < 8:
        characters = lower_letters + digits
    elif length < 12:
        characters = lower_letters + upper_letters + digits
    else:
        characters = lower_letters + upper_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
