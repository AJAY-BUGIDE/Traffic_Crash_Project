import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2193@localhost:3306/traffic_crash_db"
)

# 1
def top_dangerous_weather_crash():
    query = """
    SELECT
        WEATHER_CONDITION,
        FIRST_CRASH_TYPE,
        COUNT(*) AS total_crashes
    FROM traffic_crashes
    GROUP BY WEATHER_CONDITION, FIRST_CRASH_TYPE
    ORDER BY total_crashes DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 2
def top_streets():
    query = """
    SELECT
        STREET_NAME,
        SUM(INJURIES_TOTAL) AS total_injuries
    FROM traffic_crashes
    GROUP BY STREET_NAME
    ORDER BY total_injuries DESC
    LIMIT 10
    """
    return pd.read_sql(query, engine)

# 3
def injury_percentage_by_crash():
    query = """
    SELECT
        FIRST_CRASH_TYPE,
        COUNT(CASE WHEN INJURIES_TOTAL > 0 THEN 1 END)
        *100.0/COUNT(*) AS injury_percentage
    FROM traffic_crashes
    GROUP BY FIRST_CRASH_TYPE
    ORDER BY injury_percentage DESC
    """
    return pd.read_sql(query, engine)

# 4
def peak_crash_hour_month():
    query = """
    WITH monthly_crashes AS (
        SELECT
            CRASH_MONTH,
            CRASH_HOUR,
            COUNT(*) AS total_crashes,
            RANK() OVER(
                PARTITION BY CRASH_MONTH
                ORDER BY COUNT(*) DESC
            ) AS rnk
        FROM traffic_crashes
        GROUP BY CRASH_MONTH, CRASH_HOUR
    )
    SELECT *
    FROM monthly_crashes
    WHERE rnk = 1
    """
    return pd.read_sql(query, engine)

# 5
def night_time_causes():
    query = """
    SELECT
        PRIM_CONTRIBUTORY_CAUSE,
        COUNT(*) AS total_crashes
    FROM traffic_crashes
    WHERE CRASH_HOUR >= 18
    GROUP BY PRIM_CONTRIBUTORY_CAUSE
    ORDER BY total_crashes DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 6
def lighting_injuries():
    query = """
    SELECT
        LIGHTING_CONDITION,
        AVG(INJURIES_TOTAL) AS avg_injuries
    FROM traffic_crashes
    GROUP BY LIGHTING_CONDITION
    ORDER BY avg_injuries DESC
    """
    return pd.read_sql(query, engine)

# 7
def traffic_control_injuries():
    query = """
    SELECT
        TRAFFIC_CONTROL_DEVICE,
        AVG(INJURIES_TOTAL) AS avg_injuries
    FROM traffic_crashes
    GROUP BY TRAFFIC_CONTROL_DEVICE
    ORDER BY avg_injuries DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 8
def hotspot_locations():
    query = """
    SELECT
        LATITUDE,
        LONGITUDE,
        COUNT(*) AS total_crashes
    FROM traffic_crashes
    GROUP BY LATITUDE, LONGITUDE
    ORDER BY total_crashes DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 9
def injury_rate_streets():
    query = """
    SELECT
        STREET_NAME,
        SUM(INJURIES_TOTAL)/COUNT(*) AS injury_rate,
        COUNT(*) AS total_crashes
    FROM traffic_crashes
    GROUP BY STREET_NAME
    HAVING COUNT(*) > 100
    ORDER BY injury_rate DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 10
def common_crash_type_year():
    query = """
    WITH yearly_crashes AS (
        SELECT
            year,
            FIRST_CRASH_TYPE,
            COUNT(*) AS total_crashes,
            RANK() OVER(
                PARTITION BY year
                ORDER BY COUNT(*) DESC
            ) AS rnk
        FROM traffic_crashes
        GROUP BY year, FIRST_CRASH_TYPE
    )
    SELECT *
    FROM yearly_crashes
    WHERE rnk = 1
    """
    return pd.read_sql(query, engine)

# 11
def crash_day_average():
    query = """
    SELECT
        CRASH_DAY_OF_WEEK,
        COUNT(*)/24.0 AS avg_crashes_per_hour
    FROM traffic_crashes
    GROUP BY CRASH_DAY_OF_WEEK
    ORDER BY avg_crashes_per_hour DESC
    """
    return pd.read_sql(query, engine)

# 12
def high_risk_time_slots():
    query = """
    SELECT
        CASE
            WHEN CRASH_HOUR BETWEEN 5 AND 11 THEN 'Morning'
            WHEN CRASH_HOUR BETWEEN 12 AND 16 THEN 'Afternoon'
            WHEN CRASH_HOUR BETWEEN 17 AND 20 THEN 'Evening'
            ELSE 'Night'
        END AS time_bucket,
        SUM(INJURIES_TOTAL) AS total_injuries
    FROM traffic_crashes
    GROUP BY time_bucket
    ORDER BY total_injuries DESC
    """
    return pd.read_sql(query, engine)

# 13
def top_3_causes():
    query = """
    WITH ranked_causes AS (
        SELECT
            FIRST_CRASH_TYPE,
            PRIM_CONTRIBUTORY_CAUSE,
            COUNT(*) AS total_crashes,
            ROW_NUMBER() OVER(
                PARTITION BY FIRST_CRASH_TYPE
                ORDER BY COUNT(*) DESC
            ) AS rn
        FROM traffic_crashes
        GROUP BY FIRST_CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE
    )
    SELECT *
    FROM ranked_causes
    WHERE rn <= 3
    """
    return pd.read_sql(query, engine)

# 14
def yoy_growth():
    query = """
    WITH yearly_counts AS (
        SELECT
            year,
            COUNT(*) AS total_crashes
        FROM traffic_crashes
        GROUP BY year
    )
    SELECT
        year,
        total_crashes,
        LAG(total_crashes)
        OVER(ORDER BY year) AS previous_year
    FROM yearly_counts
    """
    return pd.read_sql(query, engine)

# 15
def hotspot_zones():
    query = """
    SELECT
        ROUND(LATITUDE,2) AS lat_zone,
        ROUND(LONGITUDE,2) AS long_zone,
        COUNT(*) AS total_crashes
    FROM traffic_crashes
    GROUP BY lat_zone, long_zone
    ORDER BY total_crashes DESC
    LIMIT 10
    """
    return pd.read_sql(query, engine)