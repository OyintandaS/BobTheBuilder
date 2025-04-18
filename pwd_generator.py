import random
import string

def generate_pwd(length=12):
    
    # Defining the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_+="
    
    # Making sure at least one of each required type
    password = [
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    remaining = length - 3
    all_chars = lowercase + uppercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(remaining))
    
    # Shuffling to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

print("Generated Password: ", generate_pwd())