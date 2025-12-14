# BruteForce-Attack-Simulation

## Project Overview
This is a Brute Force Attack Simulator written in Python Programming Language, created for educational purposes.
This Project demonstrates how **simple brute-force attack**, **dictionary attack**, and **hybrid attack** work, along with **user management** where everyone can create, update, view and delete users.

## Features
1. **User Management**
   - Create, update, view and delete users
   - Usernames and Passwords are stored in a local text file (`user_database.txt`) 
2. **Simple Brute Force Attack**
   - Try all possible combinations of characters to crack a password and display *found password* 
3. **Simple Brute Force Attack (With Attempt Count)**
   - Track the number of attempts during the operation
4. **Dictionary Attack**
   - Attempt passswords from a wordlist (`dictionary_list.txt`)
5. **Hybrid Attack**
   - Combine dictionary attack with characters (digits and punctuation)

## Steps to Run the Code
### 1. Clone or Download the Project
```bash
git clone https://github.com/ThoeunYanit/BruteForce-Attack.git
```
### 2. Navigate to the Project Directory
```bash
cd BruteForce-Attack
```
### 3. Run the Main Program
```bash
python src/main.py
```

### 4. Run Tests (Optional)
To run all tests using pytest:
```bash
pytest 
```
Or test a specific file
```bash
pytest tests/test_simple_bruteforce_attack.py
```


## Technologies Used
- Python 3.13.7
- pytest (for testing)
- Standard Python libraries (itertools, string)

### Required Libraries (pytest)
```
pip install pytest
```

## Project Structure 
```text
BruteForce-Attack/
│
├── src/
│   ├── __init__.py
│   │
│   ├── users/
│   │   ├── __init__.py
│   │   └── user_management.py
│   │
│   ├── attacks/
│   │   ├── __init__.py
│   │   ├── simple_bruteforce_attack.py
│   │   ├── dictionary_attack.py
│   │   └── hybrid_attack.py
│
├── data/
│   ├── user_database.txt
│   └── dictionary_list.txt
│
├── tests/
│   ├── __init__.py
│   ├── test_simple_bruteforce_attack.py
│   ├── test_dictionary_attack.py
│   ├── test_hybrid_attack.py
│   └── test_user_management.py
│
├── main.py
└── README.md
```

## Github Link
```bash
https://github.com/ThoeunYanit/BruteForce-Attack.git
```