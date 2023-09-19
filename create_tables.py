from settings import db_contector, db_execute_query


def create_contracts_db(conector: db_contector):
    query = """
    CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    signature_data TIMESTAMP,
    status TEXT DEFAULT 'DRAFT',
    project_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """
    db_execute_query(conector, query)


def create_projects_db(conector: db_contector):
    query = """
    CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """
    db_execute_query(conector, query)


create_projects_db(db_contector)
create_contracts_db(db_contector)
db_contector.close()
