from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.record_payment_popup_controller import RecordPaymentPopupController
from controllers.set_fee_popup_controller import SetFeePopupController
from controllers.student_fee_row_controller import StudentFeeRowController
from database.database import getDB
from ui.fee_payments_ui import Ui_FeesPaymentPage
from utils.message import showMessage, showErrorMessage


class FeesPaymentController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_FeesPaymentPage()
        self.ui.setupUi(self)

        self.user = user
        self.rows = []

        self.ui.dropdown_classes.currentIndexChanged.connect(self.loadStudents)
        self.ui.input_searchStudent.textChanged.connect(self.applyFilters)
        self.ui.dropdown_statusFilter.currentTextChanged.connect(self.applyFilters)
        self.ui.set_fees_btn.clicked.connect(self.openSetFeePopup)
        self.loadClasses()

    def refresh(self):
        self.loadClasses()

    def openSetFeePopup(self):
        popup = SetFeePopupController(self)
        popup.feeSet.connect(self.setFeesForAll)
        popup.exec()

    def setFeesForAll(self, amount):
        class_id = self.ui.dropdown_classes.currentData()
        if not class_id:
            return

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("SELECT id FROM class_members WHERE class_id = ?", (class_id,))
            members = cursor.fetchall()

            if not members:
                return

            for m in members:
                member_id = m["id"]

                cursor.execute("""
                    INSERT OR IGNORE INTO fees (class_id, member_id, total_fee, paid_fee)
                    VALUES (?, ?, ?, 0)
                """, (class_id, member_id, amount))

                cursor.execute("""
                    UPDATE fees
                    SET total_fee = ?
                    WHERE class_id = ? AND member_id = ?
                """, (amount, class_id, member_id))

            db.commit()
            self.loadStudents()

        except Exception as e:
            print("Set fees for all error:", e)

        finally:
            cursor.close()
            db.close()

    def clearSearch(self):
        self.ui.input_searchStudent.setText("")
        self.ui.dropdown_statusFilter.setCurrentText("All")
        self.applyFilters()

    def setCards(self, total_fees: float, paid_amount: float, pending_amount: float):
        self.ui.label_totalFeesValue.setText(f"₹{total_fees:,.0f}")
        self.ui.label_paidAmountValue.setText(f"₹{paid_amount:,.0f}")
        self.ui.label_pendingAmountValue.setText(f"₹{pending_amount:,.0f}")

    def loadClasses(self):
        self.ui.dropdown_classes.blockSignals(True)
        self.ui.dropdown_classes.clear()

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute(
                "SELECT id, class_name FROM classes WHERE created_by = ?",
                (self.user["id"],)
            )
            classes = cursor.fetchall()

            if not classes:
                self.ui.dropdown_classes.addItem("No Classes Found", None)
                self.ui.dropdown_classes.blockSignals(False)
                self.ui.content_stack.setCurrentWidget(self.ui.no_student_page)
                return

            for cls in classes:
                self.ui.dropdown_classes.addItem(cls["class_name"], cls["id"])

            self.ui.dropdown_classes.blockSignals(False)
            self.ui.dropdown_classes.setCurrentIndex(0)

            self.loadStudents()

        except Exception as e:
            print(f"Error loading classes: {e}")
            self.ui.dropdown_classes.blockSignals(False)

        finally:
            cursor.close()
            db.close()

    def clearStudentRows(self):
        self.rows = []

        while self.ui.studentsLayout.count():
            item = self.ui.studentsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def loadStudents(self):
        self.clearStudentRows()

        class_id = self.ui.dropdown_classes.currentData()

        if not class_id:
            self.ui.content_stack.setCurrentWidget(self.ui.no_student_page)
            self.setCards(0, 0, 0)
            return

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("""
                SELECT 
                    cm.id AS member_id,
                    u.id AS student_user_id,
                    COALESCE(cm.guest_name, u.name) AS student_name,
                    u.username AS username,

                    COALESCE(f.total_fee, 0) AS total_fee,
                    COALESCE(f.paid_fee, 0) AS paid_fee

                FROM class_members cm
                LEFT JOIN users u ON u.id = cm.student_id
                LEFT JOIN fees f ON f.member_id = cm.id AND f.class_id = cm.class_id

                WHERE cm.class_id = ?
                ORDER BY COALESCE(cm.guest_name, u.name) ASC
            """, (class_id,))

            students = cursor.fetchall()

            if not students:
                self.ui.content_stack.setCurrentWidget(self.ui.no_student_page)
                self.setCards(0, 0, 0)
                return

            self.ui.content_stack.setCurrentWidget(self.ui.page_list)

            total_sum = 0
            paid_sum = 0

            for i,s in enumerate(students):
                total_fee = float(s["total_fee"])
                paid_fee = float(s["paid_fee"])

                total_sum += total_fee
                paid_sum += paid_fee

                row = StudentFeeRowController()

                row.setData(
                    sNo=i+1,
                    student_id=str(s["member_id"]),
                    student_name=s["student_name"] if s["student_name"] else "Guest Student",
                    total_fee=total_fee,
                    paid_fee=paid_fee
                )

                row.paymentClicked.connect(self.onRecordPaymentClicked)

                self.rows.append(row)
                self.ui.studentsLayout.addWidget(row)

            pending_sum = max(0, total_sum - paid_sum)
            self.setCards(total_sum, paid_sum, pending_sum)
            self.applyFilters()
            spacer = QSpacerItem(
                20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
            self.ui.studentsLayout.addItem(spacer)
        except Exception as e:
            print(f"Error loading students: {e}")
            self.ui.content_stack.setCurrentWidget(self.ui.no_student_page)

        finally:
            cursor.close()
            db.close()

    def applyFilters(self):
        query = self.ui.input_searchStudent.text().strip().lower()
        status_filter = self.ui.dropdown_statusFilter.currentText().strip()

        for row in self.rows:
            data = row.student_data

            name = str(data.get("student_name", "")).lower()
            sid = str(data.get("student_id", "")).lower()

            total_fee = float(data.get("total_fee", 0))
            paid_fee = float(data.get("paid_fee", 0))

            if paid_fee <= 0:
                status = "Unpaid"
            elif paid_fee >= total_fee:
                status = "Paid"
            else:
                status = "Partial"

            match_search = (query in name) or (query in sid)
            match_status = (status_filter == "All") or (status_filter == status)

            row.setVisible(match_search and match_status)

    def onRecordPaymentClicked(self, student_data: dict):
        class_id = self.ui.dropdown_classes.currentData()
        if not class_id:
            return

        member_id = int(student_data["student_id"])
        student_name = student_data["student_name"]
        pending_fee = float(student_data["pending_fee"])

        if pending_fee <= 0:
            showMessage(self, "No Pending", "This student has no pending fees.")
            return

        popup = RecordPaymentPopupController(
            parent=self,
            student_name=student_name,
            pending_amount=pending_fee
        )

        def save_payment(amount_paid: float):
            db = getDB()
            cursor = db.cursor()
            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO fees (class_id, member_id, total_fee, paid_fee)
                    VALUES (?, ?, 0, 0)
                """, (class_id, member_id))

                cursor.execute("""
                    UPDATE fees
                    SET paid_fee = paid_fee + ?
                    WHERE class_id = ? AND member_id = ?
                """, (amount_paid, class_id, member_id))

                db.commit()
                self.loadStudents()

            except Exception as e:
                print("Record payment error:", e)
                showErrorMessage(self, "Error", "Failed to record payment.")
            finally:
                cursor.close()
                db.close()

        popup.paymentRecorded.connect(save_payment)
        popup.exec()
