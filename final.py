import json
from os import path
import input_validation 

phonebook = [{"First": "Serena", "Last": "DiPenti", "Middle": "M", "Phone": "+1(555) 555-5555"}, {"First": "Steve", "Last": "Smith", "Middle": "J", "Phone": "+1(444) 444-5555"}]

filename = "phonebook.json"

if path.isfile(filename) is False:
    with open('phonebook.json', 'w') as phonebook_json_initial:
        json.dump(phonebook, phonebook_json_initial)


# add a new entry
def add_person():
    #user input validation 
    name = input_validation.name_validation()
    # format {"First": "Serena", "Last": "DiPenti", "Middle": "M"}

    phone = input_validation.phone_validation()
    name['Phone'] = phone
    first_name = name["First"]
    
    #adding the new entry to the JSON document
    data = json.load(open('phonebook.json'))
    # data.append(name)
    # with open('phonebook.json', 'w') as phonebook_json:
    for entry in range(len(data)):
        if data[entry]["Phone"] == str(phone):
            print("This number already exists in the phonebook")
            break
    else: 
        with open('phonebook.json', 'w') as phonebook_json:
                data.append(name)
                json.dump(data, phonebook_json)
                print(f"{first_name} has been added to the phonebook")
    

#delete an entry by name
def del_person_name():
    #user input validation
    name = input_validation.name_validation()
    
    # format example {"First": "Serena", "Last": "DiPenti", "Middle": "M"}
    # assigning user input key values to string variables
    first = str(name["First"])
    last = str(name["Last"])

    #loading json file
    data = json.load(open('phonebook.json'))
    # matching user input with existing entry data in json
    for entry in range(len(data)):
        if str(data[entry]["Last"]).lower() == last.lower() and str(data[entry]["First"]).lower() == first.lower():
            phone = data[entry]["Phone"]
            confirm = input(f"Would you like to delete {first} {last} - {phone} Y/N: ") 
            if confirm == "Y":
                del data[entry]    
                with open('phonebook.json', 'w') as phonebook_json:
                    json.dump(data, phonebook_json)
                    print(f"{first} has been deleted from the phonebook")
                    break
            else:
                print("Exiting.")
                break
    else:
        print(f"{first} {last} is not in the phonebook")
        search_option = input("Would you like to try searching by phone number? Y/N: ")
        if search_option == "Y":
            del_person_phone()
        else:
            print("Exiting")


#delete an entry by phone number
def del_person_phone():
    #user input validation
    phone = input_validation.phone_validation()

    data = json.load(open('phonebook.json'))
    # number = input("Enter phone number of contact you would like to delete: ")
    for entry in range(len(data)):
        if data[entry]["Phone"] == str(phone):
            f_name = data[entry]["First"]
            l_name = data[entry]["Last"]
            confirm = input(f'Would you like to delete {f_name} {l_name} - {phone} ? Y/N: ') # add name of who the number belongs to
            if confirm == "Y":
                del data[entry]    
                with open('phonebook.json', 'w') as phonebook_json:
                    json.dump(data, phonebook_json)
                    print(f"{phone} has been deleted from the phonebook")
                    break
    else:
        print(f"{phone} is not in the phonebook")
        search_option_1 = input("Would you like to try searching by phone number? Y/N: ")
        if search_option_1 == "Y":
            del_person_name()
        else:
            print("Exiting")

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

