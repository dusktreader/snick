"""
This example set demonstrates the use of the `enboxify()` function.
This function draws an ASCII box around a block of text.
"""

import snick


def demo_1__simple():
    """
    This function demonstrates the basic use of `enboxify()`.

    `enboxify()` surrounds a block of text with a border made from a single
    repeated character.  It also dedents the input, so triple-quoted strings
    work naturally.
    """
    result = snick.enboxify(
        """
        May the Force be with you.
        """
    )
    print(result)


def demo_2__custom_boxchar():
    """
    This function demonstrates `enboxify()` with a custom `boxchar`.

    Any single character can be used to draw the border, making it easy to
    produce different visual styles.
    """
    result = snick.enboxify("Do. Or do not. There is no try.", boxchar="#")
    print(result)


def demo_3__padding():
    """
    This function demonstrates `enboxify()` with extra `hspace` and
    `vspace` padding.

    Horizontal padding adds spaces between the text and the side borders.
    Vertical padding inserts blank lines between the text and the top/bottom
    borders.
    """
    result = snick.enboxify(
        "I am one with the Force. The Force is with me.",
        hspace=3,
        vspace=1,
    )
    print(result)


def demo_4__multiline():
    """
    This function demonstrates `enboxify()` with a multi-line block.

    The box is sized to fit the widest line, and all other lines are padded
    to match.
    """
    result = snick.enboxify(
        """
        Rebel Alliance Fleet
        Commander: Admiral Ackbar
        Status: It's a trap!
        """
    )
    print(result)
