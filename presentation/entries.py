from datetime import date

from typing_extensions import Any

from business_logic import JournalEntry
from presentation.user_input import get_user_input
from presentation.utils import format_date


def get_new_entry_data() -> dict[str, Any]:
    try:
        year, month, day = format_date(get_user_input("Enter Date (mm/dd/yyyy)"))
        journal = JournalEntry(
            content=get_user_input("What have you learn today?"),
            entry_date=date(year, month, day),
        )
        return journal.__dict__
    except ValueError:
        print("Please enter a entry or valid date.")
