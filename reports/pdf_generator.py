from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_pdf(report, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for section, content in report.items():
        story.append(Paragraph(f"<b>{section}</b>", styles["Heading2"]))
        story.append(Spacer(1, 8))
        story.append(Paragraph(str(content), styles["Normal"]))
        story.append(Spacer(1, 14))

    doc.build(story)
