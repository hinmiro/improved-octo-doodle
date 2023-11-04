# notebook
import mysql.connector
import pyodbc

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='notebook',
    user='notes',
    password='notes',
    autocommit=True
)
try:
    cursor = connection.cursor()
    print("::Program starting::\n")
except pyodbc.DatabaseError:
    print("Cannot connect to database.")

notes = []
flag = True


def menu():
    print("------Notebook------\n")
    print("Choose one\n(1) Add new note\n(2) Read all notes\n(3) Delete specific note\n(4) End program")


def note_adder(add_note):
    sql = f"INSERT INTO notes (note) VALUES ('{add_note}')"
    cursor.execute(sql)


def note_reader():
    note = []
    sql = "SELECT * FROM notes;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            note.append(i)
    else:
        print("You have no notes in notebook.")
    return note


def note_deleter(delete_num, note_list):
    delete_id = note_list[delete_num][0]
    sql = f"DELETE FROM notes WHERE id = {delete_id}"
    cursor.execute(sql)


while flag:
    try:
        menu()
        note_choice = int(input("\nInput your choice: "))
        print("")
        if note_choice == 4:
            check = str(input("Are you sure to exit program y/n: ")).lower()

            if check == "y":
                print("You ended program, good bye.")
                flag = False

            elif check == "n":
                print("Program continues")
                continue

            else:
                print("Incorrect user input")

        elif note_choice == 1:
            new_note = str(input("Type new note: "))
            note_adder(new_note)

        elif note_choice == 2:
            temp = 1
            notes = note_reader()
            for row in notes:
                print(f"{temp}: {row[1]}")
                temp += 1

        elif note_choice == 3:
            notes = note_reader()
            try:
                delete_note_num = int(input("Give number of the note you want to delete: "))
                print("Invalid input, try again.\n")
                delete_note_num -= 1
                confirm = input(f"Are you sure to delete this note y/n - \n{notes[delete_note_num][1]}: ").lower()
                if confirm == "y":
                    note_deleter(delete_note_num, notes)
                elif confirm == "n":
                    continue
                else:
                    print("Invalid answer")
            except (IndexError, ValueError):
                print("Invalid input, try again.")

    except ValueError:
        print("Invalid input")
