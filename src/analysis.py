import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://root:2193@localhost:3306/traffic_crash_db'
)

def top_streets():

    query = """
    SELECT
        STREET_NAME,
        COUNT(*) AS total_crashes

    FROM traffic_crashes

    GROUP BY STREET_NAME

    ORDER BY total_crashes DESC

    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    return df