import random
import string


def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    if length < 4 or length > 50:
        return "Password length must be between 4 and 50"

    lower = string.ascii_lowercase if use_lower else ""
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_chars = lower + upper + digits + special
    if not all_chars:
        return "You must enable at least one character set!"

    password_chars = []

    if use_lower:
        password_chars.append(random.choice(lower))
    if use_upper:
        password_chars.append(random.choice(upper))
    if use_digits:
        password_chars.append(random.choice(digits))
    if use_special:
        password_chars.append(random.choice(special))

    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

    random.shuffle(password_chars)
    return "".join(password_chars)

