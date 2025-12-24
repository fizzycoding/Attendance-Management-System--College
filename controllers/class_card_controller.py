from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

from ui.components.class_card_ui import Ui_class_card
from utils.constants import ROLE


class ClassCardController(QFrame, Ui_class_card):
    clicked = Signal(str)

    def __init__(self, classId, className, total, present, absent, role=ROLE.TEACHER):
        super().__init__()
        self.setupUi(self)
        self.classId = classId
        self.class_name.setText(className)
        self.total_user_label.setText(str(total))
        self.present_label.setText(str(present))
        self.absent_label.setText(str(absent))
        if role == ROLE.STUDENT:
            self.btn_delete.hide()
        else:
            self.btn_delete.show()
            self.btn_delete.clicked.connect(self.deleteClass)

    def deleteClass(self):
        print("CLass to delete: ", self.classId)
        pass

    def mousePressEvent(self, event):
        self.clicked.emit(self.classId)
        super().mousePressEvent(event)
