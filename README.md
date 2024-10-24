# Admission Management System

A comprehensive **College Admission Management System** built using **Python** and **MySQL** for seamless management of student admissions, courses, and reports with a simple graphical user interface (GUI) built with **Tkinter**.

## Features

- **Admin Login**: Allows admin users to securely log in to the system.
- **Add Course**: Enables admins to add new courses for students.
- **Add Student**: Allows the addition of new students to the system.
- **View Student**: Displays details of a specific student based on their student ID.
- **Generate Admission Report**: Generates a list of students with confirmed admissions.

## Tech Stack

- **Backend**: Python, MySQL
- **Frontend**: Tkinter (Python GUI)
- **Database Connectivity**: MySQL Connector
- **Environment Variables**: Managed by Python `dotenv` package

## Folder Structure

```plaintext
📂 admission-management-system/
├── 📂 .venv/                # Virtual environment (not to be committed)
├── 📄 main.py               # Main GUI logic and imports
├── 📄 admin.py              # Admin-related logic (login)
├── 📄 student.py            # Student-related logic (add/view student)
├── 📄 course.py             # Course-related logic (add course)
├── 📄 report.py             # Report generation logic
├── 📄 database.py           # MySQL connection logic
├── 📄 .env                  # Environment file for MySQL credentials
└── 📄 README.md             # Project documentation (this file)
```

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/admission-management-system.git
cd admission-management-system
```

### Step 2: Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # For macOS/Linux
# or
.venv\Scripts\activate      # For Windows
```

### Step 3: Install required dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up `.env` file
Create a `.env` file in the root directory of the project and add the following content:

```bash
host="localhost"
user="root"                 # MySQL username
password="yourpassword"      # MySQL password
database="admission_system"  # Database name
```

### Step 5: Set up the MySQL Database
- Create the `admission_system` database in MySQL.
- Run the following SQL queries to set up the necessary tables:

```sql
CREATE TABLE admin (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    department VARCHAR(100),
    duration INT
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    course_id INT,
    admission_status VARCHAR(20),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### Step 6: Run the application
Once the setup is complete, run the following command:

```bash
python main.py
```

The GUI will launch, and you can interact with the system through the interface.

## Usage

1. **Admin Login**: Enter the admin credentials (you can add a default admin manually in the database).
2. **Add Course**: Admins can add new courses by filling out the required fields (Course Name, Department, Duration).
3. **Add Student**: Enter the student's details (First Name, Last Name, DOB, etc.) to register them in the system.
4. **View Student**: Enter a student's ID to view their information.
5. **Generate Report**: View a report of all students with confirmed admissions.

## Screenshots

_Add screenshots of the application running on your machine to give users a preview._

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- Be sure to replace `yourusername` in the clone URL with your GitHub username.
- You can also add a requirements file (`requirements.txt`) for managing dependencies:
  
```bash
mysql-connector-python
python-dotenv
tkinter
```
