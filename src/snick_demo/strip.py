"""
This example set demonstrates the strip utility functions in snick.
These functions remove various kinds of unwanted whitespace or escape codes.
"""

import snick


def demo_1__strip_whitespace():
    """
    This function demonstrates `strip_whitespace()`.

    `strip_whitespace()` removes **all** whitespace characters from a string,
    including spaces, tabs, and newlines.  It is useful for normalising strings
    before comparison or storage.
    """
    result = snick.strip_whitespace("  R2  -  D2  \n\t!")
    print(repr(result))


def demo_2__strip_trailing_whitespace():
    """
    This function demonstrates `strip_trailing_whitespace()`.

    `strip_trailing_whitespace()` trims trailing spaces and tabs from every
    line in a multi-line string without affecting leading whitespace or the
    overall structure of the text.
    """
    lines = "  Luke Skywalker   \n  Han Solo\t\n  Leia Organa  "
    result = snick.strip_trailing_whitespace(lines)
    for line in result.split("\n"):
        print(repr(line))


def demo_3__strip_ansi_escape_sequences():
    """
    This function demonstrates `strip_ansi_escape_sequences()`.

    Terminal output often includes ANSI escape codes for colours and styles.
    `strip_ansi_escape_sequences()` removes those codes so the plain text
    content can be used in contexts that don't support terminal formatting.
    """
    coloured = "\x1b[34mBlue Squadron\x1b[0m and \x1b[31mRed Squadron\x1b[0m"
    print("Raw string  :", repr(coloured))
    result = snick.strip_ansi_escape_sequences(coloured)
    print("After strip :", repr(result))
