from persistence import DatabaseManager
from .persistence import PersistenceLayer


class EntryDatabase(PersistenceLayer):
    def __init__(self):
        self.table_name = "entries"
        self.db = DatabaseManager("entries.db")

        self.db.create_table(
            self.table_name,
            {
                "id": "integer primary key autoincrement",
                "content": "text not null",
                "entry_date": "DATE",
            },
        )

    def create(self, entry_data: dict) -> None:
        self.db.add(self.table_name, entry_data)

    def list(self, order_by: str = None):
        return self.db.select(self.table_name, order_by=order_by).fetchall()
