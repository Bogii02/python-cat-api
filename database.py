import os

import psycopg2
from psycopg2 import extras


def create_connection_string():
    db_user_name = os.environ.get("PSQL_USER_NAME")
    db_password = os.environ.get("PSQL_PASSWORD")
    db_host = os.environ.get("PSQL_HOST")
    db_database_name = os.environ.get("PSQL_DB_NAME")

    defined_variables = all([db_user_name, db_password, db_host, db_database_name])

    if not defined_variables:
        raise KeyError("Needed variable not defined")

    return f"postgresql://{db_user_name}:{db_password}@{db_host}/{db_database_name}"


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
        connection = open_database()

        cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

        try:
            value = function_to_wrap(cursor, *args, **kwargs)
        finally:
            cursor.close()
            connection.close()

        return value

    return wrapper
