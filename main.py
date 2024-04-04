# Imports
import sqlite3

# Functions of code start here

# Connection function to prevent repeated code


def connection():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    return connection, cursor


def show_all_cards():
    conn, cursor = connection()
    cards = cursor.execute("SELECT Name FROM Card;").fetchall()
    for card in cards:
        print(card[0])


def cards_by_rarity():
    conn, cursor = connection()
    rarity = input('please enter id of rarity ')
    rarity = int(rarity)
    cardrarity = cursor.execute("SELECT Name FROM Card WHERE Rarity = ?", (rarity,)).fetchall()
    for card in cardrarity:
        print(card[0])


def cards_by_elixir():
    conn, cursor = connection()
    elixir = input('Please enter the elixir of card you want ')
    elixir = int(elixir)
    cardelixir = cursor.execute("SELECT Name, Elixir FROM Card ORDER BY Elixir;").fetchall()
    for card in cardelixir:
        print(card[0])


def class_of_cards():
    conn, cursor = connection()
    cofc = input('Please enter id of type of card ')
    cofc = int(cofc)
    cardclass = cursor.execute("SELECT Name FROM Card WHERE TypeID = ?", (cofc,)).fetchall()
    for card in cardclass:
        print(card[0])


# def cards_by_arena():
#     cursor = connection()
#     cards
#     cardarena = cursor.execute("SELECT * FROM Card WHERE ArenaID = ?", ()).fetchall()
#     print(x)
# functionname()


# def ():
#     cursor = connection()
#     x = cursor.execute("   ;").fetchall()
#     print(x)
# functionname()
        
while True:
    print("Hello! Welcome to my program")
    what = input('press 1 to see all cards, 2 to see cards by rarity, 3 to see cards by elixir, 4 to see class of cards ')
    what = int(what)
    if what == 1:
        show_all_cards()
    if what == 2:
        cards_by_rarity()
    if what == 3:
        cards_by_elixir()
    if what == 4:
        class_of_cards()
