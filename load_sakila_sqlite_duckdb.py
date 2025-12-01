import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path

# path
SQLITE_PATH = Path(__file__).parent / "sqlite-sakila.db"
DUCKDB_PATH = Path(__file__).parent / "sakila.duckdb"

# the source
source = sql_database(credentials=f"sqlite:///{SQLITE_PATH}", schema="main")

# build a pipeline writing to a DuckDB file
pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_to_duckdb",
# writing to a duckdb and add a staging tabel
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)),
    dataset_name="staging",
)

# run the process for load
load_info = pipeline.run(source, write_disposition="replace")

print(load_info)
