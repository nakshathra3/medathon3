from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class PDFGenerator:
    def __init__(self, patient_info, medicine_history, compliance_stats, notes):
        self.patient_info = patient_info
        self.medicine_history = medicine_history
        self.compliance_stats = compliance_stats
        self.notes = notes

    def generate_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Patient Profile
        c.setFont('Helvetica-Bold', 16)
        c.drawString(100, height - 50, 'Patient Profile')
        c.setFont('Helvetica', 12)
        for idx, (key, value) in enumerate(self.patient_info.items()):
            c.drawString(100, height - 70 - (idx * 20), f'{key}: {value}')

        # Medicine Intake History
        c.setFont('Helvetica-Bold', 16)
        c.drawString(100, height - 150, 'Medicine Intake History')
        c.setFont('Helvetica', 12)
        for idx, entry in enumerate(self.medicine_history):
            c.drawString(100, height - 170 - (idx * 20), f'{entry['timestamp']}: {entry['medicine_name']}')

        # Compliance Statistics
        c.setFont('Helvetica-Bold', 16)
        c.drawString(100, height - 250, 'Compliance Statistics')
        c.setFont('Helvetica', 12)
        for idx, (key, value) in enumerate(self.compliance_stats.items()):
            c.drawString(100, height - 270 - (idx * 20), f'{key}: {value}')

        # Notes Section
        c.setFont('Helvetica-Bold', 16)
        c.drawString(100, height - 350, 'Notes')
        c.setFont('Helvetica', 12)
        c.drawString(100, height - 370, self.notes)

        c.save()  
