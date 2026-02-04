from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel

from controllers.fee_transaction_card_controller import FeeTransactionCardController
from database.database import getDB
from ui.student_fees_page import Ui_StudentFeesPage


class StudentFeesPageController(QWidget, Ui_StudentFeesPage):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        self.user = user
        self.current_class_id = None
        self.current_member_id = None
        self.current_fee_id = None

        self.dropdown_classes.currentIndexChanged.connect(self.onClassChanged)
        self.btn_refresh.clicked.connect(self.refreshCurrent)

        self.loadClasses()

    def refresh(self):
        self.loadClasses()
        self.loadMyFees()
        self.loadMyTransactions()

    # --------------------- LOAD CLASSES ---------------------
    def loadClasses(self):
        self.dropdown_classes.blockSignals(True)
        self.dropdown_classes.clear()

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("""
                SELECT 
                    c.id AS class_id,
                    c.class_name,
                    cm.id AS member_id
                FROM class_members cm
                JOIN classes c ON c.id = cm.class_id
                WHERE cm.student_id = ?
                ORDER BY c.class_name ASC
            """, (self.user["id"],))

            rows = cursor.fetchall()

            if not rows:
                self.dropdown_classes.addItem("No Classes", None)
                self.dropdown_classes.setEnabled(False)

                self.setFeesUI(0, 0, 0)
                self.clearHistoryUI("No transactions")
                return

            self.dropdown_classes.setEnabled(True)

            for class_id, class_name, member_id in rows:
                self.dropdown_classes.addItem(class_name, (class_id, member_id))

        except Exception as e:
            print("Failed to load classes:", e)
            self.dropdown_classes.addItem("Error loading classes", None)
            self.dropdown_classes.setEnabled(False)
        finally:
            cursor.close()
            db.close()

        self.dropdown_classes.blockSignals(False)

        if self.dropdown_classes.count() > 0:
            self.dropdown_classes.setCurrentIndex(0)
            self.onClassChanged()

    # --------------------- CLASS CHANGE ---------------------
    def onClassChanged(self):
        data = self.dropdown_classes.currentData()

        if not data:
            return

        class_id, member_id = data
        self.current_class_id = class_id
        self.current_member_id = member_id

        self.loadMyFees()
        self.loadMyTransactions()

    def refreshCurrent(self):
        if not self.current_class_id or not self.current_member_id:
            return

        self.loadMyFees()
        self.loadMyTransactions()

    # --------------------- FEES SUMMARY ---------------------
    def loadMyFees(self):
        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("""
                SELECT id, total_fee, paid_fee
                FROM fees
                WHERE class_id = ? AND member_id = ?
            """, (self.current_class_id, self.current_member_id))

            row = cursor.fetchone()

            if not row:
                self.current_fee_id = None
                self.setFeesUI(0, 0, 0)
                return

            fee_id, total_fee, paid_fee = row
            self.current_fee_id = fee_id

            total_fee = float(total_fee or 0)
            paid_fee = float(paid_fee or 0)
            pending_fee = max(total_fee - paid_fee, 0)

            self.setFeesUI(total_fee, paid_fee, pending_fee)

        except Exception as e:
            print("Failed to load student fees:", e)
            self.setFeesUI(0, 0, 0)
        finally:
            cursor.close()
            db.close()

    def setFeesUI(self, total_fee: float, paid_fee: float, pending_fee: float):
        self.label_totalFeesValue.setText(f"₹{total_fee:g}")
        self.label_paidAmountValue.setText(f"₹{paid_fee:g}")
        self.label_pendingAmountValue.setText(f"₹{pending_fee:g}")

    # --------------------- TRANSACTION HISTORY ---------------------
    def loadMyTransactions(self):
        if not self.current_fee_id:
            self.clearHistoryUI("No transactions yet.")
            return

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("""
                SELECT amount, created_at
                FROM fee_transactions
                WHERE fee_id = ?
                ORDER BY created_at DESC
            """, (self.current_fee_id,))

            rows = cursor.fetchall()

            if not rows:
                self.clearHistoryUI("No transactions yet.")
                return

            self.clearHistoryUI()

            spacer_index = self.history_list_layout.count() - 1

            for amount, created_at in rows:
                card = FeeTransactionCardController(
                    amount=amount,
                    created_at=created_at,
                    title="Fees paid"
                )
                self.history_list_layout.insertWidget(spacer_index, card)
                spacer_index += 1

        except Exception as e:
            print("Failed to load transactions:", e)
            self.clearHistoryUI("Failed to load transactions.")
        finally:
            cursor.close()
            db.close()

    def clearHistoryUI(self, message: str = None):
        """
        Clears history cards and optionally shows a message label.
        """
        layout = self.history_list_layout

        # Remove all widgets except last spacer
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        if message:
            msg = QLabel(message)
            msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
            msg.setStyleSheet("""
                QLabel{
                    color: rgb(120,120,120);
                    font-size: 13px;
                    font-weight: 600;
                    padding: 20px;
                }
            """)
            # insert message before spacer
            layout.insertWidget(layout.count() - 1, msg)
