from users.user_management import UserManagement

import itertools
import string

class HybridAttack:
    def __init__(self, user_database_file):
        self.user_manager = user_database_file

    def crack(self):
        try:
            self.user_manager.reload_user()
        except FileNotFoundError:
            print("Error: User database file not found.")
            return
        except PermissionError:
            print("Error: Permission denied to access user database.")
            return
        except Exception as e:
            print(f"Error: Failed to load user database - {e}")
            return

        users = self.user_manager.get_user() ##this is a dictionary

        target_user = input("Enter a target username: ")

        if target_user not in users:
            print("User not found!")
            return 
        
        target_password = users[target_user]

        dictionary_file = "C:\\Project Python Year2\\BruteForce-Attack\\data\\user_database.txt"
        chars = string.digits + string.punctuation  ## 42characters ### N^L (N=character, L = length) ## 42^3 = 74088
        max_suffix_length = 3  ##password123 , suffix length = 3 (123) added after passwd
        attempt_count = 0

        try:
            with open(dictionary_file, 'r') as wordlist:
                for word in wordlist:
                    word = word.strip()
                    for length in range(1, max_suffix_length+1):
                        for combo in itertools.product(chars, repeat=length):
                            attempt_count += 1
                            attempt = word + "".join(combo)
                            print(f"Trying {attempt}")

                            # if attempt_count % 10000 == 0:
                            #     print(f"Attempt {attempt_count}")

                            if target_password == attempt:
                                print(f"\nPASSWORD FOUND ► {target_password}")
                                print(f"User: {target_user}")
                                print(f"Attempts: {attempt_count}")
                                return
                
                print(f"\nPassword not found after {attempt_count} attempts.")
                
        except FileNotFoundError:
            print("Error: Dictionary file not found.")
        except PermissionError:
            print("Error: Permission denied to read dictionary file.")
        except Exception as e:
            print(f"Error: Failed to read dictionary file - {e}")
                    


if __name__ == '__main__' :
    try:
        user = UserManagement("C:\\Project Python Year2\\BruteForce-Attack\\data\\user_database.txt")
        ha = HybridAttack(user)
        ha.crack()
    except Exception as e:
        print(f"Error: Program initialization failed - {e}")
            

        



