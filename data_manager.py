import database


@database.connection_handler
def create_db_table(cursor):
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cats
                        (id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER, color VARCHAR(50));
                    """)


@database.connection_handler
def create_cat(cursor, json_of_cat):
    cursor.execute("""
                    INSERT INTO cats (name, age, color)
                    VALUES (%(name)s, %(age)s, %(color)s)
                    RETURNING *;
                    """,
                   json_of_cat)
    return_value = cursor.fetchall()
    return return_value


@database.connection_handler
def get_all_cats(cursor):
    cursor.execute("""
                    SELECT *
                    FROM cats;
                    """)
    return_value = cursor.fetchall()
    return {'cats': return_value}


@database.connection_handler
def get_cat_by_id(cursor, id):
    cursor.execute("""
                    SELECT *
                    FROM cats
                    WHERE id = %(id)s;
                    """,
                   {"id": id})
    return_value = cursor.fetchone()
    return return_value


@database.connection_handler
def delete_cat_by_id(cursor, id):
    cursor.execute("""
                    DELETE
                    FROM cats
                    WHERE id = %(id)s;
                    """,
                   {"id": id})
