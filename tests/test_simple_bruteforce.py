
from src.users.user_management import UserManagement
from src.attacks.simple_bruteforce_attack import SimpleBruteForce, CountTrackingSimpleBruteForce

def create_test_user_file():
    with open("test_users.txt", "w") as f:
        f.write("alice : ab\n")
        f.write("bob : aa\n")


def test_simple_bruteforce():
    print("\n--- Testing SimpleBruteForce ---")

    create_test_user_file()
    um = UserManagement("test_users.txt")
    attack = SimpleBruteForce(um)

    result = attack.crack_user("alice")

    if result is not None:
        print("PASS: SimpleBruteForce cracked password")
    else:
        print("FAIL: SimpleBruteForce failed")


def test_count_tracking():
    print("\n--- Testing CountTrackingSimpleBruteForce ---")

    um = UserManagement("test_users.txt")
    attack = CountTrackingSimpleBruteForce(um)

    result = attack.crack_user("bob")

    if result is not None:
        print("PASS: CountTrackingSimpleBruteForce cracked password")
    else:
        print("FAIL: CountTrackingSimpleBruteForce failed")


def test_user_not_found():
    print("\n--- Testing User Not Found ---")

    um = UserManagement("test_users.txt")
    attack = SimpleBruteForce(um)

    result = attack.crack_user("charlie")

    if result is None:
        print("PASS: Correctly handled missing user")
    else:
        print("FAIL: Should not crack non-existing user")


if __name__ == "__main__":
    test_simple_bruteforce()
    test_count_tracking()
    test_user_not_found()

    print("\nALL MANUAL TESTS FINISHED")
