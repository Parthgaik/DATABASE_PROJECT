# Imports
import sqlite3

# Functions of code start here
####################################################################


# Connection function to prevent repeated code

def connection():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    return connection, cursor


def show_all_cards():
    conn, cursor = connection()
    cards = cursor.execute("SELECT Name FROM Card;").fetchall()
    print("Here are all cards")
    for card in cards:
        print(card[0])


def cards_by_rarity():
    conn, cursor = connection()
    rarity = input('please enter id of rarity card you would like. 1 for Common, 2 for Rare, 3 for Epic and 4 for Legendary ')
    acceptable_rarity = ["1", "2", "3", "4",] # Acceptable inputs for this function
    while True:
        if rarity not in acceptable_rarity:
            rarity = input("Please enter a valid input ")
        else:
            if not rarity.isnumeric():
                rarity = input("Please enter a valid input ")
            else:
                print("Here are all the cards by their rarity")
                cardrarity = cursor.execute("SELECT Name FROM Card WHERE Rarity = ?", (rarity,)).fetchall()
                for card in cardrarity:
                    print(card[0])
                break


def cards_by_elixir():
    conn, cursor = connection()
    elixir = input('Please enter the elixir of card you want from 1 - 10 ')
    acceptable_elixir = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] # Acceptable inputs for this function
    while True:
        if elixir not in acceptable_elixir:
            elixir = input("Please enter a valid input ")
        else:
            if not elixir.isnumeric():
                elixir = input("Please enter a valid input ")
            else:
                print("Here are all the cards with selected elixir")
                cardelixir = cursor.execute("SELECT Name, Elixir FROM Card Where Elixir = ?", (elixir,)).fetchall()
                for card in cardelixir:
                    print(card[0])
                break


def class_of_cards():
    conn, cursor = connection()
    # Print out id and type from type table in db (START)
    idlist = []
    cardtype = []
    id_type = cursor.execute("SELECT * FROM Type;").fetchall()
    for i in id_type: # Get the first and second values in the query and store them in the lists (START)
        id = i[0]
        idlist.append(id)
    for i in id_type:
        id = i[1]
        cardtype.append(id)
    for x in range(len(idlist)):
        id = idlist[x]
        cardclass = cardtype[x]
        print(f"{id} {cardclass}") # Get the first and second values in the query and store them in the lists and print them (END)
        # Print out id and type from type table in db (END)
    cofc = input('Please enter id of all the cards you would like to see ')
    acceptable_class = ["1", "3", "4"] # Acceptable inputs for this function
    while True:
        if cofc not in acceptable_class:
            cofc = input("Please enter a valid input ")
        else:
            if not cofc.isnumeric():
                cofc = input("Please enter a valid input ")
            else:
                print("Here are all the cards with selected class")
                cardclass = cursor.execute("SELECT Name FROM Card WHERE TypeID = ?", (cofc,)).fetchall()
                for card in cardclass:
                    print(card[0])
                break


def card_counters():
    conn, cursor = connection()
    counter = input('Please enter the counter of card you want from 1 - 29 ')
    # Acceptable inputs for this function
    acceptable_counters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"] 
    while True:
        if counter not in acceptable_counters:
            counter = input("Please enter a valid input ")
        else:
            if not counter.isnumeric():
                counter = input("Please enter a valid input ")
            else:
                print("Here are all the cards with selected counter")
                cardcounter = cursor.execute("SELECT Name FROM Card WHERE Id = ?", (counter,)).fetchall()
                for card in cardcounter:
                    print(card[0])
                break


# Start Of Program
#######################################################

no = "no"
print("Hello! Welcome to my program")
while True:
    what = input('press 1 to see all cards, 2 to see cards by rarity, 3 to see cards by elixir, 4 to see class of cards and 5 to see card counters.\nHowever, if you wish to exit the program, please enter "no" ')
    if what == no:
        print("Thank you for your time")
        break
    else:
        pass
    if what.isnumeric():
        what = int(what)
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
