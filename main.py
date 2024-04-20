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
    acceptable_rarity = ["1", "2", "3", "4",]
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
    acceptable_elixir = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
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
    # Print out id and type from type table in db
    idlist = []
    cardtype = []
    id_type = cursor.execute("SELECT * FROM Type;").fetchall()
    for i in id_type:
        id = i[0]
        idlist.append(id)
    for i in id_type:
        id = i[1]
        cardtype.append(id)
    for x in range(len(idlist)):
        id = idlist[x]
        cardclass = cardtype[x]
        print(f"{id} {cardclass}")
    cofc = input('Please enter id of all the cards you would like to see ')
    acceptable_class = ["1","3", "4"]
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


# def cards_by_arena():
#     conn, cursor = connection()
#     cards =
#     cardarena = cursor.execute("SELECT * FROM Card WHERE ArenaID = ?", ()).fetchall()
#     print(x)
# functionname()


# def ():
#     cursor = connection()
#     x = cursor.execute("   ;").fetchall()
#     print(x)
# functionname()


# Start Of Program
#######################################################

no = "no"
print("Hello! Welcome to my program")
while True:
    what = input('press 1 to see all cards, 2 to see cards by rarity, 3 to see cards by elixir, 4 to see class of cards.\nHowever, if you wish to exit the program, please enter "no" ')
    if what == no:
        print("Thank you for your time")
        break
    else:
        pass
    if what.isnumeric():
        what = int(what)
        if what > 4 or what < 1:
            print("please Enter Valid input")
        if what == 1:
            show_all_cards()
        if what == 2:
            cards_by_rarity()
        if what == 3:
            cards_by_elixir()
        if what == 4:
            class_of_cards()
    else:
        print("Please Enter Valid input")
