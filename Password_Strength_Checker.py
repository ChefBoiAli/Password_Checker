import re

def has_common_patterns(password):
    # Define common patterns or dictionary words to check against
    common_patterns = [
        r'\bpassword\b',  # Matches the word 'password'
        r'\b123456\b',    # Matches the number sequence '123456'
        r'\bqwerty\b',  # Matches the word 'qwerty'
        r'\badmin\b',  # Matches the word 'admin'
        r'\b12345678\b',  # Matches the number sequence '12345678'
        r'\b12345\b',  # Matches the number sequence '12345'
        r'\b1234567\b',  # Matches the number sequence '1234567'
        r'\b123456789\b',  # Matches the number sequence '123456789'
        r'\bletmein\b',  # Matches the word 'letmein'
        r'\bwelcome\b',  # Matches the word 'welcome'
        r'\bp@ssw0rd\b',  # Matches the word 'p@ssw0rd!'
        # Add more common patterns or dictionary words as needed
    ]

    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return True

    return False

def check_password_strength(password):
    # Define the criteria for password strength
    minimum_length = 8
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c for c in password if c.isalnum() is False)

    # Perform the password strength checks
    if len(password) < minimum_length:
        return "Password should have at least 8 characters."
    elif not has_lowercase:
        return "Password should contain at least one lowercase letter."
    elif not has_uppercase:
        return "Password should contain at least one uppercase letter."
    elif not has_digit:
        return "Password should contain at least one digit."
    elif not has_special:
        return "Password should contain at least one special character."
    elif has_common_patterns(password):
        return "Password should not contain common patterns or dictionary words."
    else:
        return "Password is strong."

def main():
    # Prompt the user to enter a password
    password = input("Enter a password: ")

    # Check the strength of the password
    result = check_password_strength(password)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()