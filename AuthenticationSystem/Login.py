import json
import string


'''userName:string,password:string)'''

def loginValidation(userName:string,password:string):

    with open("users_data.json", 'r+') as file:
        file_data = json.load(file)
        userList=file_data["users_details"]
        # print(type(userList))
        # print(userList)
        for user in userList:
            if user["FirstName"]==userName and user["Password"]==password:
                return True
        return False





def login():
    print("_____Login Page______")
    userName=input("Enter your name: ")
    password=input("Enter your password: ")
    response=loginValidation(userName,password)
    if response:
        print("Login Successfuly")

    else:
        print("try Agine")
        login()

