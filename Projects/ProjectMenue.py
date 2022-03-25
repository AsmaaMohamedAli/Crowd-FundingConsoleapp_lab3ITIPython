import ListProject
def projectMenue():
    print("1:Enter 1 To list Project: ")
    print("2:Enter 2 To add project: ")
    print("3: Enter 3 To Edit project: ")
    print("4: Enter 3 To Delete project: ")


    while True:
        choose=input("Enter your choice ==> ")
        if choose.isdigit():
            choose=int(choose)
            if choose ==1:
                ListProject.list()
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