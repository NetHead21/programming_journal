from datetime import date
from pydantic import BaseModel


class JournalEntry(BaseModel):
    content: str
    entry_date: date


if __name__ == "__main__":
    journal = JournalEntry(
        content="Today I learn how to program", entry_date=date(2024, 11, 23)
    )

    print(journal)
