"""
This example set demonstrates the use of the `indent()` function.
This function adds a prefix to every line of a string.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `indent()`.

    `indent()` wraps `textwrap.indent()` with a convenient default prefix of
    four spaces, so you can add a standard level of indentation without
    having to spell out the prefix each time.
    """
    result = snick.indent("Luke Skywalker\nHan Solo\nLeia Organa")
    print(result)


def demo_2__custom_prefix():
    """
    This function demonstrates `indent()` with a custom `prefix`.

    Any string can be used as the prefix — handy for producing quoted text,
    comment blocks, or other formatted output.
    """
    result = snick.indent("Luke Skywalker\nHan Solo\nLeia Organa", prefix="> ")
    print(result)


def demo_3__skip_first_line():
    """
    This function demonstrates `indent()` with `skip_first_line=True`.

    When the first line already has its own label or marker, you can skip
    indenting it while still indenting all subsequent lines.
    """
    result = snick.indent(
        "Jedi Order:\nObi-Wan Kenobi\nYoda\nMace Windu",
        skip_first_line=True,
    )
    print(result)
