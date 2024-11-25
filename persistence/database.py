import sqlite3
from sqlite3 import Cursor


class DatabaseManager:
    def __init__(self, database_file: str):
        self.connection = sqlite3.connect(database_file)

    def __del__(self):
        self.connection.close()

    def _execute(self, statement, values=None) -> Cursor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name: str, columns: dict) -> None:
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()
        ]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )

    def add(self, table_name: str, data: dict) -> None:
        placeholders = ", ".join("?" * len(data))
        column_names = ", ".join(data.keys())
        column_values = tuple(data.values())

        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            """,
            column_values,
        )

    def select(
        self, table_name: str, criteria: str = None, order_by: str = None
    ) -> Cursor:
        criteria = criteria or {}
        query = f"SELECT * FROM {table_name}"

        if criteria:
            placeholders = [f"{column} = ?" for column in criteria.keys()]
            select_criteria = " AND ".join(placeholders)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"

        return self._execute(query, tuple(criteria.values()))
