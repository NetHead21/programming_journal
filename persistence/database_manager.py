from persistence import DatabaseManager

database_file = "entries.db"


def database_manager() -> DatabaseManager:
    return DatabaseManager(database_file)
