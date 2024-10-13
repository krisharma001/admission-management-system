from database import get_db_connection

def add_course(course_name, department, duration):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO courses (course_name, department, duration) VALUES (%s, %s, %s)"
    values = (course_name, department, duration)
    cursor.execute(query, values)
    conn.commit()

# Fetch course details similarly
