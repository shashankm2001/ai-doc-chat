from storage.db import get_connection
import mysql.connector

# stored_chunks = []


def store_text(text):

    conn = get_connection()

    cursor = conn.cursor()

    query = "INSERT INTO documents (content) VALUES (%s)"
    cursor.execute(query, (text,))

    conn.commit()
    cursor.close()
    conn.close()


def get_text():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT content FROM documents order by id desc limit 1")

    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result[0] if result else None

def get_chunks():
    text = get_text()

    if not text:
        return []

    chunk_size = 500
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]







  
