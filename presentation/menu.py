from collections import OrderedDict

from business_logic import add_entry_command, list_entries_commands, quit_command
from persistence import EntryDatabase

from presentation import Option, get_new_entry_data

entry_database = EntryDatabase()

options = OrderedDict(
    {
        "A": Option("View All Entries", list_entries_commands.ListEntriesCommand()),
        "B": Option(
            "Add Entry",
            add_entry_command.AddEntryCommand(),
            prep_call=get_new_entry_data,
            success_message="Entry added successfully.",
        ),
        "C": Option("Quit", quit_command.QuitCommand()),
    }
)
