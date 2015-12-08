import mysql.connector
connect_to_db = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='meetup_db')


def list_meetups_for_a_particular_user():
    prepare_database = ""
    try:
        prepare_database = connect_to_db.cursor()
        prepare_database.execute("""SELECT Real_name,meetups.StartTime,meetups.Location,meetups.Topic,meetups.Description FROM users
                          INNER JOIN meetupregistrations ON meetupregistrations.UsersId = users.Id
                          INNER JOIN meetups ON meetups.Id = meetupregistrations.UsersId WHERE users.Id = 2""")
        result = prepare_database.fetchall()
        print(result)
    except mysql.connector.DatabaseError as e:
        print(e)
    prepare_database.close()


def list_meetups_which_after_date():
    prepare_database = ""
    try:
        prepare_database = connect_to_db.cursor()
        prepare_database.execute("""SELECT * FROM meetups WHERE StartTime > '2015/11/27'""")
        result = prepare_database.fetchall()
        print(result)
    except mysql.connector.DatabaseError as e:
        print(e)
    prepare_database.close()


def list_users_who_have_introduction():
    prepare_database = ""
    try:
        prepare_database = connect_to_db.cursor()
        prepare_database.execute("""SELECT * FROM users WHERE introduction IS NOT NULL""")
        result = prepare_database.fetchall()
        print(result)
    except mysql.connector.DatabaseError as e:
        print(e)
    prepare_database.close()

def create_schema():
    prepare_database = ""
    file = open("create.sql", "r")
    commands = file.read()
    file.close()
    splitted_commands = commands.split(";")
    try:
        prepare_database = connect_to_db.cursor()
        for command in splitted_commands:
                prepare_database.execute(command)
    except mysql.connector.DatabaseError as ex:
        print(ex)
        connect_to_db.rollback()
    prepare_database.close()


def insert_data_to_tables():
    prepare_database = ""
    file = open("insert.sql", "r")
    commands = file.read()
    file.close()
    splitted_commands = commands.split(";")
    try:
        prepare_database = connect_to_db.cursor()
        for command in splitted_commands:
            prepare_database.execute(command)
            connect_to_db.commit()
    except mysql.connector.DatabaseError:
        connect_to_db.rollback()
    prepare_database.close()


def drop_all_table_from_database():
    file = open("drop_tables.sql", "r")
    commands = file.read()
    file.close()
    splitted_commands = commands.split(";")
    try:
        prepare_database = connect_to_db.cursor()
        for command in splitted_commands:
                prepare_database.execute(command)
    except mysql.connector.DatabaseError as e:
        print(e)

try:
    drop_all_table_from_database()
    create_schema()
    insert_data_to_tables()
    print("\n")
    list_meetups_for_a_particular_user()
    print("\n")
    list_meetups_which_after_date()
    print("\n")
    list_users_who_have_introduction()
except Exception as e:
    print(e)
