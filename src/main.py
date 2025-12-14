from users.user_management import UserManagement
from attacks.simple_bruteforce_attack import SimpleBruteForceAttack, CountTrackingSimpleBruteForce
from attacks.dictionary_attack import DictionaryAttack
from attacks.hybrid_attack import HybridAttack

#this is just a design title
def print_title():
    RED = "\033[91m" #91m is for Red color
    RESET = "\033[0m"

    title = r"""
██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗ 
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝                                                        

███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
█████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝

 █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
███████║   ██║      ██║   ███████║██║     █████╔╝ 
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""
    
    print(RED + title + RESET)


def main():

    print_title()

    user_database_file = "data/user_database.txt"
    dictionary_file = "data/dictionary_list.txt"

    # Initialize user management
    um = UserManagement(user_database_file)

    # Initialize attacks
    simple_attack = SimpleBruteForceAttack(um)
    count_attack = CountTrackingSimpleBruteForce(um)
    dict_attack = DictionaryAttack(um, dictionary_file)
    hybrid_attack = HybridAttack(um, dictionary_file)

    while True:
        print("\n--- Brute Force Attack Simulator Menu ---")
        print("1. User Management")
        print("2. Simple Brute Force Attack")
        print("3. Simple Brute Force (With Attempt Count)")
        print("4. Dictionary Attack")
        print("5. Hybrid Attack")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                um.menu()

            elif choice == 2:
                username = input("Enter target username: ")
                simple_attack.crack_user(username)
                

            elif choice == 3:
                username = input("Enter target username: ")
                count_attack.crack_user(username)
                

            elif choice == 4:
                username = input("Enter target username: ")
                dict_attack.crack_user(username)
                

            elif choice == 5:
                username = input("Enter target username: ")
                hybrid_attack.crack_user(username)
                

            elif choice == 6:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice! Please select 1-6.")

        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
