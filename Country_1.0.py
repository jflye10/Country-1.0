# Joshua Flye, CIS261, Country

def display_menu():
    """
    Displays the program heading and menu options.
    """
    print("The Country List Program\n")
    print("COMMAND MENU")
    print("view - View a country")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit a program")

def create_country_dict():
    """
    Creates a dictionary of countries with a minimum of three entries.
    
    Returns:
        dict: A dictionary of country codes and names.
    """
    country_dict = {
        "US": "United States",
        "CA": "Canada",
        "GB": "United Kingdom"
    }
    return country_dict

def view_country(country_dict):
    """
    Displays all country codes and allows the user to view a country codes and names.
    
    Args:
        country_dict (dict): The dictionary of country codes and names.
    """
    print("Country Codes:")
    for code in country_dict:
        print(code, end=" ")
    print() # Print a newline

    code = input("Enter country code:  ").upper() # COnvert to uppercase for consistency.
    if code in country_dict:
        print(f"Country name: country_dict[country_dict[code]")
    else:
        print("Invalid country code.")
def add_country(country_dict):
    """
    Adds a country to the dictionary.

    Args:
        country_dict (dict): The dictionary of country codes and names.
    """
    code = input("Enter country code: ").upper() # Convert to uppercase for consistency.
    name = input("Enter country name: ")
    if code in country_dict:
        print("Country code already exists.")
    else:
        country_dict[code] = name
        print(f"{name} was added.")

def delete_country(country_dict):
    """
    Deletes a country to the dictionary.

    Args:
        country_dict (dict): The dictionary of country codes and names.
    """
    code = input("Enter country code: ").upper() # COnvert to uppercase for consistency.
    if code in country_dict:
        del country_dict[code]
        print(f"Country [code] was deleted.") # changed from name to code
    else:
        print("Invalid country code.")
def get_command():
    """
    Gets the user's command, handling potential EOFError.

    Returns:
        str: The command entered by the user, or empty string on error.
    """
    try:
        command = input("Command: ").lower() # Make input lowercase
        return command
    except EOFError:
        print("\nEnd of iput reached. Exiting.")
        return "" # Return an empty string to signal exit
def main():
    """
    Main function to run the program.
    """
    display_menu()
    country_dict = create_country_dict()

    while True:
        command = get_command()
        if not command: # Exit if command is empty (from EOFError)
            break
        if command == "view":
            view_country(country_dict)
        elif command == "add":
            add_country(country_dict)
        elif command == "del":
            delete_country(country_dict)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()

