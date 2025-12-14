# UserManagement
class UserManagement:

    def __init__(self, user_database_file):
        self.__user_dict = {} #this is a stored dictionary
        self.__user_database_file = user_database_file #this is path of user_database.txt
        
    #to access the stored dictionary which is a private attribute, need this so that we can access outside this class
    def get_user(self):
        return self.__user_dict

    # load user from user_database.txt into a stored dictionary 
    def reload_user(self):
        self.__user_dict.clear() #clear dictionary

        try:
            with open(self.__user_database_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(" : ")
                    self.__user_dict[username] = password

        except FileNotFoundError:
            print("Error: User database file not found.")
            return False
        except PermissionError:
            print("Error: Permission denied to access user database.")
            return False
        except Exception as e:
            print(f"Error: Failed to read user database - {e}")
            return False
        else: 
            return True
        
    
    # save username and password in the stored dictionary into the usser_dataabase.txt
    def save(self):
        try:
            with open(self.__user_database_file, 'w') as file:
                for username in self.__user_dict: 
                    file.write(f"{username} : {self.__user_dict[username]}\n")
        except PermissionError:
            print("Error: Permission denied to write to user database.")
        except Exception as e:
            print(f"Error: Failed to save user database - {e}")
        else:
            return True
            
    #always reload user first to have data in dictionary
    #after that, it will be code of the operation
    #after the operation ends, always save into the user_database.txt

    def create_user(self):
        self.reload_user()

        username = input("Enter a username: ")
        if username in self.__user_dict:
            print("User is already existed!")
            return

        password = input("Enter a password: ")
        
   
        self.__user_dict[username] = password

        try:
            self.save()
        except PermissionError:
            print("Error: Permission denied to write to user database.")
        except Exception as e:
            print(f"Error: Failed to create user - {e}")
        else:
            return True

        

    def update_user(self):

        while True:
            print("\n--- Update User Menu ----")
            print("1.Update Username")
            print("2.Update Password")
            print("3.Exit")

            choice = int(input("Enter choice: "))

            if choice == 1: self.update_username()
            elif choice == 2: self.update_password()
            elif choice == 3: break
            else: print("Invalid Choice!!")
    


    def update_username(self):

        self.reload_user()

        username = input("Enter your username: ")
        if username not in self.__user_dict.keys():
            print("Username does not exist!!")
            return
        
        new_username = input("Enter a new username: ")
        if new_username in self.__user_dict.keys():
            print("User has already existed! Please Try a new username!")
            return
        
        password = input("Enter your password: ")
        if password != self.__user_dict[username]:
            print("Password is incorrect!")
            return
        
        self.__user_dict[new_username] = self.__user_dict.pop(username)
        
        self.save()


    def update_password(self):

        self.reload_user()

        username = input("Enter your username: ")
        if username not in self.__user_dict.keys():
            print("Username does not exist!!")
            return
        
        password = input("Enter your old password: ")
        if password != self.__user_dict[username]:
            print("Password is incorrect!")
            return
        
        new_password = input("Enter a new password: ")
        self.__user_dict[username] = new_password

        self.save()
            

    def view_user(self):
        print("\nList of users:")
        try:
            with open(self.__user_database_file, 'r') as file:
                for index, line in enumerate(file, start=1):
                    username, password = line.strip().split(" : ") 
                    print(f"{index}. {username}")
        except FileNotFoundError:
            print("Error: User database file not found.")
        except PermissionError:
            print("Error: Permission denied to read user database.")
        except Exception as e:
            print(f"Error: Failed to view users - {e}")


    def delete_user(self):

        self.reload_user()

        delete_username = input("Enter a username to delete a user: ")

        if delete_username not in self.__user_dict.keys():
            print("Username does not exist!!")
            return
        
        password = input("Enter your password: ")
        if password != self.__user_dict[delete_username]:
            print("Password is incorrect!")
            return
        
        del self.__user_dict[delete_username] 
        self.save()
        


    def menu(self):
        while True:
            print("\n---User Management Menu---")
            print("1. Create User")
            print("2. Update User")
            print("3. View User")
            print("4. Delete User")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1: self.create_user()
            elif choice == 2: self.update_user()
            elif choice == 3: self.view_user()
            elif choice == 4: self.delete_user()
            elif choice == 5: return
            else: print("Invalid Choice!!!")


