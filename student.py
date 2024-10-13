def add_student(conn, first_name, last_name, dob, email, phone, address, course_id):
    cursor = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, date_of_birth, email, phone, address, course_id, admission_status) VALUES (%s, %s, %s, %s, %s, %s, %s, 'pending')"
    values = (first_name, last_name, dob, email, phone, address, course_id)
    cursor.execute(query, values)
    conn.commit()

def get_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    return cursor.fetchone()

def update_admission_status(conn, student_id, status):
    cursor = conn.cursor()
    query = "UPDATE students SET admission_status = %s WHERE student_id = %s"
    values = (status, student_id)
    cursor.execute(query, values)
    conn.commit()

def search_students(conn, keyword):
    cursor = conn.cursor()
    query = """
    SELECT * FROM students
    WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s
    """
    values = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
    cursor.execute(query, values)
    return cursor.fetchall()