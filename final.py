import json
from os import path
import input_validation 

phonebook = [{"First": "Serena", "Last": "DiPenti", "Middle": "M", "Phone": "1112223333"}, {"First": "Steve", "Last": "Smith", "Middle": "J", "Phone": "1112224444"}]

filename = "phonebook.json"

if path.isfile(filename) is False:
    with open('phonebook.json', 'w') as phonebook_json_initial:
        json.dump(phonebook, phonebook_json_initial)


# add a new entry
def add_person():
    #user input validation 
    name = input_validation.name_validation()
    new_entry = name
    phone = input_validation.phone_validation()
    new_entry['Phone'] = phone
    
    #adding the new entry to the JSON document
    data = json.load(open('phonebook.json'))
    data.append(new_entry)
    with open('phonebook.json', 'w') as phonebook_json:
        json.dump(data, phonebook_json)
    
    #confirming contact has been successfully added
    print("Contact has been added to the phonebook")  #update this to include the firstname formatting

#delete an entry by name
def del_person_name():
    #user input validation
    name = input_validation.name_validation()
    
    # format {"First": "Serena", "Last": "DiPenti", "Middle": "M"}
    # assigning key values to variables
    first = name["First"]
    last = name["Last"]
    #loading json file
    data = json.load(open('phonebook.json'))
    # matching user input with existing contact data in json
    for entry in range(len(data)):
        if data[entry]["Last"] == str(last) and data[entry]["First"] == str(first):
            confirm = input(f"Would you like to delete {entry} Y/N: ") # needs to print out whole dictonary to confirm 
            if confirm == "Y":
                del data[entry]    
                with open('phonebook.json', 'w') as phonebook_json:
                    json.dump(data, phonebook_json)
                    print(f"{first} has been deleted to the phonebook")
                    break
            else:
                print("Exiting.")
                break
    else:
        print(f"{first} {last} is not in the phonebook")

#delete an entry by phone number
def del_person_phone():
    #user input validation
    phone = input_validation.phone_validation()

    data = json.load(open('phonebook.json'))
    # number = input("Enter phone number of contact you would like to delete: ")
    for entry in range(len(data)):
        if data[entry]["Phone"] == str(phone):
            confirm = input(f'Would you like to delete {phone} ? Y/N: ') # add name of who the number belongs to
            if confirm == "Y":
                del data[entry]    
                with open('phonebook.json', 'w') as phonebook_json:
                    json.dump(data, phonebook_json)
                    print(f"{phone} has been deleted to the phonebook")
                    break
    else:
        print(f"{phone} is not in the phonebook")

#list all current saved entries
def list_entries():
    with open('phonebook.json') as phonebook_json:
        phonebook_list = json.load(phonebook_json)
        for entry in phonebook_list:
            print(entry)


while True:
    print("Welcome to the phonebook!")
    print("1 -- Add an entry")
    print("2 -- Delete an entry by name")
    print("3 -- Delete an entry by number")
    print("4 -- List all entries")
    print("5 -- Exit")
    choice = input("Choose a number from the options above: ")

    if choice == "1":
        add_person()
    elif choice == "2":
        del_person_name()
    elif choice == "3":
        del_person_phone()
    elif choice == "4":
        list_entries()
    elif choice == "5":
        break
    else:
        print("Error: Invalid option. Please select from the list.")

