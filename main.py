import sqlite3

#Functions of code
def show_all_cards():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT Name FROM Card;").fetchall()
    for card in cards:
        print(card[0])


def cards_by_rarity():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    rarity = input('please enter id of rarity ')
    rarity = int(rarity)
    cardrarity = cursor.execute("SELECT Name FROM Card WHERE Rarity = ?", (rarity,)).fetchall()
    for card in cardrarity:
        print(card[0])


def cards_by_elixir():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    elixir = input('Please enter the elixir of card you want ')
    elixir = int(elixir)
    cardelixir = cursor.execute("SELECT Name, Elixir FROM Card ORDER BY Elixir;").fetchall()
    for card in cardelixir:
        print(card[0])





def all_troops():
    connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
    cursor = connection.cursor()
    troops = input('Please enter id of rarity ')
    troops = int(troops)
    alltroops = cursor.execute("SELECT Name FROM Card WHERE TypeID = ?", (troops,)).fetchall()
    for card in alltroops:
        print(card[0])






# def ():
#     connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
#     cursor = connection.cursor()
#     x = cursor.execute("   ;").fetchall()
#     print(x)
# functionname()





# def ():
#     connection = sqlite3.connect("Yr13ClashRoyaleDB.db")
#     cursor = connection.cursor()
#     x = cursor.execute("   ;").fetchall()
#     print(x)
# functionname()


if __name__ == "__main__":
    #main code starts here
    all_troops()