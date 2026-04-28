"""
This example set demonstrates the use of the `dedent()` function.
This function strips indentation from multi-line strings.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `dedent()`.

    When writing multi-line strings in indented code, the indentation is
    embedded in the string. `dedent()` removes that common leading whitespace
    and strips surrounding blank lines.
    """
    result = snick.dedent(
        """
        The Force will be with you.
        Always.
        """
    )
    print(result)


def demo_2__no_strip():
    """
    This function demonstrates `dedent()` with `should_strip=False`.

    By default, `dedent()` strips leading and trailing whitespace from the
    result. Passing `should_strip=False` preserves the surrounding blank
    lines that come from the triple-quoted string.
    """
    result = snick.dedent(
        """
        I find your lack of faith disturbing.
        """,
        should_strip=False,
    )
    print(repr(result))


def demo_3__already_flush():
    """
    This function demonstrates `dedent()` on text that is already flush with
    the left margin.

    When no common leading whitespace exists, the string is returned unchanged
    (aside from stripping surrounding blank lines).
    """
    result = snick.dedent("Never tell me the odds.\nI know.")
    print(result)
