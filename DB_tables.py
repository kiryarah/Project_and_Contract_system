from settings import db_contector, db_execute_query


class BaseDBTable:

    db_name: str

    def __init__(self) -> None:
        self.conn = db_contector

    def __del__(self) -> None:
        self.conn.close()

    def view(self) -> list[tuple]:
        query = f"SELECT * FROM {self.db_name}"
        cursor = db_execute_query(self.conn, query)
        rows = cursor.fetchall()
        return rows

    def get(self, table_id: int) -> tuple:
        query = f"SELECT * FROM {self.db_name} WHERE id={table_id}"
        cursor = db_execute_query(self.conn, query)
        row = cursor.fetchone()
        return row if row else f'Записи с {table_id} нет!'

    def get_id_by_name(self, name: str) -> int:
        return self.search_by_name(name)[0]

    def delete(self, table_id):
        query = f"DELETE FROM {self.db_name} WHERE id={table_id}"
        db_execute_query(self.conn, query)

    def search_by_name(self, name: str) -> tuple:
        query = f"SELECT * FROM {self.db_name} WHERE name='{name}'"
        cursor = db_execute_query(self.conn, query)
        return cursor.fetchone()


class ContractDBTable(BaseDBTable):
    db_name = 'contracts'
    COLUMNS = ('signature_data', 'status', 'project_id')

    def insert(self, name: str) -> None:
        query = f"INSERT INTO {self.db_name} (name, signature_data, project_id) VALUES ('{name}', NULL, NULL);"
        db_execute_query(self.conn, query)

    def update_by_id(self, table_id: int, date=None, status=None, project_id=None) -> None:
        set_columns = [
            f"{key}='{value}'"
            for key, value in zip(self.COLUMNS, (date, status, project_id))
            if value
        ]
        set_columns = ', '.join(set_columns)

        query = f"UPDATE {self.db_name} SET {set_columns} WHERE id={table_id}"
        db_execute_query(self.conn, query)

    def filter_by_project_id(self, project_id: int) -> list[tuple]:
        query = f"SELECT * FROM {self.db_name} WHERE project_id={project_id}"
        cursor = db_execute_query(self.conn, query)
        rows = cursor.fetchall()
        return rows

    # def update_status(self, table_id: int, status: str) -> None:
    #     query = f"UPDATE {self.db_name} SET status={status} WHERE id={table_id}"
    #     db_execute_query(self.conn, query)

    # def update_signature_date(self, table_id: int, date: str) -> None:
    #     query = f"UPDATE {self.db_name} SET signature_data={date} WHERE id={table_id}"
    #     db_execute_query(self.conn, query)

    # def update_project_id(self, project_id: int, table_id: int) -> None:
    #     query = f"UPDATE {self.db_name} SET project_id={project_id} WHERE id={table_id}"
    #     db_execute_query(self.conn, query)


class ProjectDBTable(BaseDBTable):
    db_name = 'projects'

    def insert(self, name) -> None:
        query = f"INSERT INTO {self.db_name} (name) VALUES ('{name}');"
        db_execute_query(self.conn, query)

    def update_has_active(self, table_id: int, has_active: bool):
        query = f"UPDATE {self.db_name} SET has_active={has_active} WHERE id={table_id}"
        db_execute_query(self.conn, query)
