# CODSOFT Task 3: Password Generator
import random
import string

def generate_password():
    print("--- Password Generator ---")
    
    try:
        # Get user input for password length
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Define the characters to use
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for i in range(length))
        
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Invalid input. Please enter a number for the length.")

if __name__ == "__main__":
    generate_password()