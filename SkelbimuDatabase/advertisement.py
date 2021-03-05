from SkelbimuDatabase import CUD_function,select_function

def create_advertisement_table():
    query = """CREATE TABLE IF NOT EXISTS Advertisement(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                title TEXT,
                date DATE,
                description TEXT,
                user_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (category_id) REFERENCES Category(id))"""
    CUD_function(query)


def create_advertisement(title,date,description,user_id,category_id):
    query = """INSERT INTO Advertisement(title,date,description,user_id,category_id) VALUES (%s,%s,%s,%s,%s)"""
    params = [title,date,description,user_id,category_id]
    CUD_function(query, params)


def get_advertisement(id):
    query = """SELECT * FROM Advertisement
                WHERE id = %s"""
    params = [id]
    select_function(query, params)


def update_advertisement(description, id, editing_user):
    get_advertisement_user_id_query = """SELECT user_id FROM Advertisement
                WHERE id = %s"""
    get_advertisement_user_id_params = [id]
    advertisement_user_id = select_function(get_advertisement_user_id_query, get_advertisement_user_id_params)
    if editing_user == advertisement_user_id[0]:
        edit_advertisement_query = """UPDATE Advertisement
                SET description = %s
                WHERE id = %s"""
        edit_advertisement_params = [description, id]

        CUD_function(edit_advertisement_query, edit_advertisement_params)
    else:
        print("You can't edit advertisement that are not yours")

def delete_category(id):
    query = """DELETE FROM Advertisement
                WHERE id = %s"""
    params = [id]
    CUD_function(query, params)
