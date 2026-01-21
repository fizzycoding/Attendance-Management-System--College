from datetime import datetime

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.student_class_block_controller import StudentClassBlockController
from database.database import getDB
from ui.classopen_std_ui import Ui_ClassOpenStd


class ClassOpenStdController(QWidget):
    def __init__(self, user, home, classId):
        super().__init__()
        self.ui = Ui_ClassOpenStd()
        self.ui.setupUi(self)
        self.classId = classId
        self.home = home
        self.user = user
        self.classData = None

        self.view_date = QDate.currentDate()
        self.loadClass()
        if self.classData:
            self.loadUserData()
            self.loadStudents()
        self.ui.back_btn.clicked.connect(self.home.closeClassOpened)

    def loadUserData(self):
        db = getDB()
        cursor = db.cursor()
        try:
            classCountQuery = """
                    SELECT 
                        (SELECT COUNT(*) FROM attendance_sessions WHERE class_id = ?) AS total,
                        (SELECT COUNT(*) FROM attendance_records ar
                         JOIN attendance_sessions a ON a.id = ar.session_id
                         JOIN class_members cm ON cm.id = ar.member_id
                         WHERE a.class_id = ? AND cm.student_id = ? AND ar.status = "present") as present
                    """
            cursor.execute(classCountQuery, (self.classId, self.classId, self.user["id"]))
            result = cursor.fetchone()
            print(result)
            if result:
                total_classes = result[0]
                total_present = result[1]
                total_absent = total_classes - total_present
                self.ui.val_total_classes.setText(str(total_classes))
                self.ui.val_present.setText(str(max(0, total_present)))
                self.ui.val_absent.setText(str(max(0, total_absent)))

                if total_classes > 0:
                    rate = int(round((total_present / total_classes) * 100))
                else:
                    rate = 0
                self.ui.val_rate.setText(f"{rate}%")

                today_str = datetime.now().strftime("%Y-%m-%d")
                status_query = """
            SELECT ar.status 
            FROM attendance_records ar
            JOIN attendance_sessions s ON s.id = ar.session_id
            JOIN class_members cm ON cm.id = ar.member_id
            WHERE s.class_id = ? 
              AND cm.student_id = ? 
              AND s.date = ?
        """

                cursor.execute(status_query, (self.classId, self.user["id"], today_str))
                result = cursor.fetchone()
                if result:
                    status = result[0]  # 'present' or 'absent'

                    if status == 'present':
                        self.ui.val_today.setText("Present")
                        self.ui.val_today.setStyleSheet(
                            "color: #2ab79d; font-size: 24px; font-weight: bold; border:none;")
                    else:
                        self.ui.val_today.setText("Absent")
                        self.ui.val_today.setStyleSheet(
                            "color: #ff5252; font-size: 24px; font-weight: bold; border:none;")
                else:
                    self.ui.val_today.setText("Not Marked")
                    self.ui.val_today.setStyleSheet("color: #777; font-size: 20px; font-weight: bold; border:none;")

        except Exception as e:
            print("Failed to load students", e)

        finally:
            cursor.close()
            db.close()

    def loadClass(self):
        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT id,class_name as name,invite_code as code FROM classes WHERE id = ?"
            cursor.execute(query, (self.classId,))
            data = cursor.fetchone()

            if data:
                # Convert to dict if row factory isn't set
                if isinstance(data, tuple):
                    self.classData = {"id": data[0], "name": data[1], "code": data[2]}
                else:
                    self.classData = dict(data)

                self.ui.class_name.setText(self.classData["name"])
            else:
                print("Class not found!")
        except Exception as e:
            print(f"Failed to load class data, {e}")
        finally:
            cursor.close()
            db.close()

    def loadStudents(self):
        # clear UI
        while self.ui.studentLayout.count():
            item = self.ui.studentLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        data = self.classData
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
                if isinstance(row, tuple):
                    attendance_map[row[0]] = row[1]
                else:
                    attendance_map[row['member_id']] = row['status']

            query = """
                    SELECT 
                        c.id AS member_id,
                        u.name,
                        u.id AS user_id,
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

            if not data:
                self.ui.student_stack.setCurrentWidget(self.ui.no_student)
            else:
                self.ui.student_stack.setCurrentWidget(self.ui.all_students)
                for i, d in enumerate(data):
                    if isinstance(d, tuple):
                        user = {
                            "member_id": d[0],
                            "name": d[1],
                            "user_id": d[2],
                            "total_session": d[3],
                            "total_present": d[4]
                        }
                    else:
                        user = dict(d)
                    s_id = user['member_id']

                    totalClasses = user.get("total_session", 0)
                    totalPresent = user.get("total_present", 0)

                    if totalClasses > 0:
                        rate = round((totalPresent / totalClasses) * 100)
                    else:
                        rate = 0

                    currentStatus = attendance_map.get(s_id, None)

                    self.insertIntoUi(
                        id=user["member_id"],
                        sNo=i + 1,
                        name=user["name"],
                        attendanceRate=rate,
                        status=currentStatus,
                        isCurrent=user["user_id"] == self.user["id"]
                    )
            spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.studentLayout.addItem(spacer)
        except Exception as e:
            print(f"Error loading students: {e}")
        finally:
            cursor.close()
            db.close()

    # ----- HELPERS -----

    def onClassChanged(self):
        self.loadStudents()

    def insertIntoUi(self, id, sNo, name, attendanceRate, status, isCurrent):
        block = StudentClassBlockController(id=id, sNo=sNo, name=name,
                                            attendanceRate=attendanceRate, status=status, role=self.user["role"],
                                            isCurrent=isCurrent)
        block.studentModified.connect(self.studentBlockModified)
        self.ui.studentLayout.addWidget(block)

    def studentBlockModified(self):
        self.loadStudents()
