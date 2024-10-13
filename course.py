def add_course(conn, course_name, department, duration, max_seats):
    cursor = conn.cursor()
    query = "INSERT INTO courses (course_name, department, duration, max_seats) VALUES (%s, %s, %s, %s)"
    values = (course_name, department, duration, max_seats)
    cursor.execute(query, values)
    conn.commit()

def get_all_courses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

def get_available_seats(conn, course_id):
    cursor = conn.cursor()
    query = """
    SELECT c.max_seats - COUNT(s.student_id) as available_seats
    FROM courses c
    LEFT JOIN students s ON c.course_id = s.course_id AND s.admission_status = 'confirmed'
    WHERE c.course_id = %s
    GROUP BY c.course_id
    """
    cursor.execute(query, (course_id,))
    result = cursor.fetchone()
    return result[0] if result else 0