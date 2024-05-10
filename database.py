import os

import psycopg2


def create_connection_string():
    db_user_name = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_database_name = os.environ.get("POSTGRES_DB")
    db_host = os.environ.get("POSTGRES_HOST", "database")
    db_port = os.environ.get("POSTGRES_PORT", 5432)

    missing_variables = []

    if not db_user_name:
        missing_variables.append("POSTGRES_USER")
    if not db_password:
        missing_variables.append("POSTGRES_PASSWORD")
    if not db_database_name:
        missing_variables.append("POSTGRES_DB")
    if not db_host:
        missing_variables.append("POSTGRES_HOST")
    if not db_port:
        missing_variables.append("POSTGRES_PORT")

    if missing_variables:
        raise KeyError(f"The following variables are missing: {', '.join(missing_variables)}")

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
