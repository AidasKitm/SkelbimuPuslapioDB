from SkelbimuDatabase import CUD_function, select_function


def create_user_table():
    query = """CREATE TABLE IF NOT EXISTS User(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username TEXT,
                password TEXT,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT)"""
    CUD_function(query)

def create_user(username,password,first_name,last_name):
    query = """INSERT INTO User(username,password,first_name,last_name) VALUES (%s,%s,%s,%s)"""
    params = [username,password,first_name,last_name]
    CUD_function(query,params)


def get_user(id):
    query = """SELECT * FROM User
                WHERE id = %s"""
    params = [id]
    select_function(query, params)


def update_user(first_name,id):
    query = """UPDATE User
                SET first_name = %s
                WHERE id = %s"""
    params = [first_name,id]
    CUD_function(query, params)


def delete_user(id):
    query = """DELETE FROM User
                WHERE id = %s"""
    params = [id]
    CUD_function(query, params)



