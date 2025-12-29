from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QMessageBox

from controllers.create_test_popup_controller import CreateTestPopup
from controllers.test_card_controller import TestCardController
from database.database import getDB
from ui.test_results_ui import Ui_tests_page
from utils.constants import ROLE
from utils.message import showMessage


class TestResultController(QWidget):
    def __init__(self, user, testDetailOpenFn):
        super().__init__()
        self.ui = Ui_tests_page()
        self.ui.setupUi(self)
        self.user = user
        self.testDetailOpenFn = testDetailOpenFn

        # 1. Load Classes first (Populate dropdown)
        self.loadClasses()

        # 2. Connect Signals
        if user["role"] == ROLE.STUDENT:
            self.ui.btn_new_test.hide()
        else:
            self.ui.btn_new_test.show()
            self.ui.btn_new_test.clicked.connect(self.showCreateTestPopup)
        self.ui.dropdown_classes.currentIndexChanged.connect(self.loadTests)


    def loadClasses(self):
        self.ui.dropdown_classes.blockSignals(True)  # Prevent reload while adding items
        self.ui.dropdown_classes.clear()

        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT id, class_name FROM classes WHERE created_by=?"
            cursor.execute(query, (self.user["id"],))
            rows = cursor.fetchall()

            if not rows:
                self.ui.dropdown_classes.addItem("No Classes Found", {"id": None})
            else:
                for row in rows:
                    # row[0] is id, row[1] is class_name
                    classData = {"id": row[0]}
                    self.ui.dropdown_classes.addItem(row[1], classData)

        except Exception as e:
            print("Error loading classes:", e)
        finally:
            cursor.close()
            db.close()
            self.ui.dropdown_classes.blockSignals(False)

            # Manually trigger load for the first item
            self.loadTests()

    def showCreateTestPopup(self):
        current_data = self.ui.dropdown_classes.currentData()
        if not current_data or current_data["id"] is None:
            showMessage(self, "Error", "Please select a class first!", QMessageBox.Icon.Warning)
            return

        popup = CreateTestPopup(self)

        if popup.exec():
            name = popup.getTestName()
            max_marks = popup.getMaxMarks()
            pass_marks = popup.getPassingMarks()
            date = popup.getDate()

            db = getDB()
            cursor = db.cursor()
            classId = current_data["id"]

            try:
                query = """
                    INSERT INTO tests (class_id, test_name, max_marks, passing_marks, test_date)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (classId, name, max_marks, pass_marks, date))
                db.commit()

                showMessage(self, "Success", f"Test '{name}' created successfully!")
                self.loadTests()

            except Exception as e:
                db.rollback()
                print(f"Error creating test: {e}")
                showMessage(self, "Error", "Failed to create test.")
            finally:
                cursor.close()
                db.close()

    def loadTests(self):
        # 1. Clear existing cards
        while self.ui.testsLayout.count():
            item = self.ui.testsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # 2. Get Selected Class
        current_data = self.ui.dropdown_classes.currentData()
        if not current_data or current_data["id"] is None:
            self.ui.content_stack.setCurrentWidget(self.ui.page_no_test)
            return

        class_id = current_data['id']

        db = getDB()
        cursor = db.cursor()
        try:
            # 3. Fetch Tests
            query = "SELECT * FROM tests WHERE class_id = ? ORDER BY id DESC"
            cursor.execute(query, (class_id,))
            rows = cursor.fetchall()

            if not rows:
                self.ui.content_stack.setCurrentWidget(self.ui.page_no_test)
            else:
                self.ui.content_stack.setCurrentWidget(self.ui.page_list)

                for row in rows:
                    # Handle Tuple (sqlite default) vs Dictionary cursor
                    if isinstance(row, tuple):
                        t_id = row[0]
                        # skip class_id at index 1
                        t_name = row[2]
                        t_max = row[3]
                        t_pass = row[4]
                        t_date = row[5]
                    else:
                        t_id = row['id']
                        t_name = row['test_name']
                        t_max = row['max_marks']
                        t_pass = row['passing_marks']
                        t_date = row['test_date']

                    # Create and Add Card
                    card = TestCardController(t_id, t_name, t_max, t_pass, t_date, self.user["role"],
                                              self.testDetailOpenFn)
                    # card.clicked.connect(self.openTestMarks) # Future feature
                    card.deleted.connect(self.loadTests)  # Refresh if deleted
                    self.ui.testsLayout.addWidget(card)

            # Add Spacer at bottom
            spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.testsLayout.addItem(spacer)

        except Exception as e:
            print(f"Error loading tests: {e}")
        finally:
            cursor.close()
            db.close()

    def refresh(self):
        current_data = self.ui.dropdown_classes.currentData()
        current_class_id = current_data['id'] if current_data else None
        self.ui.dropdown_classes.blockSignals(True)
        self.loadClasses()

        found_old_class = False
        if current_class_id:
            for i in range(self.ui.dropdown_classes.count()):
                item_data = self.ui.dropdown_classes.itemData(i)
                if item_data and item_data['id'] == current_class_id:
                    self.ui.dropdown_classes.setCurrentIndex(i)
                    found_old_class = True
                    break

        if not found_old_class and self.ui.dropdown_classes.count() > 0:
            self.ui.dropdown_classes.setCurrentIndex(0)
        self.ui.dropdown_classes.blockSignals(False)
        self.loadTests()
