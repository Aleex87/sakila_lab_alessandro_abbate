import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path

# source path
SQLITE_PATH = Path(__file__).parent / "sqlite-sakila.db"
# destination path and create the sakila.duckdb
DUCKDB_PATH = Path(__file__).parent / "sakila.duckdb"

# the source for a sqlite data
source = sql_database(credentials=f"sqlite:///{SQLITE_PATH}", schema="main")

# build a pipeline and writing to a DuckDB file
pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_to_duckdb",
# writing to a duckdb and add a staging tabel
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)),
# sett all the data in a new shema (staging)    
    dataset_name="staging",
)

# run the pipline for load
load_info = pipeline.run(source, write_disposition="replace")

print(load_info)
