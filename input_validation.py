
import re

#user input name validation
def name_validation():
    user_input_name = str(input("Enter the name <lastname> <firstname> <middleinitial(optional)>: "))
    pattern = re.compile('^([A-Za-z]{1,25}[\'\-]?[A-Za-z]{1,25}?[\,]?) ([A-Za-z]{1,25}[\,\'\.\-]?)?([A-Za-z]{1}[\,\'\.\-]?)?$') # last-name first M
    
    if re.findall(pattern, user_input_name):
        named_list = re.search(pattern, user_input_name)  
        last_name = named_list.group(1)
        first_name = named_list.group(2)
        if named_list.group(3):
            middle_inital = named_list.group(3) 
            valid_name = {"First": first_name, "Last": last_name, "Middle": middle_inital}
        else:
            valid_name = {"First": first_name, "Last": last_name}
        return valid_name
    else: 
        print('Your input is not valid, please try again')
        name_validation()

# user input phone number validation
def phone_validation():
    user_input_phone = input('Enter phone number [+][country code][(area code) subscriber number]: ')
    pattern = re.compile('^([+][0-9]{1,2})[\(]?[0-9]{2,5}[)\- ]?[0-9\- ]{3,10}$') 

    if re.findall(pattern, user_input_phone):
        valid_phone = re.search(pattern, user_input_phone)
        return str(valid_phone.group()) 
    else:
        print('Your input is not valid, please try again.')
        phone_validation()
