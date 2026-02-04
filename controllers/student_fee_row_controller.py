from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

from ui.components.student_fee_row import Ui_StudentFeeRow


class StudentFeeRowController(QFrame):
    paymentClicked = Signal(dict)  # emits student data when button clicked

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_StudentFeeRow()
        self.ui.setupUi(self)

        self.student_data = {}

        self.ui.btn_recordPayment.clicked.connect(self._handle_payment_click)

    def setData(
            self, sNo: int, student_id: str, student_name: str, total_fee: float, paid_fee: float
    ):
        pending_fee = max(0.0, total_fee - paid_fee)
        self.student_data = {
            "sNo": sNo,
            "student_id": student_id,
            "student_name": student_name,
            "total_fee": total_fee,
            "paid_fee": paid_fee,
            "pending_fee": pending_fee,
        }

        # UI labels
        self.ui.label_sno.setText(f"{sNo}. ")
        self.ui.label_studentName.setText(student_name)
        self.ui.label_totalFee.setText(f"₹{total_fee:,.0f}")
        self.ui.label_paidFee.setText(f"₹{paid_fee:,.0f}")
        self.ui.label_pendingFee.setText(f"₹{pending_fee:,.0f}")

        # Status logic
        if paid_fee <= 0:
            status = "Unpaid"
        elif paid_fee >= total_fee:
            status = "Paid"
        else:
            status = "Partial"

        self._setStatusBadge(status)

    def _setStatusBadge(self, status: str):
        self.ui.label_status.setText(status)

        # Default style base
        base = """
QLabel {
    border-radius: 10px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 600;
}
"""

        if status == "Paid":
            self.ui.label_status.setStyleSheet(
                base
                + """
QLabel {
    background-color: #bbf1d0;
    color: #168a3a;
}
"""
            )
        elif status == "Partial":
            self.ui.label_status.setStyleSheet(
                base
                + """
QLabel {
    background-color: #f6dfbe;
    color: #b86b00;
}
"""
            )
        else:  # Unpaid
            self.ui.label_status.setStyleSheet(
                base
                + """
QLabel {
    background-color: #fbc8c8;
    color: #c62828;
}
"""
            )

    def _handle_payment_click(self):
        self.paymentClicked.emit(self.student_data)
