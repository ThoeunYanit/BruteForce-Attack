import itertools
import string


class SimpleBruteForceAttack:

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def crack_user(self, target_user, char = string.ascii_lowercase + string.ascii_uppercase + string.digits +string.punctuation):
        chars = char
        attempt_count = 0

        try:
            status = self.user_manager.reload_user() #incase file path is wrong so will get False or True/ to reload data from database into a private dictionary
            if status is False:
                return False
            
            users = self.user_manager.get_user() #to acceses the private dictionary

        except Exception as e:
            print(f"ERROR: {e}")
            return False

        if target_user not in users:
            print("User not found")
            return None

        target_password = users[target_user]


        # we use length for the amount of letters that can be used during the operation to bruteforce attack the user
        for length in range(1, len(target_password) + 1): #len(target_password) + 1 because we start from 1 so n + 1 

            #itertools.product: word from chars (uppercase, lowercase, digits, punctuation) will become elements stored in tuple each loop
            #repeat is for setting the digit of letter
            #since itertools.product provide tuple, we use ""join(combo) to join those elements in tuple together to get a string of word
            for combo in itertools.product(chars, repeat=length): 
                attempt_count += 1
                attempt = "".join(combo)
                print(f"Trying {attempt}")

                if attempt == target_password:
                    print(f"FOUND password '{target_password}' in {attempt_count} attempts")
                    return target_password

        return None

class CountTrackingSimpleBruteForce:

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def crack_user(self, target_user):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits +string.punctuation
        attempt_count = 0

        try:
            self.user_manager.reload_user()
            users = self.user_manager.get_user()

        except Exception as e:
            print(f"ERROR: {e}")
            return False

        if target_user not in users:
            print("User not found")
            return None

        target_password = users[target_user]

        #process is the same as above but with a slight difference. instead of printing each word, it prints attempt_count
        for length in range(1, len(target_password) + 1):
            for combo in itertools.product(chars, repeat=length):
                attempt_count += 1
                attempt = "".join(combo)

                if attempt_count % 1000 == 0: #print attempt_count each time attempt_count % 1000 equal to 0
                    print(f"Attempts: {attempt_count}")

                if attempt == target_password:
                    print(f"FOUND password '{target_password}' in {attempt_count} attempts")
                    return target_password

        return None
