Python version used: 3.13.1

Dependencies: 
pip install psycopg
pip install psycopg[binary]


Starting steps:

Run the setup.sql query in your postgresql database
Alter the connection params to match your database name, user, password, and port
    conn = psycopg.connect(
        host="localhost",
        dbname="student_db",
        user="postgres",
        password='PASSWORD',
        port=5432
    )

Run command, enter input responses in the specified format, starting with the query number you want, followed by the params in order space seperated ie: 
2 Logan Merriam log.mer@gmail.com 2026-11-15

Demo Video:
https://www.youtube.com/watch?v=9QEAIvwHZik