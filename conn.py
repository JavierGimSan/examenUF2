import psycopg2

def connection_db():

    conn = psycopg2.connect(
        database = "postgres_24278",
        user = "user_postgres1",
        password = "pass_postgres1",
        host = "localhost",
        port = "5432"
    )

    print("Connexió establerta correctament")
    return conn

