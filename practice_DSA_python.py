# import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# print(f"path: {basedir}")

from fpdf import FPDF
from datetime import datetime


class PDF(FPDF):
    def header(self):
        # Dummy Organization Name
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Dummy Organization Name", 0, 1, "C")

    def footer(self):
        # Page number
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


# Create instance of PDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Proof of National Insurance Number", 0, 1, "C")
pdf.ln(10)

# Document details
pdf.set_font("Arial", size=12)
details = [
    ("Document Type:", "National Insurance Number Card"),
    ("NI Number:", "AB123456C"),
    ("Name:", "John Doe"),
    ("Date of Birth:", "01/01/1990"),
    ("Address:", "123 Maple Street, London, UK, NW1 6XE"),
    ("Issued by:", "HM Revenue and Customs (HMRC)"),
    ("Date of Issue:", "01/01/2025"),
]

for label, value in details:
    pdf.cell(50, 10, label, 0, 0)
    pdf.cell(0, 10, value, 0, 1)
pdf.ln(10)

# Notes
notes = (
    "Notes:\n"
    "- This document serves as proof of your National Insurance number.\n"
    "- Keep this document safe for your records.\n"
    "- Do not share your NI number publicly to prevent identity theft."
)
pdf.multi_cell(0, 10, notes)
pdf.ln(10)

# Website link
pdf.cell(
    0,
    10,
    "For any queries, visit: www.gov.uk/national-insurance",
    ln=True,
    link="http://www.gov.uk/national-insurance",
)
pdf.ln(10)

# Signature
pdf.cell(50, 10, "Signature:", 0, 0)
pdf.cell(0, 10, "John Doe", 0, 1)
pdf.ln(10)

# Add stamp with current date and time
stamp_text = f"Approved\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(255, 0, 0)  # Red color for stamp
pdf.set_xy(150, 250)  # Position the stamp
pdf.multi_cell(0, 10, stamp_text, border=1, align="C")

# Output the PDF
pdf_output = "Realistic_Proof_of_NI_Number_with_Stamp.pdf"
pdf.output(pdf_output)

print(f"PDF generated: {pdf_output}")
