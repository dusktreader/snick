"""
Example: pretty_format() and pretty_print()

Render nested Python data structures with clean indentation and trailing commas.

Run it: `uv run python examples/pretty.py`
"""

import snick

# Simple dict
ship = {"name": "Millennium Falcon", "captain": "Han Solo", "parsecs": 12}
print(snick.pretty_format(ship))
print()

# Nested structure
order = {
    "faction": "Rebel Alliance",
    "leaders": ["Mon Mothma", "Admiral Ackbar"],
    "fleet": {
        "fighters": "X-Wing",
        "capital_ship": "Home One",
        "operational": True,
    },
}
print(snick.pretty_format(order))
print()

# pretty_print writes directly to stdout
snick.pretty_print({"planet": "Tatooine", "suns": 2, "inhabitants": ["Jawas", "Tusken Raiders"]})
