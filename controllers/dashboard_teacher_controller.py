from datetime import datetime, timedelta

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy

from database.database import getDB
from ui.dashboard_teacher_ui import Ui_dashboard_page
from utils.chart_manager import ChartManager


class DashboardTeacherController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui = Ui_dashboard_page()
        self.ui.setupUi(self)

        self.chart_manager = ChartManager()

        self.ui.dropdown_classes.currentIndexChanged.connect(self.loadDashboardData)

        self.loadClasses()

    def refresh(self):
        try:
            current_data = self.ui.dropdown_classes.currentData()
            self.loadClasses()

            if current_data:
                index = self.ui.dropdown_classes.findData(current_data)
                if index >= 0:
                    self.ui.dropdown_classes.setCurrentIndex(index)
                if index == self.ui.dropdown_classes.currentIndex():
                    self.loadDashboardData()
        except Exception as e:
            print(f"Error refreshing dashboard: {e}")

    def loadClasses(self):
        self.ui.dropdown_classes.blockSignals(True)
        self.ui.dropdown_classes.clear()

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("SELECT id, class_name FROM classes WHERE created_by = ?", (self.user['id'],))
            classes = cursor.fetchall()

            if classes:
                for cls in classes:
                    self.ui.dropdown_classes.addItem(cls['class_name'], cls['id'])

                self.ui.dropdown_classes.blockSignals(False)

                if self.ui.dropdown_classes.count() > 0:
                    self.ui.dropdown_classes.setCurrentIndex(0)
                    self.loadDashboardData()
                else:
                    self.resetClassData()
            else:
                self.ui.dropdown_classes.addItem("No Classes Found")
                self.ui.dropdown_classes.blockSignals(False)

        except Exception as e:
            print(f"Error loading classes: {e}")
            self.ui.dropdown_classes.blockSignals(False)
        finally:
            cursor.close()
            db.close()

    def loadDashboardData(self):
        try:
            class_id = self.ui.dropdown_classes.currentData()
            if not class_id: return

            self.loadTopCards(class_id)
            self.loadTodayReport(class_id)
            self.loadWeeklyReport(class_id)

            self.loadLeaderboard(class_id)
        except Exception as e:
            print(f"Error loading dashboard data: {e}")

    def loadTopCards(self, class_id):
        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("SELECT COUNT(*) FROM class_members WHERE class_id=?", (class_id,))
            total_students = cursor.fetchone()[0]

            self.ui.val_total_student.setText(str(total_students))

            cursor.execute("SELECT COUNT(*) FROM attendance_sessions WHERE class_id=?", (class_id,))
            total_classes = cursor.fetchone()[0]

            self.ui.val_total_classes.setText(str(total_classes))

            cursor.execute("SELECT COUNT(*) FROM tests WHERE class_id=?", (class_id,))
            total_tests = cursor.fetchone()[0]

            self.ui.val_tests.setText(str(total_tests))

            cursor.execute("""
                SELECT 
                    COUNT(CASE WHEN r.status = 'present' THEN 1 END),
                    COUNT(CASE WHEN r.status = 'absent' THEN 1 END)
                FROM attendance_records r
                JOIN attendance_sessions s ON r.session_id = s.id
                WHERE s.class_id = ?
            """, (class_id,))
            stats = cursor.fetchone()

            present = stats[0] if stats else 0
            absent = stats[1] if stats else 0
            total_records = present + absent

            avg_rate = 0
            if total_records > 0:
                avg_rate = int((present / total_records) * 100)

            self.ui.val_avg_attendance.setText(f"{avg_rate}%")

        except Exception as e:
            print(f"Error loading top cards: {e}")
            self.ui.val_total_student.setText("0")
            self.ui.val_total_classes.setText("0")
            self.ui.val_tests.setText("0")
            self.ui.val_avg_attendance.setText("0%")
        finally:
            cursor.close()
            db.close()

    def loadTodayReport(self, class_id):
        container = self.ui.chart_pie_container
        if not container.layout():
            l = QVBoxLayout()
            l.setContentsMargins(0, 0, 0, 0)
            container.setLayout(l)

        self._clear_layout(container.layout())

        db = getDB()
        cursor = db.cursor()

        try:
            today_str = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("SELECT id FROM attendance_sessions WHERE class_id=? AND date=?", (class_id, today_str))
            session = cursor.fetchone()

            present, absent, not_marked = 0, 0, 0
            total_students = 0

            cursor.execute("SELECT COUNT(*) FROM class_members WHERE class_id=?", (class_id,))
            res = cursor.fetchone()
            if res:
                total_students = res[0]

            if session:
                session_id = session[0]
                cursor.execute("""
                    SELECT status, COUNT(*) FROM attendance_records 
                    WHERE session_id=? GROUP BY status
                """, (session_id,))
                rows = cursor.fetchall()

                for status, count in rows:
                    if status == 'present':
                        present = count
                    elif status == 'absent':
                        absent = count

            not_marked = total_students - (present + absent)

            if total_students > 0:
                chart_view = self.chart_manager.createPieChart(present, absent, total_students)
                container.layout().addWidget(chart_view)
            else:
                chart_view = self.chart_manager.createPieChart(0, 0, 1)
                container.layout().addWidget(chart_view)

        except Exception as e:
            print(f"Error loading today's report: {e}")
        finally:
            cursor.close()
            db.close()

    def loadWeeklyReport(self, class_id):
        container = self.ui.chart_weekly_container
        if not container.layout():
            l = QVBoxLayout()
            l.setContentsMargins(0, 0, 0, 0)
            container.setLayout(l)
        self._clear_layout(container.layout())

        db = getDB()
        cursor = db.cursor()

        try:
            present_data = []
            absent_data = []
            days_labels = []

            for i in range(6, -1, -1):
                day = datetime.now() - timedelta(days=i)
                date_str = day.strftime("%Y-%m-%d")
                days_labels.append(day.strftime("%a"))

                cursor.execute("""
                    SELECT 
                        COUNT(CASE WHEN r.status='present' THEN 1 END),
                        COUNT(CASE WHEN r.status='absent' THEN 1 END)
                    FROM attendance_records r
                    JOIN attendance_sessions s ON r.session_id = s.id
                    WHERE s.class_id = ? AND s.date = ?
                """, (class_id, date_str))

                res = cursor.fetchone()
                present_data.append(res[0] if res else 0)
                absent_data.append(res[1] if res else 0)

            chart_view = self.chart_manager.createWeeklyBarChart(days_labels, present_data, absent_data)
            container.layout().addWidget(chart_view)

        except Exception as e:
            print(f"Error loading weekly report: {e}")
        finally:
            cursor.close()
            db.close()

    def loadLeaderboard(self, class_id):
        layout = self.ui.container_top_students
        self._clear_layout(layout)

        db = getDB()
        cursor = db.cursor()

        try:
            query = """
                SELECT 
                    u.name,
                    COUNT(CASE WHEN r.status='present' THEN 1 END) as p_count,
                    COUNT(s.id) as total_sessions
                FROM class_members c
                JOIN users u ON c.student_id = u.id
                LEFT JOIN attendance_records r ON r.member_id = c.id
                LEFT JOIN attendance_sessions s ON r.session_id = s.id AND s.class_id = ?
                WHERE c.class_id = ?
                GROUP BY u.id
                ORDER BY p_count DESC
                LIMIT 5
            """
            cursor.execute(query, (class_id, class_id))
            rows = cursor.fetchall()

            for idx, row in enumerate(rows):
                name = row[0]
                p_count = row[1]
                total = row[2]

                rate = int((p_count / total * 100)) if total > 0 else 0
                self._addLeaderboardRow(layout, idx + 1, name, rate)

            verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            layout.addItem(verticalSpacer)

        except Exception as e:
            print(f"Error loading leaderboard: {e}")
        finally:
            cursor.close()
            db.close()

    def _addLeaderboardRow(self, layout, rank, name, rate):
        try:
            row = QFrame()
            row.setStyleSheet("background: transparent; border-radius: 5px; border: none; border-top: 1px solid #eee;")
            row.setFixedHeight(35)

            row_layout = QHBoxLayout(row)
            row_layout.setContentsMargins(5, 0, 5, 0)

            lbl_name = QLabel(f"{rank}. {name}")
            lbl_name.setStyleSheet("font-weight: 600; color: #333; font-family: 'Segoe UI';")

            lbl_rate = QLabel(f"{rate}%")
            color = "#2ab79d" if rate >= 75 else "#ffbf00" if rate >= 50 else "#ff5252"
            lbl_rate.setStyleSheet(f"font-weight: bold; color: {color}; font-family: 'Segoe UI';")
            lbl_rate.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            row_layout.addWidget(lbl_name)
            row_layout.addStretch()
            row_layout.addWidget(lbl_rate)

            layout.addWidget(row)
        except Exception as e:
            print(f"Error adding leaderboard row: {e}")

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                layout.removeItem(item)
