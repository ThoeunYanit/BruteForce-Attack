import itertools
import string


class SimpleBruteForce:

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
            return None

        if target_user not in users:
            print("User not found")
            return None

        target_password = users[target_user]

        for length in range(1, len(target_password) + 1):
            for combo in itertools.product(chars, repeat=length):
                attempt_count += 1
                attempt = "".join(combo)
                print(f"Trying {attempt}")

                if attempt == target_password:
                    print(f"FOUND password '{target_password}' in {attempt_count} attempts")
                    return attempt_count

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
            return None

        if target_user not in users:
            print("User not found")
            return None

        target_password = users[target_user]

        for length in range(1, len(target_password) + 1):
            for combo in itertools.product(chars, repeat=length):
                attempt_count += 1
                attempt = "".join(combo)

                if attempt_count % 1000 == 0:
                    print(f"Attempts: {attempt_count}")

                if attempt == target_password:
                    print(f"FOUND password '{target_password}' in {attempt_count} attempts")
                    return attempt_count

        return None
