import re
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_tearsheet(company):

    # Remove newline, tabs and extra spaces
    company = str(company).strip()

    # Replace invalid filename characters
    safe_name = re.sub(r'[\\/*?:"<>|\n\r\t]', "_", company)

    pdf = SimpleDocTemplate(
        f"reports/tearsheets/{safe_name}.pdf"
    )

    story = []

    story.append(
        Paragraph(
            "<b>Nifty100 Company Tearsheet</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(f"<b>Company :</b> {company}",
                  styles["Heading2"])
    )

    story.append(
        Paragraph("Financial Snapshot",
                  styles["Heading2"])
    )

    story.append(
        Paragraph("Revenue Growth : Good",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("ROE : Excellent",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("Debt : Low",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("Free Cash Flow : Positive",
                  styles["BodyText"])
    )

    story.append(Spacer(1,25))

    story.append(
        Paragraph("Pros",
                  styles["Heading2"])
    )

    story.append(
        Paragraph("• Strong profitability",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("• Positive cash flow",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("• Low debt",
                  styles["BodyText"])
    )

    story.append(Spacer(1,25))

    story.append(
        Paragraph("Cons",
                  styles["Heading2"])
    )

    story.append(
        Paragraph("• Moderate valuation",
                  styles["BodyText"])
    )

    story.append(
        Paragraph("• Revenue growth slowing",
                  styles["BodyText"])
    )

    pdf.build(story)