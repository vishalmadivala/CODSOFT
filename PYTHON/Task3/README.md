# Task 3 — Password Generator

**CodSoft Python Programming Internship**

## Description
A command-line tool that generates strong, random passwords. The user
specifies the desired length and which character types to include
(lowercase, uppercase, digits, symbols). Passwords are generated using
Python's `secrets` module for cryptographically secure randomness, and
the generator guarantees at least one character from each selected type.

## Features
- User-specified password length
- Configurable complexity: lowercase, uppercase, digits, symbols
- Cryptographically secure randomness (`secrets` module, not `random`)
- Guarantees at least one character from each chosen category
- Generate multiple passwords in one session

## Requirements
- Python 3.7+
- No external libraries needed (see `requirements.txt`)

## How to Run
```bash
python password_generator.py
```

Then follow the prompts:
```
Enter the desired password length: 16
Include lowercase letters (a-z)? (Y/n):
Include uppercase letters (A-Z)? (Y/n):
Include digits (0-9)? (Y/n):
Include symbols (!@#$...)? (Y/n):
```

## Files
| File | Description |
|---|---|
| `password_generator.py` | Main application source code |
| `requirements.txt` | Project dependencies |
| `output/sample_run.txt` | Example of a sample program run |

## Example
```
Generated Password:
  qT8!vR2$mLp9
```

## Author
Vishal — CodSoft Python Programming Virtual Internship (Sept 2026)
