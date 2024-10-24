import tkinter as tk
from tkinter import ttk, messagebox
from database import get_db_connection
import os
import hashlib
from dotenv import load_dotenv
from admin import get_admin_credentials, hash_password, admin_login
import course
import student
import report

load_dotenv()

class AdmissionManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Admission Management System")
        self.master.geometry("800x600")

        self.conn = None
        self.is_admin_logged_in = False

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both")

        self.create_admin_tab()
        self.create_course_tab()
        self.create_student_tab()
        self.create_report_tab()

        # Disable other tabs initially
        self.disable_tabs()

    def get_connection(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = get_db_connection()
            if self.conn is None:
                messagebox.showerror("Database Connection Error", "Failed to connect to the database.")
            else:
                print("Successfully connected to the database")
        return self.conn

    def create_admin_tab(self):
        admin_frame = ttk.Frame(self.notebook)
        self.notebook.add(admin_frame, text="Admin")

        ttk.Label(admin_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.admin_username = ttk.Entry(admin_frame)
        self.admin_username.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(admin_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.admin_password = ttk.Entry(admin_frame, show="*")
        self.admin_password.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(admin_frame, text="Login", command=self.admin_login).grid(row=2, column=0, columnspan=2, pady=20)

    def disable_tabs(self):
        for i in range(1, self.notebook.index('end')):
            self.notebook.tab(i, state='disabled')

    def enable_tabs(self):
        for i in range(1, self.notebook.index('end')):
            self.notebook.tab(i, state='normal')

    def create_course_tab(self):
        course_frame = ttk.Frame(self.notebook)
        self.notebook.add(course_frame, text="Course Management")

        ttk.Label(course_frame, text="Course Name:").grid(row=0, column=0, padx=10, pady=10)
        self.course_name = ttk.Entry(course_frame)
        self.course_name.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(course_frame, text="Department:").grid(row=1, column=0, padx=10, pady=10)
        self.department = ttk.Entry(course_frame)
        self.department.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(course_frame, text="Duration (months):").grid(row=2, column=0, padx=10, pady=10)
        self.duration = ttk.Entry(course_frame)
        self.duration.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(course_frame, text="Max Seats:").grid(row=3, column=0, padx=10, pady=10)
        self.max_seats = ttk.Entry(course_frame)
        self.max_seats.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(course_frame, text="Add Course", command=self.add_course).grid(row=4, column=0, columnspan=2, pady=20)

    def create_student_tab(self):
        student_frame = ttk.Frame(self.notebook)
        self.notebook.add(student_frame, text="Student Management")

        ttk.Label(student_frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
        self.first_name = ttk.Entry(student_frame)
        self.first_name.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
        self.last_name = ttk.Entry(student_frame)
        self.last_name.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Date of Birth:").grid(row=2, column=0, padx=10, pady=5)
        self.dob = ttk.Entry(student_frame)
        self.dob.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Email:").grid(row=3, column=0, padx=10, pady=5)
        self.email = ttk.Entry(student_frame)
        self.email.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Phone:").grid(row=4, column=0, padx=10, pady=5)
        self.phone = ttk.Entry(student_frame)
        self.phone.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Address:").grid(row=5, column=0, padx=10, pady=5)
        self.address = ttk.Entry(student_frame)
        self.address.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(student_frame, text="Course ID:").grid(row=6, column=0, padx=10, pady=5)
        self.course_id = ttk.Entry(student_frame)
        self.course_id.grid(row=6, column=1, padx=10, pady=5)

        ttk.Button(student_frame, text="Add Student", command=self.add_student).grid(row=7, column=0, columnspan=2, pady=20)

    def create_report_tab(self):
        report_frame = ttk.Frame(self.notebook)
        self.notebook.add(report_frame, text="Reports")

        ttk.Button(report_frame, text="Generate Admission Report", command=self.generate_report).pack(pady=20)

        self.report_text = tk.Text(report_frame, height=20, width=80)
        self.report_text.pack(pady=10)

    def admin_login(self):
        username = self.admin_username.get()
        password = self.admin_password.get()
        
        if admin_login(username, password):
            messagebox.showinfo("Success", "Admin login successful!")
            self.is_admin_logged_in = True
            self.enable_tabs()
        else:
            messagebox.showerror("Error", "Invalid admin credentials")
        
    def add_course(self):
        if not self.is_admin_logged_in:
            messagebox.showerror("Error", "Please login as admin first")
            return

        conn = self.get_connection()
        if conn:
            name = self.course_name.get()
            dept = self.department.get()
            dur = self.duration.get()
            max_seats = self.max_seats.get()
            course.add_course(conn, name, dept, dur, max_seats)
            messagebox.showinfo("Success", "Course added successfully!")

    def add_student(self):
        if not self.is_admin_logged_in:
            messagebox.showerror("Error", "Please login as admin first")
            return

        conn = self.get_connection()
        if conn:
            student.add_student(
                conn,
                self.first_name.get(),
                self.last_name.get(),
                self.dob.get(),
                self.email.get(),
                self.phone.get(),
                self.address.get(),
                self.course_id.get()
            )
            messagebox.showinfo("Success", "Student added successfully!")

    def generate_report(self):
        if not self.is_admin_logged_in:
            messagebox.showerror("Error", "Please login as admin first")
            return

        conn = self.get_connection()
        if conn:
            report_data = report.generate_admission_report(conn)
            self.report_text.delete('1.0', tk.END)
            if report_data:
                for row in report_data:
                    self.report_text.insert(tk.END, f"{row}\n")
            else:
                self.report_text.insert(tk.END, "No data available for the report.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdmissionManagementSystem(root)
    root.mainloop()