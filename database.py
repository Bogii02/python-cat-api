import os

import psycopg2


def create_connection_string():
    db_user_name = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_database_name = os.environ.get("POSTGRES_DB")
    db_host = os.environ.get("POSTGRES_HOST")
    db_port = os.environ.get("POSTGRES_PORT")

    defined_variables = all([db_user_name, db_password, db_host, db_port, db_database_name])

    if not defined_variables:
        raise KeyError("Needed variable not defined")

    return f"postgresql://{db_user_name}:{db_password}@{db_host}:{db_port}/{db_database_name}"


def open_database():
    try:
        conn_url = create_connection_string()
        connection = psycopg2.connect(conn_url)
        connection.autocommit = True

    except psycopg2.DatabaseError as exception:
        raise exception

    return connection


def connection_handler(function_to_wrap):
    def wrapper(*args, **kwargs):

        try:
            with open_database() as connection:
                with connection.cursor() as cursor:
                    value = function_to_wrap(cursor, *args, **kwargs)

        finally:
            cursor.close()
            connection.close()

        return value

    return wrapper
