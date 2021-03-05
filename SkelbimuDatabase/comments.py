from SkelbimuDatabase import CUD_function,select_function

def create_comments_table():
    query = """CREATE TABLE IF NOT EXISTS Comment(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                comment_text TEXT,
                user_id INTEGER,
                advertisement_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (advertisement_id) REFERENCES Advertisement(id))"""
    CUD_function(query)


def create_comment(comment_text,user_id,advertisement_id):
    query = """INSERT INTO Comment(comment_text,user_id,advertisement_id) VALUES (%s,%s,%s)"""
    params = [comment_text,user_id,advertisement_id]
    CUD_function(query, params)


def get_comments(id):
    query = """SELECT * FROM Comment
                WHERE advertisement_id = %s"""
    params = [id]
    select_function(query, params)


def update_comment(comment_text, id, editing_user):
    get_comment_user_id_query = """SELECT user_id FROM Comment
                WHERE id = %s"""
    get_comment_user_id_params = [id]
    comment_user_id = select_function(get_comment_user_id_query, get_comment_user_id_params)
    if editing_user == comment_user_id[0]:
        edit_comment_query = """UPDATE Comment
                SET comment_text = %s
                WHERE id = %s"""
        edit_comment_params = [comment_text, id]

        CUD_function(edit_comment_query, edit_comment_params)
    else:
        print("You can't edit comments that are not yours")

def delete_comment(id):
    query = """DELETE FROM Comment
                WHERE id = %s"""
    params = [id]
    CUD_function(query, params)

