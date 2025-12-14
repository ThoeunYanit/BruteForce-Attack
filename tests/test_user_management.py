from src.users.user_management import UserManagement

#case 1: test if reload is really returning dictionary value, if it is, return True else False
def test_reload_user():
    um = UserManagement("data/user_database.txt")
    
    result = um.reload_user() 

    assert result == True

#case 2: test if reload is really returning dictionary value, if it is, return True else False (Wrong path file in this case)
def test_reload_user_file_not_found():
    um = UserManagement("data/user_databases.txt") #FileNotFoundError
    
    result = um.reload_user() 

    assert result == False

