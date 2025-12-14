from src.users.user_management import UserManagement
from src.attacks.simple_bruteforce_attack import SimpleBruteForceAttack

#case 1: password found
def test_password_found():
    um = UserManagement("data/user_database.txt")
    attack = SimpleBruteForceAttack(um)

    result = attack.crack_user("messi") #username

    assert result == "goat" #password we expect to get from username

#case 2: find the non-existent user
def test_user_not_found():
    um = UserManagement("data/user_database.txt")
    attack = SimpleBruteForceAttack(um)

    result = attack.crack_user("not_messi")

    assert result == None

#case 3: password cannot be cracked
def test_password_not_cracked():
    um = UserManagement("data/user_database.txt")
    attack = SimpleBruteForceAttack(um)

    result = attack.crack_user("messi", char="xyz")

    assert result == None

#case 4: user_database file is incorrect
def test_file_path_incorrect():
    um = UserManagement("data/user_databases.txt")
    attack = SimpleBruteForceAttack(um)

    result = attack.crack_user("messi")

    assert result == False
