import re
import json

def registrationValidation():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        firstName = input("Enter your first name==> ")
        if not (firstName.isalpha()):
            print("invalid name")
        else:
            break
    while True:
        lastName = input("Enter your last name==> ")
        if not (lastName.isalpha()):
                print("invalid name")
        else:
            break
    while True:
        email = input("Enter you email==> ")
        if not (re.fullmatch(regex, email)):
            print("inalid Email")
        else:
            break
    while True:
        phone=input("Enter your phone number")
        if not (re.match("^01[0125][0-9]{8}$",phone)):
            print("inalid phone")
        else:
            break
    password = input("Enter your password => ")
    confirmPassword = input("Enter confirm Password ==>")
    while True:
        if(confirmPassword != password):
            print("Pasword And Comfirm passsword should be Equuleus")
            confirmPassword = input("Enter confirm Password ==>")
        else:
            break

    userData={'FirstName':firstName,'LastName':lastName,'Email':email,'Phone':phone,'Password':password}

    return  userData


def registration():
    print("_____Registration page______")
    with open("users_data.json", 'r+') as file:

        file_data = json.load(file)
        file_data["users_details"].append(registrationValidation())
        file.seek(0)
        json.dump(file_data, file, indent=4)



