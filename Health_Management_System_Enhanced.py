#                     @AbhijeetK1N6

import os
#Function to Store time while feeding the data
def getdate():
    import datetime
    return datetime.datetime.now()

#Function to feed the data
def func_log(name,respect):
    choice = int(input("Click 1 for DIET or 2 for EXERCISE : "))
    if choice == 2:
        entry = input("Which Exercise you have done Just Now? :- ")
        with open(f"{name}Exer.txt", "a") as f:
            f.write(str([str(getdate())]) + ":" + entry + "\n")
        print(f"Dear {name} {respect} Your Exercise has been Updated Successfully :)")
    elif choice == 1:
        entry = input("What you have eaten Just now? :- ")
        with open(f"{name}Diet.txt", "a") as f:
            f.write(str([str(getdate())]) + ":" + entry + "\n")
        print(f"Dear {name} {respect} Your Diet has been Updated Successfully :)")
#CODED BY AbhijeetK1N6
#Function to fetch the data
def func_fetch(name,respect):
    ck=input("What you want to Access??\nPress D for DIET or E for EXERCISE : ",)
    if ck == 'D':
        try:
            with open(f"{name}Diet.txt") as diet:
                print(diet.read())
        except IOError:
            print(f"Dear {name} {respect} to fetch the data, First you need to create a file and feed the data :')")
    elif ck == "E":
        try:
            with open(f"{name}Exer.txt") as exer:
                print(exer.read())
        except IOError:
            print(f"Dear {name} {respect} to fetch the data, First you need to create a file and feed the data :')")

#Driver Code
if __name__=="__main__":
    name = input("Enter your Name :- ")
    print("Enter your Gender Now")
    gender=input("Press M for Male and F for Female :- ")
    if gender=="M":
        respect="Sir"
    elif gender=="F":
        respect="Ma'am"
    k = int((input("Hello " + name + f" {respect} \nPress 1 to FEED the data and 2 to FETCH the data : ")))
    if k == 1:
        func_log(name,respect)
    elif k == 2:
        func_fetch(name,respect)
