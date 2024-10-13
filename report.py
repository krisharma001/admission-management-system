from database import get_db_connection

def generate_admission_report():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE admission_status = 'confirmed'")
    return cursor.fetchall()
