"""
This example set demonstrates the use of the `Conjoiner` class.
`Conjoiner` accumulates string parts and joins them on demand.
"""

from snick import Conjoiner


def demo_1__simple():
    """
    This function demonstrates the basic use of `Conjoiner`.

    `Conjoiner` lets you build up a multi-line string incrementally by
    calling `add()`.  Calling `str()` on the instance returns all parts
    joined with the configured `join_str` (newline by default).
    """
    c = Conjoiner()
    c.add("Episode IV: A New Hope")
    c.add("Episode V: The Empire Strikes Back")
    c.add("Episode VI: Return of the Jedi")
    print(str(c))


def demo_2__iadd_operator():
    """
    This function demonstrates the `+=` operator on `Conjoiner`.

    The `+=` operator is a shorthand for `add()` with a single part.  It
    dedents the string automatically, just like `add()`.
    """
    c = Conjoiner()
    c += "Use the Force, Luke."
    c += "I am your father."
    c += "Do or do not. There is no try."
    print(str(c))


def demo_3__blanks():
    """
    This function demonstrates blank-line insertion with `Conjoiner`.

    `add()` accepts `blanks_before`, `blanks_after`, and
    `blanks_between` keyword arguments to insert blank lines around and
    between the parts being added.
    """
    c = Conjoiner()
    c.add("Rebel Alliance")
    c.add("Luke Skywalker", "Han Solo", "Leia Organa", blanks_before=1, blanks_between=1)
    c.add("May the Force be with them.", blanks_before=1)
    print(str(c))


def demo_4__dedent():
    """
    This function demonstrates automatic dedenting in `Conjoiner`.

    By default, `add()` dedents each part.  This means you can use
    triple-quoted strings with natural source indentation and the output
    will be clean.  Pass `should_dedent=False` to skip this behaviour.
    """
    c = Conjoiner()
    c.add(
        """
        A long time ago in a galaxy far,
        far away...
        """
    )
    c.add("    STAR WARS", should_dedent=False)
    print(str(c))


def demo_5__custom_join_str():
    """
    This function demonstrates `Conjoiner` with a custom `join_str`.

    The `join_str` controls what is inserted between every part.  Using a
    separator other than newline makes `Conjoiner` useful for building
    non-line-oriented strings too.
    """
    c = Conjoiner(join_str=" -> ")
    c.add("Tatooine", "Alderaan", "Death Star", "Yavin 4")
    print(str(c))


def demo_6__extend():
    """
    This function demonstrates the `extend()` method on `Conjoiner`.

    `extend()` is a convenience wrapper around `add()` that accepts an
    iterable of strings instead of variadic positional arguments.
    """
    c = Conjoiner()
    members = ["Obi-Wan Kenobi", "Yoda", "Mace Windu"]
    c.extend(members)
    print(str(c))
