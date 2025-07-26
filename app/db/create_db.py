from app.db.datasource_id import DatasourceID
from app.db.postgres import PostgresDatabase


def data_source(key):
    if key is DatasourceID.POSTGRES:
        return PostgresDatabase()
    else:
        return None


database = data_source(DatasourceID.POSTGRES)
