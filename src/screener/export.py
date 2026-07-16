import os


def export_excel(df):

    os.makedirs("output", exist_ok=True)

    file = "output/screener_output.xlsx"

    df.to_excel(
        file,
        index=False
    )

    print("Exported:", file)