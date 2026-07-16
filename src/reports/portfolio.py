from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import os

styles = getSampleStyleSheet()


def create_portfolio_summary():

    os.makedirs("reports/portfolio", exist_ok=True)

    pdf = SimpleDocTemplate(
        "reports/portfolio/portfolio_summary.pdf"
    )

    story = []

    story.append(Paragraph("<b>NIFTY100 PORTFOLIO SUMMARY</b>", styles["Title"]))

    try:
        companies = pd.read_excel("output/valuation_summary.xlsx")

        for _, row in companies.head(92).iterrows():

            story.append(
                Paragraph(
                    f"<b>{row.get('company_name','Company')}</b>",
                    styles["Heading2"]
                )
            )

            story.append(
                Paragraph(
                    f"Sector : {row.get('sector','NA')}",
                    styles["BodyText"]
                )
            )

            story.append(
                Paragraph(
                    f"P/E : {row.get('P/E','NA')}",
                    styles["BodyText"]
                )
            )

            story.append(
                Paragraph(
                    f"P/B : {row.get('P/B','NA')}",
                    styles["BodyText"]
                )
            )

            story.append(
                Paragraph("<br/>", styles["BodyText"])
            )

    except:

        story.append(
            Paragraph(
                "valuation_summary.xlsx not found.",
                styles["BodyText"]
            )
        )

    pdf.build(story)

    print("Portfolio Summary Generated")