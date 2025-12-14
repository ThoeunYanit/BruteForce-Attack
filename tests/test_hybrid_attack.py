from src.attacks.hybrid_attack import HybridAttack
from src.users.user_management import UserManagement

#case 1: find exisiting password
def test_password_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_list.txt"

    attack = HybridAttack(um, wordlist)
    result = attack.crack_user("dani")

    assert result == None

#case 2: password is not found in the dictionary_list and cannot find after being add suffix(suffix length = 3)
def test_password_not_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_list.txt"

    attack = HybridAttack(um, wordlist)
    result = attack.crack_user("max")

    assert result == None

#case 3: test with wrong file of dictionary_list, so we expect result=None and it will print Dictionary file not found.
def test_file_not_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_lists.txt" #dictionary_lists.txt

    attack = HybridAttack(um, wordlist) 
    result = attack.crack_user("dani")

    assert result == False
