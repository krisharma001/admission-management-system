from database import get_db_connection

def admin_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM admin WHERE username = %s", (username,))
    stored_password = cursor.fetchone()
    
    if stored_password and stored_password[0] == password:
        return True
    else:
        return False
