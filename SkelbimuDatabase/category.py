from SkelbimuDatabase import CUD_function,select_function

def create_category_table():
    query = """CREATE TABLE IF NOT EXISTS Category(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name TEXT)"""
    CUD_function(query)


def create_category(name):
    query = """INSERT INTO Category(name) VALUES (%s)"""
    params = [name]
    CUD_function(query, params)


def get_category(id):
    query = """SELECT * FROM Category
                WHERE id = %s"""
    params = [id]
    select_function(query, params)


def update_category(name, id):
    query = """UPDATE Category
                SET name = %s
                WHERE id = %s"""
    params = [name, id]
    CUD_function(query, params)


def delete_category(id):
    query = """DELETE FROM Category
                WHERE id = %s"""
    params = [id]
    CUD_function(query, params)

