import json
from os import path

phonebook = [{"Name": "Serena", "Phone": "1112223333"}, {"Name":"Steve", "Phone": "0009998888"}]

filename = "phonebook.json"

if path.isfile(filename) is False:
    with open('phonebook.json', 'w') as phonebook_json_initial:
        json.dump(phonebook, phonebook_json_initial)


def add_person():
    name = input("Enter the persons full name: ")
    phone_number = input("Enter the persons phone number: ")
    new_entry = {"Name": name, "Phone": phone_number}
    data = json.load(open('phonebook.json'))
    data.append(new_entry)
    with open('phonebook.json', 'w') as phonebook_json:
        json.dump(data, phonebook_json)
    print(f"{name} has been added to the phonebook")

def del_person_name():
    data = json.load(open('phonebook.json'))
    name = input("Enter name of contact you would like to delete: ")
    for entry in range(len(data)):
        if data[entry]["Name"] == str(name):
            del data[entry]    
            with open('phonebook.json', 'w') as phonebook_json:
                json.dump(data, phonebook_json)
                print(f"{name} has been deleted to the phonebook")
                break
    else:
        print(f"{name} is not in the phonebook")


def del_person_phone():
    data = json.load(open('phonebook.json'))
    number = input("Enter phone number of contact you would like to delete: ")
    for entry in range(len(data)):
        if data[entry]["Phone"] == str(number):
            del data[entry]    
            with open('phonebook.json', 'w') as phonebook_json:
                json.dump(data, phonebook_json)
                print(f"{number} has been deleted to the phonebook")
                break
    else:
        print(f"{number} is not in the phonebook")

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

