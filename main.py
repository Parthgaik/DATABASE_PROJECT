# Imports
import sqlite3

# Functions of code start here
####################################################################


# Connection function to prevent repeated code

def connection():
    '''connection and cursor connect to reduce repeated code'''
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    return connection, cursor


def show_all_cards():
    '''Shows all the cards'''
    conn, cursor = connection()
    cards = cursor.execute("SELECT Name FROM Card;").fetchall()
    print("Here are all cards")
    for card in cards:
        print(card[0])
# Basic query and print statement to get all the cards and print the first index of the query(Name)

def cards_by_rarity():
    '''Shows all of the cards based on the rarity input by the user'''
    conn, cursor = connection()
    rarity = input('please enter id of rarity card you would like. 1 for Common, 2 for Rare, 3 for Epic and 4 for Legendary ')
    acceptable_rarity = ["1", "2", "3", "4",]  # Acceptable inputs for this function
    while True:
        if rarity not in acceptable_rarity:
            rarity = input("Please enter a valid input ")
        else:
            if not rarity.isnumeric():
                rarity = input("Please enter a valid input ") # Error prevention code
            else:
                print("Here are all the cards by their rarity")
                cardrarity = cursor.execute("SELECT Name FROM Card WHERE Rarity = ?", (rarity,)).fetchall()
                for card in cardrarity:
                    print(card[0])
                break
# After all the error prevention, the correct input is passed through the query and printed

def cards_by_elixir():
    '''Shows all of the cards based on the elixir input by the user'''
    conn, cursor = connection()
    elixir = input('Please enter the elixir of card you want from 1 - 10 ')
    acceptable_elixir = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # Acceptable inputs for this function
    while True:
        if elixir not in acceptable_elixir:
            elixir = input("Please enter a valid input ")
        else:
            if not elixir.isnumeric():
                elixir = input("Please enter a valid input ") #Error prevention code
            else:
                print("Here are all the cards with selected elixir")
                cardelixir = cursor.execute("SELECT Name, Elixir FROM Card Where Elixir = ?", (elixir,)).fetchall()
                for card in cardelixir:
                    print(card[0])
                break
# After all the error prevention, the correct input is passed through the query and printed

def class_of_cards():
    '''Shows all of the cards based on the class of card input by the user'''
    conn, cursor = connection()
    # Print out id and type from type table in db (START)
    idlist = []
    cardtype = []
    id_type = cursor.execute("SELECT * FROM Type;").fetchall()
    for i in id_type:  # Get the first and second values in the query and store them in the lists (START)
        id = i[0]
        idlist.append(id)
    for i in id_type:
        id = i[1]
        cardtype.append(id)
    for x in range(len(idlist)):
        id = idlist[x]
        cardclass = cardtype[x]
        print(f"{id} {cardclass}")  # Get the first and second values in the query and store them in the lists and print them (END)
        # Print out id and type from type table in db (END)
    cofc = input('Please enter id of all the cards you would like to see ')
    acceptable_class = ["1", "3", "4"]  # Acceptable inputs for this function
    while True:
        if cofc not in acceptable_class:
            cofc = input("Please enter a valid input ")
        else:
            if not cofc.isnumeric():
                cofc = input("Please enter a valid input ") #Error prevention code
            else:
                print("Here are all the cards with selected class")
                cardclass = cursor.execute("SELECT Name FROM Card WHERE TypeID = ?", (cofc,)).fetchall()
                for card in cardclass:
                    print(card[0])
                break
# After all the error prevention, the correct input is passed through the query and printed

def card_counters():
    '''Shows the counter of the card the user inputs by first displaying all of the cards'''
    conn, cursor = connection()
    # Selecting two collums from the cards table so the user can see what id relates to which card (START)
    idlist = []
    cardnames = []
    cards = cursor.execute("SELECT id, Name FROM Card").fetchall()
    for i in cards:
        x = i[0]
        idlist.append(x)
    for i in cards:
        x = i[1]
        cardnames.append(x)
    for x in range(len(idlist)):
        id = idlist[x]
        names = cardnames[x]
        print(f"{id} {names}")
    # Selecting two collums from the cards table so the user can see what id relates to which card (END)
    counter = input('Please enter the counter of card you want from 1 - 104 ')
    acceptable_counters = [x for x in range(1, 105)]
    acceptable_counters_1 = []
    unacceptablecounter = ["74", "76", "77", "78", "79", "80", "82", "83", "85", "86", "87", "88", "89", "91"]
    for i in acceptable_counters:
        i = str(i)
        acceptable_counters_1.append(i)
        # Converting the input to a string and storing in new list ready to be checked in upcoming code
    while True:
        if counter in unacceptablecounter:
            print("Sorry, that card does not have a counter")
            counter = input('Please enter the counter of card you want from 1 - 104 ')
        else:
            if counter not in acceptable_counters_1:
                counter = input("Please enter a valid input ")
            else:
                if not counter.isnumeric():
                    counter = input("Please enter a valid input ")  # Error prevention code
                else:
                    print("Here is the selected card with its counter")
                    card = cursor.execute("SELECT Card.Name, Counters.CounterID FROM Card JOIN Counters ON Card.id = Counters.id WHERE CardID = ?", (counter,)).fetchall()
                    card = card[0][1]
                    cardcounter = cursor.execute("SELECT Counters.CounterID, Card.Name FROM Card JOIN Counters ON Card.id = Counters.CounterID WHERE CounterID = ?", (card,)).fetchall()
                    cardcounter = cardcounter[0][1]
                    print(cardcounter)
                    break
# After all the error prevention, the correct input is passed through the query and printed

# Start Of Program
#######################################################


no = "no"
print("Hello! Welcome to my program")
while True:
    what = input('press 1 to see all cards, 2 to see cards by rarity, 3 to see cards by elixir, 4 to see class of cards and 5 to see card counters.\nHowever, if you wish to exit the program, please enter "no" ')
    if what == no:
        print("Thank you for your time")
        break
    # Allow the user to exit out of the program
    else:
        pass
    if what.isnumeric():
        what = int(what)
        # If valid inputs are entered, run above functions
        if what > 5 or what < 1:
            print("please Enter Valid input")
        if what == 1:
            show_all_cards()
        if what == 2:
            cards_by_rarity()
        if what == 3:
            cards_by_elixir()
        if what == 4:
            class_of_cards()
        if what == 5:
            card_counters()
    else:
        print("Please Enter Valid input")
