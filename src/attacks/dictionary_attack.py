class DictionaryAttack:
    def __init__(self, user_manager, dictionary_file):
        self.user_manager = user_manager #instance of UserManagement assigned to user_manager
        self.dictionary_file = dictionary_file #path of dictionary_list.txt

    def crack_user(self, username):
        self.user_manager.reload_user() #get user from database file into a private dictionary
        users = self.user_manager.get_user() #assign the private dictionary of user_manager to users

        if username not in users:
            print("User not found.") #to find if usernames is in users or not (check by using the dictionary of users)
            return None

        target_password = users[username] #assgin value of users which is a password of username into target_password

        try:
            with open(self.dictionary_file, "r") as f:
                attempt = 0
                
                for word in f:
                    attempt += 1
                    word = word.strip() #remove '\n' after each word
                    print(f"Trying {word}") #print trying password
                    if word == target_password:
                        print(f"FOUND '{username}' : {word} in {attempt} attempts")
                        return word

            return None

        except FileNotFoundError:
            print("Dictionary file not found.")
            return False
        
