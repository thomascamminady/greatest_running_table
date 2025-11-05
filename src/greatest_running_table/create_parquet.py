import duckdb


def create_parquet(
    source: str = "~/Data/Runalyze/2025-10-30-30378-gdpr-backup/activities/*json",
    destination: str = "../data/activities.parquet",
    sample_size: int = 10000,
    union_by_name: bool = True,
):
    duckdb.read_json(
        source,
        sample_size=sample_size,
        union_by_name=union_by_name,
    ).pl().write_parquet(destination)
