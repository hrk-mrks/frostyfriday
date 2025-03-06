import snowflake.snowpark as snowpark
import pandas as pd

def main(session: snowpark.Session): 
    data = {
    "STATEMENT1": ["We", "Love", "Frosty", "Friday"],
    "STATEMENT2": ["Python", "Worksheets", "Are", "Cool"]
    }
    df = pd.DataFrame(data)
    df_sp = session.create_dataframe(df)

    return df_sp