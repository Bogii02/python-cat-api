import copy
import database


@database.connection_handler
def create_db_table_if_not_exists(cursor):
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

    cats_list = []
    for cat in return_value:
        cat_dict = {
            "id": cat[0],
            "name": cat[1],
            "age": cat[2],
            "color": cat[3]
        }
        cats_list.append(cat_dict)

    return {'cats': cats_list}


@database.connection_handler
def get_cat_by_id(cursor, id):
    cursor.execute("""
                    SELECT *
                    FROM cats
                    WHERE id = %(id)s;
                    """,
                   {"id": id})
    return_value = cursor.fetchone()
    cat_dict = {
        "id": return_value[0],
        "name": return_value[1],
        "age": return_value[2],
        "color": return_value[3]
    }

    return {'cat': cat_dict}


@database.connection_handler
def delete_cat_by_id(cursor, id):
    cursor.execute("""
                    DELETE
                    FROM cats
                    WHERE id = %(id)s;
                    """,
                   {"id": id})


@database.connection_handler
def update_cat_by_id(cursor, json_of_cat_update, id):
    cat_data = copy.deepcopy(json_of_cat_update)
    cat_data["id"] = id
    cursor.execute("""
                    UPDATE cats
                    SET name = %(name)s, age = %(age)s, color = %(color)s
                    WHERE id = %(id)s
                    RETURNING *;
                    """,
                   cat_data)

    return_value = cursor.fetchone()

    cat_dict = {
        "id": return_value[0],
        "name": return_value[1],
        "age": return_value[2],
        "color": return_value[3]
    }

    return {'cat': cat_dict}
