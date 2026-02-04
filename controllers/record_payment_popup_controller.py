from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.components.record_payment_popup import Ui_RecordPaymentPopup
from utils.message import showMessage


class RecordPaymentPopupController(QDialog):
    paymentRecorded = Signal(float)

    def __init__(self, parent=None, student_name="--", pending_amount=0):
        super().__init__(parent)
        self.ui = Ui_RecordPaymentPopup()
        self.ui.setupUi(self)

        self.pending_amount = float(pending_amount)

        self.ui.studentNameLabel.setText(f"Student: {student_name}")
        self.ui.pendingAmountLabel.setText(f"Pending: ₹{self.pending_amount:,.0f}")

        self.ui.cancelBtn.clicked.connect(self.reject)
        self.ui.recordBtn.clicked.connect(self.onRecordClicked)
        self.ui.payment_input.returnPressed.connect(self.onRecordClicked)

    def onRecordClicked(self):
        text = self.ui.payment_input.text().strip()

        if not text:
            showMessage(self, "Invalid Input", "Please enter a payment amount.")
            return

        try:
            amount = float(text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            showMessage(self, "Invalid Input", "Enter a valid positive amount.")
            return

        if amount > self.pending_amount:
            showMessage(self, "Too Much", "Amount cannot be greater than pending fees.")
            return

        self.paymentRecorded.emit(amount)
        self.accept()
