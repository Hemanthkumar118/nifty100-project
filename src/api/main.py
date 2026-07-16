from fastapi import FastAPI
from src.api.database import run_query
import pandas as pd
app = FastAPI(
    title="Nifty100 Financial Intelligence API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Nifty100 API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/companies")
def companies():

    df = run_query(
        "SELECT * FROM companies"
    )

    return df.to_dict(
        orient="records"
    )


@app.get("/financial_ratios")
def ratios():

    df = run_query(
        "SELECT * FROM financial_ratios"
    )

    return df.to_dict(
        orient="records"
    )

@app.get("/company/{company_id}")
def company(company_id: str):

    query = f"""
    SELECT *
    FROM companies
    WHERE company_id='{company_id}'
    """

    df = run_query(query)

    return df.to_dict(
        orient="records"
    )


@app.get("/screener")
def screener():

    query = """
    SELECT *
    FROM financial_ratios
    WHERE return_on_equity_pct >= 15
      AND debt_to_equity <= 1
    """

    df = run_query(query)

    return df.to_dict(
        orient="records"
    )

@app.get("/top_roe")
def top_roe():

    query = """
    SELECT *
    FROM financial_ratios
    ORDER BY return_on_equity_pct DESC
    LIMIT 10
    """

    df = run_query(query)

    return df.to_dict(
        orient="records"
    )

@app.get("/clusters")
def clusters():

    df = pd.read_csv(
        "output/cluster_labels.csv"
    )

    return df.to_dict(
        orient="records"
    )

@app.get("/sector/{sector}")
def sector(sector: str):

    query = f"""
    SELECT *
    FROM companies
    WHERE broad_sector='{sector}'
    """

    df = run_query(query)

    return df.to_dict(
        orient="records"
    )