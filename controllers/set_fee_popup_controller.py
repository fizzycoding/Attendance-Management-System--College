from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.components.set_fee_popup import Ui_SetFeesPopup
from utils.message import showMessage


class SetFeePopupController(QDialog):
    feeSet = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SetFeesPopup()
        self.ui.setupUi(self)

        self.setWindowTitle("Set fees")

        self.ui.cancelBtn.clicked.connect(self.reject)
        self.ui.setBtn.clicked.connect(self.onSetClicked)
        self.ui.fee_input.returnPressed.connect(self.onSetClicked)

    def onSetClicked(self):
        text = self.ui.fee_input.text().strip()

        if not text:
            showMessage(self, "Invalid Input", "Please enter an amount.")
            return

        try:
            amount = float(text)
            if amount < 0:
                raise ValueError
        except ValueError:
            showMessage(self, "Invalid Input", "Enter a valid positive number.")
            return

        self.feeSet.emit(amount)
        self.accept()
