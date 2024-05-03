import database


@database.connection_handler
def get_all_cats(cursor):
    cursor.execute("""
                    SELECT *
                    FROM cats
                    """)
    return_value = cursor.fetchall()
    return return_value
