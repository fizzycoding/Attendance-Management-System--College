from calendar import monthrange
from datetime import date
from datetime import timedelta

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

from database.database import getDB
from utils.constants import ATTENDANCE_STATUS


class ExcelExporter:
    def __init__(self, class_id, class_name, from_date, to_date):
        self.class_id = class_id
        self.class_name = class_name
        self.from_date = from_date
        self.to_date = to_date

        self.COLOR_HEADER_BG = "3388FF"
        self.COLOR_HEADER_TXT = "FFFFFF"

        self.FILL_GREEN = PatternFill(
            start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"
        )
        self.FILL_RED = PatternFill(
            start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"
        )
        self.FILL_GREY = PatternFill(
            start_color="E0E0E0", end_color="E0E0E0", fill_type="solid"
        )

    def generate(
        self, filepath, include_attendance=True, include_tests=True, include_fees=True
    ):
        wb = Workbook()
        wb.remove(wb.active)

        # 1. ATTENDANCE SHEETS (Per Month)
        if include_attendance:
            current = self.from_date.replace(day=1)
            end = self.to_date.replace(day=1)

            while current <= end:
                self._add_monthly_attendance_sheet(wb, current.year, current.month)
                # Next month logic
                next_month = current.replace(day=28) + timedelta(days=4)
                current = next_month.replace(day=1)

        # 2. TEST REPORT SHEET
        if include_tests:
            self._add_test_report_sheet(wb)

        if include_fees:
            self._add_fees_report_sheet(wb)

        wb.save(filepath)

    def _add_monthly_attendance_sheet(self, wb, year, month):
        sheet_name = f"{year}-{month:02d}"
        ws = wb.create_sheet(title=sheet_name)

        db = getDB()
        cursor = db.cursor()
        month_name = date(year, month, 1).strftime("%B %Y")
        title = f"{self.class_name} - Attendance Report - {month_name}"
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=35)
        cell = ws.cell(row=1, column=1, value=title)
        cell.font = Font(size=18, bold=True, color="333333")
        cell.alignment = Alignment(horizontal="center")

        # Fetch Students & Data
        cursor.execute(
            "SELECT c.id, COALESCE(c.guest_name, u.name) FROM class_members c LEFT JOIN users u ON c.student_id = u.id WHERE c.class_id = ? ORDER BY COALESCE(c.guest_name, u.name) ASC",
            (self.class_id,),
        )
        members = cursor.fetchall()

        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-{monthrange(year, month)[1]}"

        cursor.execute(
            """
            SELECT r.member_id, strftime('%d', s.date) as day, r.status 
            FROM attendance_records r JOIN attendance_sessions s ON r.session_id = s.id
            WHERE s.class_id = ? AND s.date BETWEEN ? AND ?
        """,
            (self.class_id, start_date, end_date),
        )

        att_map = {}
        for row in cursor.fetchall():
            m_id, day, status = row[0], int(row[1]), row[2]
            code = (
                "P"
                if status == ATTENDANCE_STATUS.PRESENT
                else "A" if status == ATTENDANCE_STATUS.ABSENT else "-"
            )
            att_map.setdefault(m_id, {})[day] = code

        days_in_month = monthrange(year, month)[1]
        headers = (
            ["S.No", "Name"]
            + [str(d) for d in range(1, days_in_month + 1)]
            + ["Total Present", "Total Absent"]
        )
        ws.append(headers)

        for idx, (mem_id, name) in enumerate(members):
            row_data = [idx + 1, name]
            p_count = 0
            a_count = 0

            for d in range(1, days_in_month + 1):
                stat = att_map.get(mem_id, {}).get(d, "-")
                row_data.append(stat)
                if stat == "P":
                    p_count += 1
                elif stat == "A":
                    a_count += 1

            row_data.append(p_count)
            row_data.append(a_count)
            ws.append(row_data)

        for row in ws.iter_rows(min_row=3, min_col=3, max_col=days_in_month + 2):
            for cell in row:
                if cell.value == "P":
                    cell.fill = self.FILL_GREEN
                elif cell.value == "A":
                    cell.fill = self.FILL_RED

        self._style_headers(ws)
        cursor.close()
        db.close()

    def _add_test_report_sheet(self, wb):
        ws = wb.create_sheet(title="Test Results")
        db = getDB()
        cursor = db.cursor()

        cursor.execute(
            "SELECT id, test_name, max_marks, passing_marks, test_date FROM tests WHERE class_id = ? ORDER BY test_date ASC",
            (self.class_id,),
        )
        tests = cursor.fetchall()

        if not tests:
            ws.append(["No tests found for this class."])
            return

        total_columns = 2 + (len(tests) * 2)

        title = f"{self.class_name} - Test Report"
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=total_columns)
        cell = ws.cell(row=1, column=1, value=title)
        cell.font = Font(size=18, bold=True, color="333333")
        cell.alignment = Alignment(horizontal="center")

        headers = ["S.No", "Name"]
        for t in tests:
            headers.extend([f"{t[1]} (Max: {t[2]})", "Status"])
        ws.append(headers)

        cursor.execute(
            "SELECT c.id, COALESCE(c.guest_name, u.name) FROM class_members c LEFT JOIN users u ON c.student_id = u.id WHERE c.class_id = ? ORDER BY COALESCE(c.guest_name, u.name) ASC",
            (self.class_id,),
        )
        members = cursor.fetchall()

        for idx, (mem_id, name) in enumerate(members):
            row = [idx + 1, name]
            for t in tests:
                cursor.execute(
                    "SELECT marks_obtained FROM test_results WHERE test_id=? AND member_id=?",
                    (t[0], mem_id),
                )
                res = cursor.fetchone()
                if res:
                    status = "Pass" if res[0] >= t[3] else "Fail"
                    row.extend([res[0], status])
                else:
                    row.extend(["-", "Absent"])
            ws.append(row)

        for row in ws.iter_rows(min_row=3, min_col=3):
            for cell in row:
                if cell.value == "Pass":
                    cell.fill = self.FILL_GREEN
                elif cell.value == "Fail":
                    cell.fill = self.FILL_RED
                elif cell.value == "Absent":
                    cell.fill = self.FILL_GREY

        self._style_headers(ws)
        cursor.close()
        db.close()

    def _add_fees_report_sheet(self, wb):
        ws = wb.create_sheet(title="Fees Report")

        db = getDB()
        cursor = db.cursor()

        title = f"{self.class_name} - Fees Report"
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=6)
        cell = ws.cell(row=1, column=1, value=title)
        cell.font = Font(size=18, bold=True, color="333333")
        cell.alignment = Alignment(horizontal="center")

        headers = ["S.No", "Name", "Total Fee", "Paid Fee", "Pending Fee", "Status"]
        ws.append(headers)

        cursor.execute(
            """
            SELECT 
                c.id as member_id,
                COALESCE(c.guest_name, u.name) as name,
                COALESCE(f.total_fee, 0) as total_fee,
                COALESCE(f.paid_fee, 0) as paid_fee
            FROM class_members c
            LEFT JOIN users u ON c.student_id = u.id
            LEFT JOIN fees f ON f.member_id = c.id AND f.class_id = c.class_id
            WHERE c.class_id = ?
            ORDER BY name ASC
        """,
            (self.class_id,),
        )

        members = cursor.fetchall()

        for idx, (member_id, name, total_fee, paid_fee) in enumerate(members):
            pending = float(total_fee) - float(paid_fee)
            if pending < 0:
                pending = 0

            if float(total_fee) == 0 and float(paid_fee) == 0:
                status = "No Fee Set"
            elif pending == 0:
                status = "Paid"
            else:
                status = "Pending"

            ws.append([idx + 1, name, total_fee, paid_fee, pending, status])

        for row in ws.iter_rows(min_row=3, min_col=6, max_col=6):
            for cell in row:
                if cell.value == "Paid":
                    cell.fill = self.FILL_GREEN
                elif cell.value == "Pending":
                    cell.fill = self.FILL_RED
                elif cell.value == "No Fee Set":
                    cell.fill = self.FILL_GREY

        self._style_headers(ws)

        cursor.close()
        db.close()

    def _style_headers(self, ws):
        thin_border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )
        header_font = Font(bold=True, color=self.COLOR_HEADER_TXT)
        header_fill = PatternFill(
            start_color=self.COLOR_HEADER_BG,
            end_color=self.COLOR_HEADER_BG,
            fill_type="solid",
        )

        for cell in ws[2]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.border = thin_border

        for row in ws.iter_rows(min_row=3):
            for cell in row:
                cell.border = thin_border
                cell.alignment = Alignment(horizontal="center", vertical="center")

        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                try:
                    if cell.value:
                        max_len = max(max_len, len(str(cell.value)))
                except:
                    pass
            ws.column_dimensions[col_letter].width = max_len + 3

        ws.column_dimensions["A"].width = 10
