#Carys Lewelling

grocery = [] #Empty list

#Initial
def view():
    print("This is your grocery list: " + str(grocery))
def add():
    y = input("What do you want to add?")
    grocery.append(y)
    print("Item was added to list: " + str(grocery))
def remove():
    z = input("Which item do you want to remove from your list? Enter the specific item:")
    grocery.remove(z)
    print("This is your updated grocery list: " + str(grocery))
def alphabet():
    grocery.sort()
    print("This is your grocery list in order: " + str(grocery))
def count():
    a = len(grocery)
    print("There are " + str(a) + " items in your list")
def list():
    print("Welcome to your digital grocery list!")
    while True:
        try:
            x = int(input("Do you want to...\n1. Veiw your grocery list\n2. Add an item\n3. Remove a task from list\n4. Sort list alphabetically\n5. count the number of items in list\n6. exit the program?\nEnter a number (1-6)"))
            if x == 1:
                view()
            elif x == 2:
                add()
            elif x == 3:
                remove()
            elif x == 4:
                alphabet()
            elif x == 5:
                count()
            elif x == 6:
                print("goodbye")
                break
        except:
            print("Invalid. You must enter a number 1-6!!")

#Main
list()

