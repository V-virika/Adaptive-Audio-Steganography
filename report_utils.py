from fpdf import FPDF
import datetime
from report_utils import create_pdf_report

def create_pdf_report(message, sr, audio_shape, output_path="static/extraction_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Audio Steganography Extraction Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Sample Rate: {sr}", ln=True)
    pdf.cell(200, 10, txt=f"Audio Shape: {audio_shape}", ln=True)
    pdf.cell(200, 10, txt=f"Message Length: {len(message)} characters", ln=True)
    pdf.multi_cell(0, 10, txt=f"Extracted Message:\n{message}")
    
    pdf.output(output_path)
