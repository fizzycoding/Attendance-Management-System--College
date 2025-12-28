from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QVBoxLayout, QDialog, QCalendarWidget

from controllers.student_attendance_block_controller import StudentAttendanceBlockController
from database.database import getDB
from ui.attendance_ui import Ui_attendance_page


class AttendanceController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_attendance_page()
        self.ui.setupUi(self)
        self.user = user
        self.view_date = QDate.currentDate()
        self.loadClasses()
        self.ui.dropdown_classes.currentIndexChanged.connect(self.onClassChanged)
        self.updateInviteCodeUI()
        self.loadStudents()

        self.ui.btn_next_date.clicked.connect(self.incrementDate)
        self.ui.btn_prev_date.clicked.connect(self.decrementDate)
        self.ui.btn_date_picker.clicked.connect(self.openDatePicker)

    def loadClasses(self):
        self.ui.dropdown_classes.clear()
        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT id, class_name, invite_code FROM classes WHERE created_by=?"
            cursor.execute(query, (self.user["id"],))

            rows = cursor.fetchall()

            for row in rows:
                classData = {"id": row["id"], "code": row["invite_code"]}
                self.ui.dropdown_classes.addItem(row["class_name"], classData)

        except Exception as e:

            print("Error loading classes:", e)
        finally:
            cursor.close()
            db.close()

    def updateInviteCodeUI(self):
        data = self.ui.dropdown_classes.currentData()
        if data:
            code = data["code"]
            self.ui.invteCode_box.setText(code)
        else:
            self.ui.invteCode_box.setText("------")

    def loadStudents(self):
        # clear UI
        while self.ui.studentsLayout.count():
            item = self.ui.studentsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        data = self.ui.dropdown_classes.currentData()
        if not data: return

        classId = data["id"]
        date_str = self.view_date.toString("yyyy-MM-dd")
        db = getDB()
        cursor = db.cursor()
        try:
            attendance_map = {}
            mapQuery = """
                SELECT r.member_id, r.status 
                FROM attendance_records r
                JOIN attendance_sessions s ON r.session_id = s.id
                WHERE s.class_id = ? AND s.date = ?
            """
            cursor.execute(mapQuery, (classId, date_str))
            markedRows = cursor.fetchall()

            for row in markedRows:
                attendance_map[row[0]] = row[1]

            query = """
                SELECT 
                    c.id AS member_id,
                    u.name,
                    u.id AS student_id,
                 
                    (SELECT COUNT(*) FROM attendance_sessions WHERE class_id = ?) AS total_session,
                    (SELECT COUNT(*)
                        FROM attendance_records ar
                        JOIN attendance_sessions s ON ar.session_id = s.id
                        WHERE s.class_id = ? AND ar.member_id = c.id AND ar.status = 'present'
                    ) AS total_present
                FROM class_members c 
                JOIN users u ON c.student_id = u.id 
                WHERE c.class_id = ?
                ORDER BY u.name ASC
            """
            cursor.execute(query, (classId, classId, classId))
            data = cursor.fetchall()
            print(data)
            print(len(data))
            if len(data) <= 0:
                self.ui.students_stacked.setCurrentWidget(self.ui.no_student)
            else:
                self.ui.students_stacked.setCurrentWidget(self.ui.all_student)
                for i, d in enumerate(data):
                    user = dict(d)
                    member_id = user['member_id']

                    totalClasses = user.get("total_session", 0)
                    totalPresent = user.get("total_present", 0)

                    if totalClasses > 0:
                        rate = round((totalPresent / totalClasses) * 100)
                    else:
                        rate = 0

                    currentStatus = attendance_map.get(member_id, None)

                    self.insertIntoUi(
                        id=member_id,
                        sNo=i + 1,
                        name=user["name"],
                        student_id=member_id,
                        attendanceRate=rate,
                        status=currentStatus
                    )
            spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.studentsLayout.addItem(spacer)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            db.close()

    def markAttendance(self, member_id, status):
        data = self.ui.dropdown_classes.currentData()
        if not data: return
        class_id = data['id']

        date_str = self.view_date.toString("yyyy-MM-dd")

        db = getDB()
        cursor = db.cursor()
        try:
            # 1. Get Session ID
            checkSessionQuery = "SELECT id FROM attendance_sessions WHERE class_id=? AND date=?"
            cursor.execute(checkSessionQuery, (class_id, date_str))
            session = cursor.fetchone()

            if session:
                session_id = session[0]
            else:
                createSessionQuery = "INSERT INTO attendance_sessions (class_id, date, created_by) VALUES (?, ?, ?)"
                cursor.execute(createSessionQuery, (class_id, date_str, self.user["id"]))
                session_id = cursor.lastrowid

            # 2. Upsert Record
            usertQuery = """
                    INSERT INTO attendance_records (session_id, member_id, status) 
                    VALUES (?, ?, ?)
                    ON CONFLICT(session_id, member_id)
                    DO UPDATE SET status=excluded.status
                """
            cursor.execute(usertQuery, (session_id, member_id, status))
            db.commit()

        except Exception as e:
            print(f"Error marking attendance: {e}")
        finally:
            cursor.close()
            db.close()

    # ----- HELPERS -----

    def onClassChanged(self):
        self.updateInviteCodeUI()
        self.loadStudents()

    def insertIntoUi(self, id, sNo, name, student_id, attendanceRate, status):
        block = StudentAttendanceBlockController(id=id, sNo=sNo, name=name, member_id=student_id,
                                                 attendanceRate=attendanceRate, status=status)
        block.attendanceChanged.connect(self.markAttendance)
        self.ui.studentsLayout.addWidget(block)

    def incrementDate(self):
        self.view_date = self.view_date.addDays(1)
        self.updateDateLabel()
        self.loadStudents()

    def decrementDate(self):
        self.view_date = self.view_date.addDays(-1)
        self.updateDateLabel()
        self.loadStudents()

    def updateDateLabel(self):
        today = QDate.currentDate()

        if self.view_date == today:
            self.ui.btn_date_picker.setText("Today")
        else:
            self.ui.btn_date_picker.setText(self.view_date.toString("dd-MMM-yyyy"))

    def openDatePicker(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Date")
        dialog.setFixedSize(300, 250)  # Small size

        layout = QVBoxLayout(dialog)

        calendar = QCalendarWidget()
        calendar.setSelectedDate(self.view_date)
        calendar.setGridVisible(True)
        calendar.setStyleSheet("""
    QCalendarWidget QWidget {
        background-color: white; 
        color: black;
    }
    QCalendarWidget QAbstractItemView:enabled {
        color: black; 
        background-color: white;
        selection-background-color: #009688; 
        selection-color: white;
    }
    QCalendarWidget QToolButton {
        color: black;
        font-weight: bold;
        icon-size: 25px;
    }
    QCalendarWidget QSpinBox {
        color: black;
        background-color: white;
        selection-background-color: #009688;
    }
                    """)
        calendar.clicked.connect(lambda: dialog.accept())

        layout.addWidget(calendar)

        if dialog.exec():
            self.view_date = calendar.selectedDate()
            self.updateDateLabel()
            self.loadStudents()

    def refresh(self):
        current_data = self.ui.dropdown_classes.currentData()
        current_id = current_data["id"] if current_data else None

        self.ui.dropdown_classes.blockSignals(True)
        self.loadClasses()
        if current_id:
            for i in range(self.ui.dropdown_classes.count()):
                if current_id == self.ui.dropdown_classes.itemData(i)["id"]:
                    self.ui.dropdown_classes.setCurrentIndex(i)
                    break

        self.ui.dropdown_classes.blockSignals(False)
        self.updateInviteCodeUI()
        self.loadStudents()
