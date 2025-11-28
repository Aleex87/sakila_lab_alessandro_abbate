import os
import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path

# --- Path to the file ---
BASE_PATH = Path(__file__).parent
DATA_PATH = BASE_PATH / "data"

SQLITE_PATH = DATA_PATH / "sqlite-sakila.db"
DUCKDB_PATH = DATA_PATH / "sakila.duckdb"

# --- Config destination in duckdb
os.environ["DESTINATION__DUCKDB__CREDENTIALS__DATABASE"] = str(DUCKDB_PATH)

# --- the source 
source = sql_database(
    credentials=f"sqlite:///{SQLITE_PATH}",
    schema="main"   
# sqlite need for identify which kind of file 
# :/// means local file
#  {SQLITE_PATH} is the path to the db
)

# --- Create a pipeline ---
pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_duckdb",
    destination="duckdb",     
    dataset_name="staging"    
)

# --- Execution loadin all in duckdb ---
load_info = pipeline.run(source, write_disposition="replace")

print(load_info)
