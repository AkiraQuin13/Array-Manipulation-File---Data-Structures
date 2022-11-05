# Array Variables
# Programmed By: Charina Vallecera
# BSCOE 2-2

print("\n<<<<<<<< ARRAY MANIPULATION >>>>>>>>\n")
listed = [3, 8, 13, 18, 21, 24, 28, 32, 99, 100]


def main():
    print("<<<<<<<<<<<<< MENU >>>>>>>>>>>>>")
    print("1 -> Add an element")
    print("2 -> Insert an element")
    print("3 -> Modify an element")
    print("4 -> Delete an element")
    print("5 -> Arrange in ascending order")
    print("6 -> Arrange in descending order")
    print("7 -> Exits the program")


def add():
    while True:
        print("\n<<<<<<<<<<<< ADD >>>>>>>>>>>>>>")
        added = int(input("Add the number: "))
        listed.append(added)
        print("New list: ", listed)
        print("The number has been added successfully!")

        addAgain = input("\nWould you like to add another element [ yes / no ] : ")
        if addAgain.casefold() == "yes":
            add()
        elif addAgain.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            runProg()


def insert():
    while True:
        print("\n<<<<<<<<<<<< INSERT >>>>>>>>>>>>>>")
        inserts = int(input("Insert the number: "))
        index = int(input("Enter the placement of the number: "))
        listed.insert(index, inserts)
        print("New list: ", listed)
        print("The number has been inserted successfully!")

        insertAgain = input("\nWould you like to insert another element [ yes / no ] : ")
        if insertAgain.casefold() == "yes":
            insert()
        elif insertAgain.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            runProg()


def modify():
    while True:
        print("\n<<<<<<<<<<<< MODIFY >>>>>>>>>>>>>>")
        index = int(input("Enter the number placement: "))
        listed.pop(index)
        modified = int(input("Enter the number to be modify: "))
        listed.insert(index, modified)
        print("New list: ", listed)
        print("The number has been modified successfully!")

        modifyAgain = input("\nWould you like to modify another element [ yes / no ] : ")
        if modifyAgain.casefold() == "yes":
            modify()
        elif modifyAgain.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            runProg()


def delete():
    while True:
        print("\n<<<<<<<<<<<< DELETE >>>>>>>>>>>>>>")
        print(listed)
        deleted = int(input("Enter the number to be deleted: "))
        listed.pop(deleted)
        print("New list: ", listed)
        print("The number has been deleted successfully!")

        deleteAgain = input("\nWould you like to delete another element [ yes / no ] : ")
        if deleteAgain.casefold() == "yes":
            delete()
        elif deleteAgain.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            runProg()


def ascending():
    while True:
        print("\n<<<<<<<<<<<< ASCENDING >>>>>>>>>>>>>>")
        listed.sort()
        print("New list: ", listed)

        again = input("\nWould you like to return to main menu? [ yes / no ] : ")
        if again.casefold() == "yes":
            runProg()
        elif again.casefold() == "no":
            print("\nThank You for using the Program!")


def descending():
    while True:
        print("\n<<<<<<<<<<<< DESCENDING >>>>>>>>>>>>>>")
        listed.sort()
        listed.reverse()
        print("New list: ", listed)

        again = input("\nWould you like to return to main menu? [ yes / no ] : ")
        if again.casefold() == "yes":
            runProg()
        elif again.casefold() == "no":
            print("\nThank You for using the Program!")
            exit()


def exits():
    while True:
        print("\n<<<<<<<<<<<< EXIT >>>>>>>>>>>>>>")
        exitOption = input("Are you sure you want to close thE program? [ yes / no ] : ")
        if exitOption.casefold() == "yes":
            print("Thank You for using the Program!")
            print("Bye!")
            exit()
        elif exitOption.casefold() == "no":
            runProg()
        else:
            print("Invalid Input! Please try again!")
            continue


def runProg():
    while True:
        main()
        mainOption = int(input("Choose the number corresponding to your choice: "))

        if mainOption in (1, 2, 3, 4, 5, 6, 7):
            if mainOption == 1:
                add()
            elif mainOption == 2:
                insert()
            elif mainOption == 3:
                modify()
            elif mainOption == 4:
                delete()
            elif mainOption == 5:
                ascending()
            elif mainOption == 6:
                descending()
            elif mainOption == 7:
                exits()
        else:
            print("Invalid Input! Choose a number on the menu and try again!")
            continue

while True:
    runProg()

