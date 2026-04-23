import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shashank@1234",
        database="ai_doc_chat",
    )