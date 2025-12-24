from database.database import getDB

USER_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        role ENUM('teacher', 'student') NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP   
    );
"""

CLASSES_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS classes (
        id INT PRIMARY KEY AUTO_INCREMENT,
        class_name VARCHAR(100) NOT NULL,
        created_by INT,
        invite_code VARCHAR(10) UNIQUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
    );
"""

CLASS_REQUEST_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS class_requests (
        id INT PRIMARY KEY AUTO_INCREMENT,
        class_id INT,
        student_id INT,
        status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
        requested_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
        FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE
    );
"""

CLASS_MEMBERS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS class_members (
        id INT PRIMARY KEY AUTO_INCREMENT,
        class_id INT,
        student_id INT,
        joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
        FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE
    );
"""

ATTENDANCE_SESSIONS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS attendance_sessions (
        id INT PRIMARY KEY AUTO_INCREMENT,
        class_id INT,
        date DATE NOT NULL,
        created_by INT,
        FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
        FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
    );
"""

ATTENDANCE_RECORDS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS attendance_records (
        id INT PRIMARY KEY AUTO_INCREMENT,
        session_id INT,
        student_id INT,
        status ENUM('present', 'absent') NOT NULL,
        FOREIGN KEY (session_id) REFERENCES attendance_sessions(id) ON DELETE CASCADE,
        FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
        UNIQUE KEY (session_id, student_id)
    )
"""

queries = [
    USER_TABLE_QUERY,
    CLASSES_TABLE_QUERY,
    CLASS_MEMBERS_TABLE_QUERY,
    CLASS_REQUEST_TABLE_QUERY,
    ATTENDANCE_SESSIONS_TABLE_QUERY,
    ATTENDANCE_RECORDS_TABLE_QUERY,
]


def init_db():
    db = getDB()
    cursor = db.cursor()
    try:

        for query in queries:
            cursor.execute(query)

        db.commit()
    except Exception as e:
        print(f"Failed to create Tables {e}")
    finally:
        if db and db.is_connected():
            db.close()
            cursor.close()
