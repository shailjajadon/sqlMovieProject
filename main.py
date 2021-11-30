import sqlite3
import pandas as pd

conn = sqlite3.connect('movieTable.db')
print('Successfully Connected')

cur = conn.cursor()

choice = '0'
while choice != '8':
    choice = input('\n\nChoose from the menu:\n 1. Add data\n 2. Delete column\n 3. Update information\n 4. Search movie\n 5. Show table\n 6. Save changes\n 7. Undo\n 8. Exit\n')

    if choice=='1':
        id = int(input('Enter id: '))
        name = input('Enter movie name: ')
        actor = input('Enter actor name: ')
        actress = input('Enter actress name: ')
        yor = int(input('Enter year of release: '))
        director = input('Enter directors name: ')

        cur.execute("INSERT INTO movies VALUES(?, ?, ?, ?, ?, ?)", (id, name, actor, actress, yor, director))

    elif choice=='2':
        id = int(input('Enter movie id to be deleted: '))

        conn.execute("DELETE FROM movies WHERE id=?",(id,))

    elif choice=='3':
        id = int(input('Enter movie id to be updated: '))
        name = input('Enter updated movie name: ')
        actor = input('Enter updated actor name: ')
        actress = input('Enter updated actress name: ')
        yor = int(input('Enter updated year of release: '))
        director = input('Enter updated directors name: ')

        conn.execute("UPDATE movies SET name=?, actor=?, actress=?, yor=?, director=? WHERE id=?", (name, actor, actress, yor, director, id))

    elif choice=='4':
        param = int(input('Search by:\n 1. Actor\n 2. Actress\n 3. Year of release\n 4. Director\n'))
        cursor = ""
        if param==1:
            actor = input('Enter actor name: ')
            cursor = conn.execute("SELECT * FROM movies WHERE UPPER(actor)=UPPER(?)",(actor,))
        elif param==2:
            actress = input('Enter actress name: ')
            cursor = conn.execute("SELECT * FROM movies WHERE UPPER(actress)=UPPER(?)",(actress,))
        elif param==3:
            yor = int(input('Enter year of release: '))
            cursor = conn.execute("SELECT * FROM movies WHERE UPPER(yor)=UPPER(?)",(yor,))
        elif param==4:
            director = input('Enter director name: ')
            cursor = conn.execute("SELECT * FROM movies WHERE UPPER(director)=UPPER(?)", (director,))
        else:
            print('Wrong input')

        df = pd.DataFrame(cursor.fetchall(),
                          columns=['Movie ID', 'Movie Name', 'Lead Actor', 'Lead Actress', 'Year of Release',
                                   'Director'])
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(df)

    elif choice=='5':
        cursor = conn.execute("SELECT * FROM movies")
        df = pd.DataFrame(cursor.fetchall(), columns=['Movie ID', 'Movie Name', 'Lead Actor', 'Lead Actress', 'Year of Release', 'Director'])
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(df)

    elif choice=='6':
        conn.commit()
        print('Total changes: ',conn.total_changes)

    elif choice=='7':
        conn.rollback()

    elif choice=='8':
        break

print('\n\nSQL operations performed successfully')

conn.close()
print('Connection closed')
