def list_operations():
    try:
        user_list = input("Enter a list of numbers separated by spaces: ").split()
        user_list = [int(item) for item in user_list]
    except ValueError:
        print("Please enter a valid list of numbers.")
        return

    while True:
        print("\nOptions:")
        print("1. Sort the list")
        print("2. Search for an element in the list")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            user_list.sort()
            print(f"Sorted list: {user_list}")
        elif choice == 2:
            try:
                element = int(input("Enter the element to search for: "))
                if element in user_list:
                    print(f"Element {element} found at index {user_list.index(element)}.")
                else:
                    print(f"Element {element} not found in the list.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

list_operations()
