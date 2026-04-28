"""
This example set demonstrates the `pretty_format()` and `pretty_print()`
functions.  These functions render nested Python data structures with clean
indentation and trailing commas.
"""

import snick


def demo_1__simple_dict():
    """
    This function demonstrates `pretty_format()` with a simple dictionary.

    `pretty_format()` renders a Python dict with each key–value pair on its
    own line, indented and followed by a trailing comma.
    """
    data = {"name": "Millennium Falcon", "captain": "Han Solo", "parsecs": 12}
    result = snick.pretty_format(data)
    print(result)


def demo_2__nested():
    """
    This function demonstrates `pretty_format()` with a nested structure.

    The formatter recurses into nested dicts and lists, indenting each level
    consistently.
    """
    data = {
        "faction": "Rebel Alliance",
        "leaders": ["Mon Mothma", "Admiral Ackbar"],
        "fleet": {
            "fighters": "X-Wing",
            "capital_ship": "Home One",
            "operational": True,
        },
    }
    result = snick.pretty_format(data)
    print(result)


def demo_3__pretty_print():
    """
    This function demonstrates `pretty_print()`.

    `pretty_print()` is a thin wrapper that calls `pretty_format()` and
    prints the result directly to stdout (or any supplied stream).
    """
    import sys

    data = {"planet": "Tatooine", "suns": 2, "inhabitants": ["Jawas", "Tusken Raiders"]}
    snick.pretty_print(data, stream=sys.stdout)
