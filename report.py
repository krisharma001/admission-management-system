def generate_admission_report(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE admission_status = 'confirmed'")
    return cursor.fetchall()

def generate_course_wise_report(conn):
    cursor = conn.cursor()
    query = """
    SELECT c.course_name, COUNT(s.student_id) as student_count
    FROM courses c
    LEFT JOIN students s ON c.course_id = s.course_id
    WHERE s.admission_status = 'confirmed'
    GROUP BY c.course_id
    """
    cursor.execute(query)
    return cursor.fetchall()

def generate_demographic_report(conn):
    cursor = conn.cursor()
    query = """
    SELECT 
        YEAR(date_of_birth) as birth_year,
        COUNT(*) as student_count
    FROM students
    WHERE admission_status = 'confirmed'
    GROUP BY YEAR(date_of_birth)
    ORDER BY birth_year
    """
    cursor.execute(query)
    return cursor.fetchall()