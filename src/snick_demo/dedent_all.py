"""
This example set demonstrates the use of the `dedent_all()` function.
This function dedents each supplied string blob and then joins them.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `dedent_all()`.

    `dedent_all()` is handy when you want to compose a final string from
    several separately-indented triple-quoted blocks.  Each block is dedented
    independently before being joined.
    """
    result = snick.dedent_all(
        """
        In my experience, there is no such thing as luck.
        """,
        """
        Your eyes can deceive you.
        Don't trust them.
        """,
    )
    print(result)


def demo_2__custom_join_str():
    """
    This function demonstrates `dedent_all()` with a custom `join_str`.

    The `join_str` is passed through to `conjoin()`, so you can use any
    separator between the dedented blocks.
    """
    result = snick.dedent_all(
        """
        The dark side of the Force is a pathway
        to many abilities some consider to be unnatural.
        """,
        """
        It's not a story the Jedi would tell you.
        """,
        join_str="\n\n---\n\n",
    )
    print(result)
