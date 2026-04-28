"""
This example set demonstrates the use of the `unwrap()` function.
This function collapses an indented, wrapped paragraph into a single line.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `unwrap()`.

    Long strings written across multiple indented lines in source code carry
    embedded newlines and indentation.  `unwrap()` removes all of that and
    returns a single flat string — useful for building log messages or error
    strings without sacrificing readability in source.
    """
    result = snick.unwrap(
        """
        It is a period of civil war. Rebel spaceships,
        striking from a hidden base, have won their first
        victory against the evil Galactic Empire.
        """
    )
    print(result)


def demo_2__custom_separator():
    """
    This function demonstrates `unwrap()` with a custom `separator`.

    By default lines are joined with a single space.  Passing a different
    `separator` lets you control exactly what is inserted between the
    original lines.
    """
    result = snick.unwrap(
        """
        Tatooine
        Hoth
        Dagobah
        """,
        separator=" / ",
    )
    print(result)
