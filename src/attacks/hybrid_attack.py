import itertools
import string


class HybridAttack:
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

        chars = string.digits + string.punctuation  # suffix characters
        max_suffix_length = 3  # suffix length (add after wordlist) 3 letters
        attempt_count = 0


        #the process is the same as dictionary + simple bruteforce with a slight difference
        #we use word from dictionary and add suffix  (add letters after the word)
        #in this case we only use length of suffix = 3, so for instance, we expect password to look like this 'word123' which means 'word' is taking from the dictionary and '123' is being added using itertools.product
        try:
            with open(self.dictionary_file, "r") as f:
                for word in f:
                    word = word.strip()

                    for length in range(1, max_suffix_length + 1):
                        for combo in itertools.product(chars, repeat=length):
                            attempt_count += 1
                            attempt = word + "".join(combo)
                            print(f"Trying {attempt}")

                            if attempt == target_password:
                                print(f"FOUND '{username}' :{attempt} in {attempt_count} attempts")
                                return attempt

            return None

        except FileNotFoundError:
            print("Dictionary file not found.")
            return False
        
