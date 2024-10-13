from database import get_db_connection

def add_student(first_name, last_name, dob, email, phone, address, course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, date_of_birth, email, phone, address, course_id, admission_status) VALUES (%s, %s, %s, %s, %s, %s, %s, 'pending')"
    values = (first_name, last_name, dob, email, phone, address, course_id)
    cursor.execute(query, values)
    conn.commit()

def get_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    return cursor.fetchone()

# Similarly, add update and delete functions
