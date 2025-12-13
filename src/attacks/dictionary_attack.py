class DictionaryAttack:
    def __init__(self, user_manager, dictionary_file):
        self.user_manager = user_manager
        self.dictionary_file = dictionary_file

    def crack_user(self, username):
        self.user_manager.reload_user()
        users = self.user_manager.get_user()

        if username not in users:
            print("User not found.")
            return None

        target_password = users[username]

        try:
            with open(self.dictionary_file, "r") as f:
                attempt = 0
                
                for word in f:
                    attempt += 1
                    word = word.strip()
                    print(f"Trying {word}")
                    if word == target_password:
                        print(f"FOUND '{username}' : {word} in {attempt} attempts")
                        return word

            return None

        except FileNotFoundError:
            print("Dictionary file not found.")
            return None
        except PermissionError:
            print("Permission denied to read dictionary file.")
            return None
