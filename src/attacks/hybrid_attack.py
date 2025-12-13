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

        chars = string.digits  # suffix characters
        max_suffix_length = 2  # suffix length (add after wordlist) 2 letters
        attempts = 0

        try:
            with open(self.dictionary_file, "r") as f:
                for word in f:
                    word = word.strip()

                    for length in range(1, max_suffix_length + 1):
                        for combo in itertools.product(chars, repeat=length):
                            attempts += 1
                            attempt = word + "".join(combo)
                            print(f"Trying {attempt}")

                            if attempt == target_password:
                                print(f"FOUND '{username}' :{attempt} in {attempts} attempts")
                                return attempt

            return None

        except FileNotFoundError:
            print("Dictionary file not found.")
            return None
        except PermissionError:
            print("Permission denied to read dictionary file.")
            return None
