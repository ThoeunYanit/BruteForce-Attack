from src.attacks.dictionary_attack import DictionaryAttack
from src.users.user_management import UserManagement

#case 1: find exisiting password
def test_password_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_list.txt"

    attack = DictionaryAttack(um, wordlist)
    result = attack.crack_user("mbappe")

    assert result == 'apple'

#case 2: password is not found in the dictionary_list
def test_password_not_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_list.txt"

    attack = DictionaryAttack(um, wordlist)
    result = attack.crack_user("ajax")

    assert result == None

#case 3: test with wrong file of dictionary_list, so we expect result=None and it will print Dictionary file not found.
def test_file_not_found():
    um = UserManagement("data/user_database.txt")
    wordlist = "data/dictionary_lists.txt" #dictionary_lists.txt

    attack = DictionaryAttack(um, wordlist) 
    result = attack.crack_user("ajax")

    assert result == False
