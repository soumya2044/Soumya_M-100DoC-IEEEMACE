def create_new_file():
    file_name = input("Enter the name of the new file: ")
    content = input("Enter the content for the new file: ")
    with open(file_name, "w") as file:
        file.write(content)
    print(f"File '{file_name}' has been created.")

def copy_file_content():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    with open(source_file, "r") as source:
        content = source.read()
    with open(destination_file, "w") as destination:
        destination.write(content)
    print(f"Content from '{source_file}' has been copied to '{destination_file}'.")

def display_file_content():
    file_name = input("Enter the name of the file to display: ")
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"--- Content of '{file_name}' ---")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

while True:
    print("\nMenu:")
    print("1. Create a new file")
    print("2. Copy contents from file to another")
    print("3. Display a file")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        create_new_file()
    elif choice == "2":
        copy_file_content()
    elif choice == "3":
        display_file_content()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
