from PySide6.QtWidgets import QFrame
from datetime import datetime

from ui.components.fee_transaction_card import Ui_FeeTransactionCard  # adjust path


class FeeTransactionCardController(QFrame, Ui_FeeTransactionCard):
    def __init__(self, amount: float, created_at: str, title: str = "Fees paid", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_title.setText(title)
        try:
            amt = float(amount)
            if amt.is_integer():
                self.label_amount.setText(f"₹{int(amt)}")
            else:
                self.label_amount.setText(f"₹{amt:.2f}")
        except:
            self.label_amount.setText("₹0")
        try:
            dt = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
            self.label_datetime.setText(dt.strftime("%d %b %Y • %I:%M %p"))
        except:
            self.label_datetime.setText(created_at or "-- / -- / --")
