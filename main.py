from password_generator import generate_password

def main():
    print("Welcome to the Password Generator 🔐\n")

    # If it's not a valid number
    while True:
        length_input = input("Enter password length (4-50): ")
        if not length_input.isdigit():
            print("Please enter a valid number.")
            continue
        length = int(length_input)
        if length < 4 or length > 50:
            print("Password length must be between 4 and 50.")
            continue
        break

    use_lower = input("Include lowercase letters? (y/n) : ").lower() == "y"
    use_upper = input("Include uppercase letters? (y/n) : ").lower() == "y"
    use_digits = input("Include digits? (y/n) : ").lower() == "y"
    use_special = input("Include special characters? (y/n) : ").lower() == "y"

    password = generate_password(length, use_lower, use_upper, use_digits, use_special)
    print(f"\nGenerated password : {password}")

if __name__ == "__main__":
    main()
