import pandas as pd

from src.nlp.parser import parse_dataframe


sample = pd.DataFrame({

    "company_id":[1,2,3,4],

    "growth":[

        "10 Years: 21%",

        "5 Years: 18.4%",

        "3 Years: -2%",

        "invalid data"

    ]

})


parsed, failed = parse_dataframe(sample,"growth")

print("="*50)
print("DAY 29 NLP PARSER")
print("="*50)

print(parsed)

print()

print("Failed Rows")

print(failed)