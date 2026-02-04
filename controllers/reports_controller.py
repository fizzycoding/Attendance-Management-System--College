from datetime import date

from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QFileDialog

from controllers.export_report_popup_controller import ExportReportPopupController
from controllers.report_student_names_row_controller import ReportStudentNamesRowController
from controllers.test_report_row_controller import TestReportRowController
from database.database import getDB
from ui.view_reports_ui import Ui_view_reports_page
from utils.excelExporter import ExcelExporter  # <--- IMPORT THE EXPORTER
from utils.message import showMessage


class ReportsController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_view_reports_page()
        self.ui.setupUi(self)
        self.user = user

        self.student_rows = []

        self.ui.content_stack.setCurrentWidget(self.ui.no_student)
        self.loadClasses()

        self.ui.dropdown_classes.currentIndexChanged.connect(self.loadStudents)
        self.ui.btn_export.clicked.connect(self.openExportPopup)

    def loadClasses(self):
        self.ui.dropdown_classes.blockSignals(True)
        self.ui.dropdown_classes.clear()

        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT id, class_name FROM classes WHERE created_by=?"
            cursor.execute(query, (self.user["id"],))
            rows = cursor.fetchall()

            if not rows:
                self.ui.content_stack.setCurrentWidget(self.ui.no_classes)
                return
            for row in rows:
                classData = {"id": row["id"]}
                self.ui.dropdown_classes.addItem(row["class_name"], classData)

        except Exception as e:
            print("Reports-Error loading classes:", e)
        finally:
            cursor.close()
            db.close()
            self.ui.dropdown_classes.blockSignals(False)
            self.loadStudents()

    def loadStudents(self):
        self.student_rows = []
        while self.ui.all_students_container.count():
            item = self.ui.all_students_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        data = self.ui.dropdown_classes.currentData()
        if not data:
            return

        classId = data["id"]
        db = getDB()
        cursor = db.cursor()

        first_member_id = None

        try:
            query = """
                SELECT 
                    c.id AS member_id,
                    COALESCE(c.guest_name, u.name) as name,
                    u.id AS student_id,
                    (SELECT COUNT(*) FROM attendance_sessions WHERE class_id = ?) AS total_session,
                    (SELECT COUNT(*)
                        FROM attendance_records ar
                        JOIN attendance_sessions s ON ar.session_id = s.id
                        WHERE s.class_id = ? AND ar.member_id = c.id AND ar.status = 'present'
                    ) AS total_present
                FROM class_members c 
                LEFT JOIN users u ON c.student_id = u.id 
                WHERE c.class_id = ?
                ORDER BY COALESCE(c.guest_name, u.name) ASC
            """
            cursor.execute(query, (classId, classId, classId))
            data = cursor.fetchall()

            if len(data) <= 0:
                self.ui.content_stack.setCurrentWidget(self.ui.no_student)
                self.ui.classes_attended_count.setText("0")
                self.ui.present_count.setText("0")
                self.ui.absent_count.setText("0")
                self.clearTestResults()
            else:
                self.ui.content_stack.setCurrentWidget(self.ui.classes_selected)

                for i, d in enumerate(data):
                    user = dict(d)
                    member_id = user["member_id"]

                    if i == 0:
                        first_member_id = member_id

                    totalClasses = user.get("total_session", 0)
                    totalPresent = user.get("total_present", 0)
                    rate = round((totalPresent / totalClasses) * 100) if totalClasses > 0 else 0

                    self.insertIntoUi(
                        id=member_id,
                        sNo=i + 1,
                        name=user["name"],
                        student_id=member_id,
                        attendanceRate=rate,
                    )

            self.ui.all_students_container.addItem(
                QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            )

            if first_member_id:
                self.loadStudentData(first_member_id)

        except Exception as e:
            print("Error loading students:", e)
        finally:
            cursor.close()
            db.close()

    def insertIntoUi(self, id, sNo, name, student_id, attendanceRate=0):
        card = ReportStudentNamesRowController(memberId=id, sNo=sNo, name=name, studentId=student_id,
                                               attendanceRate=attendanceRate)
        card.clicked.connect(self.loadStudentData)

        self.ui.all_students_container.addWidget(card)
        self.student_rows.append(card)

    def loadStudentData(self, memId):

        for card in self.student_rows:
            if card.memberId == memId:
                card.setSelected(True)
            else:
                card.setSelected(False)
        class_data = self.ui.dropdown_classes.currentData()
        if not class_data: return
        classId = class_data["id"]

        db = getDB()
        cursor = db.cursor()

        try:
            query_att = """
                SELECT 
                    (SELECT COUNT(*) FROM attendance_sessions WHERE class_id = ?) as total,
                    (SELECT COUNT(*) FROM attendance_records ar 
                     JOIN attendance_sessions s ON ar.session_id = s.id 
                     WHERE s.class_id = ? AND ar.member_id = ? AND ar.status = 'present') as present
            """
            cursor.execute(query_att, (classId, classId, memId))
            att_data = cursor.fetchone()

            if att_data:
                total = att_data[0]
                present = att_data[1]
                absent = total - present

                self.ui.classes_attended_count.setText(f"{total:02d}")
                self.ui.present_count.setText(f"{present:02d}")
                self.ui.absent_count.setText(f"{absent:02d}")

            self.clearTestResults()

            query_tests = """
                SELECT t.test_name, t.max_marks, t.passing_marks, tr.marks_obtained
                FROM test_results tr
                JOIN tests t ON tr.test_id = t.id
                WHERE tr.member_id = ?
                ORDER BY t.id DESC
            """
            cursor.execute(query_tests, (memId,))
            test_rows = cursor.fetchall()

            if not test_rows:
                self.ui.stackedWidget.setCurrentIndex(0)  # Show "No Tests Found" widget
            else:
                self.ui.stackedWidget.setCurrentIndex(1)  # Show List widget

                for t in test_rows:
                    row = TestReportRowController(
                        name=t[0],
                        max_marks=t[1],
                        passing_marks=t[2],
                        marks_obtained=t[3]
                    )
                    self.ui.test_results_layout.addWidget(row)

                self.ui.test_results_layout.addItem(
                    QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
                )

        except Exception as e:
            print(f"Error loading student data for {memId}: {e}")
        finally:
            cursor.close()
            db.close()

    def clearTestResults(self):
        if self.ui.test_results_layout:
            while self.ui.test_results_layout.count():
                item = self.ui.test_results_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

    def openExportPopup(self):
        className = self.ui.dropdown_classes.currentText()
        if not className:
            return

        popup = ExportReportPopupController(className, self)

        if popup.exec():
            data = popup.getExportData()
            print("User Selected:", data['action'])
            print("Date Range:", data['from_date'], "to", data['to_date'])

            if data["action"] == "excel":
                self.exportExcel(data)
            else:
                self.exportPdf(data)

    def exportExcel(self, data):
        filename = f"Report_{data['from_date']}_to_{data['to_date']}.xlsx"
        path, _ = QFileDialog.getSaveFileName(self, "Save Excel", filename, "Excel Files (*.xlsx)")

        if not path:
            return

        class_data = self.ui.dropdown_classes.currentData()
        if not class_data: return
        class_id = class_data['id']
        class_name = self.ui.dropdown_classes.currentText()

        y1, m1, d1 = map(int, data['from_date'].split('-'))
        start_date = date(y1, m1, d1)

        y2, m2, d2 = map(int, data['to_date'].split('-'))
        end_date = date(y2, m2, d2)

        try:
            exporter = ExcelExporter(class_id, class_name, start_date, end_date)
            exporter.generate(
                filepath=path,
                include_attendance=data['include_attendance'],
                include_tests=data['include_tests'],
                include_fees=data['include_fees'],
            )

            showMessage(self, "Success", "Excel exported successfully!")

        except Exception as e:
            print("Export Error:", e)
            showMessage(self, "Error", f"Failed to export excel.\n{e}")

    def exportPdf(self, data):
        print("Generating PDF...")

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
        self.loadStudents()
