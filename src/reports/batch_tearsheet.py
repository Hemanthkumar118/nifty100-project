import os
import pandas as pd

from src.reports.tearsheet import create_tearsheet


def generate_all_tearsheets():

    os.makedirs("reports/tearsheets", exist_ok=True)

    companies_file = "data/processed/companies.csv"

    if not os.path.exists(companies_file):
        print("companies.csv not found.")
        return

    companies = pd.read_csv(companies_file)

    if "company_name" not in companies.columns:
        print("company_name column not found.")
        return

    total = len(companies)

    print("=" * 60)
    print("BATCH PDF GENERATION")
    print("=" * 60)

    for i, company in enumerate(companies["company_name"], start=1):

        company = str(company).strip()

    print(f"[{i}/{total}] Generating {company}...")

    create_tearsheet(company)