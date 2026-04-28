"""
This example set demonstrates the use of the `conjoin()` function.
This function joins multiple strings with a configurable separator.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `conjoin()`.

    `conjoin()` joins positional string arguments with a newline by default,
    making it a convenient way to build multi-line output without packing
    strings into a list.
    """
    result = snick.conjoin(
        "Help me, Obi-Wan Kenobi.",
        "You're my only hope.",
        "-- Princess Leia",
    )
    print(result)


def demo_2__custom_separator():
    """
    This function demonstrates `conjoin()` with a custom `join_str`.

    Any string can be used as the separator, making `conjoin()` useful for
    building CSV rows, pipe-delimited output, or any other format.
    """
    result = snick.conjoin("Luke Skywalker", "Han Solo", "Leia Organa", join_str=" | ")
    print(result)


def demo_3__single_item():
    """
    This function demonstrates `conjoin()` with a single argument.

    When only one string is provided there is nothing to join, so the string
    is returned as-is.
    """
    result = snick.conjoin("These are not the droids you are looking for.")
    print(result)
