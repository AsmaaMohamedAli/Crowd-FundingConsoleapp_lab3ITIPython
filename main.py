from AuthenticationSystem import Login,registration

def mainMenue():
    print("1:Enter 1 for login")
    print("2:Enter 2 for Registration")
    print("3: Enter 3 to exit")
    while True:
        choose=input("Enter your choice ==> ")
        if choose.isdigit():
            choose=int(choose)
            if choose ==1:
                Login.login()
            elif choose==2:
                registration.registration()
            elif choose==3:
                print(" !! you will exit from applocation")
                break
            else:
                print("invalid choice")
        else:
            print("Enter numeric choice")

mainMenue()

