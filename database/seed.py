from database.database import getDB

USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('teacher', 'student')) NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
"""

CLASSES_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    created_by INTEGER,
    invite_code TEXT UNIQUE,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
);
"""

CLASS_MEMBERS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS class_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    student_id INTEGER,
    joined_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

ATTENDANCE_SESSIONS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS attendance_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    date TEXT NOT NULL,
    created_by INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
);
"""

ATTENDANCE_RECORDS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS attendance_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    member_id INTEGER,
    status TEXT CHECK(status IN ('present', 'absent')) NOT NULL,
    FOREIGN KEY (session_id) REFERENCES attendance_sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES class_members(id) ON DELETE CASCADE,
    UNIQUE (session_id, member_id)
);
"""

TESTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    test_name TEXT NOT NULL,
    max_marks INTEGER NOT NULL,
    passing_marks INTEGER NOT NULL,
    test_date TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);
"""

TEST_RESULTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    marks_obtained REAL DEFAULT 0,
    FOREIGN KEY (test_id) REFERENCES tests(id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES class_members(id) ON DELETE CASCADE,
    UNIQUE(test_id, member_id) 
);
"""
queries = [
    USER_TABLE_QUERY,
    CLASSES_TABLE_QUERY,
    CLASS_MEMBERS_TABLE_QUERY,
    ATTENDANCE_SESSIONS_TABLE_QUERY,
    ATTENDANCE_RECORDS_TABLE_QUERY,
    TESTS_TABLE_QUERY,
    TEST_RESULTS_TABLE_QUERY
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
        cursor.close()
        db.close()
