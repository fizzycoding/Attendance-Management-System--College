from PySide6.QtWidgets import QDialog

from ui.components.edit_name_popup import Ui_EditNamePopup  # adjust import path


class EditNamePopup(QDialog):

    def __init__(
            self,
            title: str = "Edit",
            field_label: str = "Name",
            placeholder: str = "",
            default_value: str = "",
            min_length: int = 1,
            max_length: int = 50,
            parent=None,
    ):
        super().__init__(parent)
        self.ui = Ui_EditNamePopup()
        self.ui.setupUi(self)
        self._min_length = min_length
        self._max_length = max_length
        self.setWindowTitle(title)
        self.setModal(True)
        self.ui.title_label.setText(title)
        self.ui.field_label.setText(field_label)
        self.ui.name_input.setPlaceholderText(placeholder)
        self.ui.name_input.setText(default_value)
        self.ui.error_label.setText("")

        self.ui.name_input.setMaxLength(max_length)
        self.ui.name_input.setFocus()
        self.ui.name_input.selectAll()

        # events
        self.ui.btn_close.clicked.connect(self.reject)
        self.ui.btn_save.clicked.connect(self._handle_save)
        self.ui.name_input.returnPressed.connect(self._handle_save)

    def _handle_save(self):
        value = self.ui.name_input.text().strip()

        if len(value) < self._min_length:
            self.ui.error_label.setText(f"Minimum {self._min_length} character required.")
            return

        if len(value) > self._max_length:
            self.ui.error_label.setText(f"Maximum {self._max_length} characters allowed.")
            return

        self.ui.error_label.setText("")
        self.accept()

    def get_value(self) -> str:
        return self.ui.name_input.text().strip()
