#                     @AbhijeetK1N6
def getdate():
    import datetime
    return datetime.datetime.now()

def func_log():
    choice = int(input("Click 1 for DIET or 2 for EXERCISE : "))
    if choice == 2:
        entry = input("Enter Your Exercise : ")
        if name == "USER_1_":
            with open("USER_1_Exer.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        elif name == "USER_2_":
            with open("USER_2_Exer.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        elif name == "USER_3_":
            with open("USER_3_Exer.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        print("Your Exercise Updated Successfully")
    elif choice == 1:
        entry = input("Enter your Diet : ")
        if name == "USER_1_":
            with open("USER_1_Diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        elif name == "USER_2_":
            with open("USER_2_Diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        elif name == "USER_3_":
            with open("USER_3_Diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + entry + "\n")
        print("Your Diet Updated Successfully")

def func_fetch():
    print("What you want to Access??\nPress D for DIET or E for EXERCISE : ")
    ck = input()
    if name == "USER_1_" and ck == 'D':
        with open("USER_1_Diet.txt") as diet:
            print(diet.read())
    elif name == "USER_1_" and ck == "E":
        with open("USER_1_Exer.txt") as exer:
            print(exer.read())
    elif name == "USER_2_" and ck == 'D':
        with open("USER_2_Diet.txt") as diet:
            print(diet.read())
    elif name == "USER_2_" and ck == "E":
        with open("USER_2_Exer.txt") as exer:
            print(exer.read())
    elif name == "USER_3_" and ck == 'D':
        with open("USER_3_Diet.txt") as diet:
            print(diet.read())
    elif name == "USER_3_" and ck == "E":
        with open("USER_3_Exer.txt") as exer:
            print(exer.read())

name = input("Enter your Name :- ")
k = int((input("Hello Mr. " + name + "\nPress 1 to FEED the data and 2 to FETCH the data : ")))
if k == 1:
    func_log()
elif k == 2:
    func_fetch()
