"""
Password Generator
CodSoft Python Programming Internship - Task 3

Generates strong, random passwords based on a user-specified length and
complexity (character sets to include: lowercase, uppercase, digits,
symbols). Uses the `secrets` module for cryptographically strong
randomness.
"""

import string
import secrets


def get_length():
    while True:
        raw = input("Enter the desired password length: ").strip()
        if raw.isdigit() and int(raw) > 0:
            length = int(raw)
            if length < 4:
                print("Warning: very short passwords are weak. Recommended: 12+.")
            return length
        print("Please enter a positive whole number.")


def get_yes_no(prompt, default_yes=True):
    suffix = " (Y/n): " if default_yes else " (y/N): "
    raw = input(prompt + suffix).strip().lower()
    if raw == "":
        return default_yes
    return raw.startswith("y")


def build_character_pool():
    print("\nChoose which character types to include:")
    use_lower = get_yes_no("Include lowercase letters (a-z)?", True)
    use_upper = get_yes_no("Include uppercase letters (A-Z)?", True)
    use_digits = get_yes_no("Include digits (0-9)?", True)
    use_symbols = get_yes_no("Include symbols (!@#$...)?", True)

    pool = ""
    guaranteed = []
    if use_lower:
        pool += string.ascii_lowercase
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        pool += string.ascii_uppercase
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        pool += string.digits
        guaranteed.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{}?"
        pool += symbols
        guaranteed.append(secrets.choice(symbols))

    if not pool:
        print("No character types selected — defaulting to lowercase letters.")
        pool = string.ascii_lowercase
        guaranteed = [secrets.choice(string.ascii_lowercase)]

    return pool, guaranteed


def generate_password(length, pool, guaranteed):
    if length < len(guaranteed):
        # Not enough room to guarantee one of each type; just sample from pool.
        return "".join(secrets.choice(pool) for _ in range(length))

    remaining = length - len(guaranteed)
    password_chars = guaranteed + [secrets.choice(pool) for _ in range(remaining)]
    # Shuffle securely so guaranteed characters aren't always at the front.
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]
    return "".join(password_chars)


def main():
    print("=" * 40)
    print("PASSWORD GENERATOR".center(40))
    print("=" * 40)

    while True:
        length = get_length()
        pool, guaranteed = build_character_pool()
        password = generate_password(length, pool, guaranteed)

        print("\nGenerated Password:")
        print(f"  {password}")

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Stay secure! Goodbye.")
            break


if __name__ == "__main__":
    main()
