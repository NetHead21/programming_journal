from business_logic import Command
from persistence import DatabaseManager
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class ListEntriesCommand(Command):
    def __init__(self, order_by: str = "entry_date") -> None:
        self.order_by = order_by

    def execute(self, data=None) -> tuple[bool, any]:
        return True, db.select("entries", order_by=self.order_by).fetchall()
