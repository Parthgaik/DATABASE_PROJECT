import sqlite3


def show_all_cards():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM Card;").fetchall()
    print(cards)
show_all_cards()

def cards_by_rarity():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    rarity = input('please enter id of rarity')
    rarity = int(rarity)
    cardrarity = cursor.execute("SELECT * FROM Card WHERE Rarity = ?", (rarity,)).fetchall()
    print(cardrarity)


cards_by_rarity()

def cards_by_elixir():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    x = cursor.execute("SELECT * FROM Card ORDER BY Elixir;").fetchall()
    print(x)
functionname()




def ():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    x = cursor.execute("   ;").fetchall()
    print(x)
functionname()





def ():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    x = cursor.execute("   ;").fetchall()
    print(x)
functionname()





def ():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    x = cursor.execute("   ;").fetchall()
    print(x)
functionname()