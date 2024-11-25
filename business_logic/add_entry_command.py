from business_logic import Command
from persistence import DatabaseManager
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class AddEntryCommand(Command):
    def execute(self, data=None) -> tuple[bool, None]:
        db.add("entries", data)
        return True, None
