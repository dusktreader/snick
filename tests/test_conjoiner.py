from snick.conjoiner import Conjoiner
from snick.methods import dedent


def test_conjoiner_basic():
    conjoiner = Conjoiner()
    conjoiner.add("First line", "Second line")
    conjoiner.add(
        """
        Dedented third line
        Dedented fourth line
        """
    )
    conjoiner.add(
        "    Indented fifth line",
        "    Indented sixth line",
        should_dedent=False,
    )
    conjoiner.add(
        "Seventh line",
        "Eighth line",
        "Ninth line",
        blanks_between=2,
    )

    assert str(conjoiner) == dedent(
        """
        First line
        Second line
        Dedented third line
        Dedented fourth line
            Indented fifth line
            Indented sixth line
        Seventh line


        Eighth line


        Ninth line
        """
    )


def test_conjoiner_empty():
    conjoiner = Conjoiner()
    assert str(conjoiner) == ""


def test_conjoiner_single_part():
    conjoiner = Conjoiner()
    conjoiner.add("Single line")
    assert str(conjoiner) == "Single line"


def test_conjoiner_custom_join_str():
    conjoiner = Conjoiner(join_str=" | ")
    conjoiner.add("first", "second", "third")
    assert str(conjoiner) == "first | second | third"


def test_conjoiner_custom_blank():
    conjoiner = Conjoiner(blank="---")
    conjoiner.add("first", "second", blanks_between=2)
    assert str(conjoiner) == dedent(
        """
        first
        ---
        ---
        second
        """
    )


def test_conjoiner_no_dedent():
    conjoiner = Conjoiner()
    conjoiner.add("    indented", should_dedent=False)
    assert str(conjoiner) == "    indented"


def test_conjoiner_blanks_between_multiple_adds():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.add("second")
    assert str(conjoiner) == dedent(
        """
        first
        second
        """
    )


def test_conjoiner_blanks_between():
    conjoiner = Conjoiner()
    conjoiner.add("first", "second", "third", blanks_between=2)
    assert str(conjoiner) == dedent(
        """
        first


        second


        third
        """
    )


def test_conjoiner_mixed_dedent():
    conjoiner = Conjoiner()
    conjoiner.add("    dedented", should_dedent=True)
    conjoiner.add("    not dedented", should_dedent=False)
    assert str(conjoiner) == "dedented\n    not dedented"


def test_conjoiner_multiple_calls_with_blanks():
    conjoiner = Conjoiner()
    conjoiner.add("first", "second", blanks_between=1)
    conjoiner.add("third")
    assert str(conjoiner) == dedent(
        """
        first

        second
        third
        """
    )


def test_conjoiner_empty_string_part():
    conjoiner = Conjoiner()
    conjoiner.add("first", "", "third")
    assert str(conjoiner) == dedent(
        """
        first

        third
        """
    )


def test_conjoiner_multiline_dedent():
    conjoiner = Conjoiner()
    conjoiner.add(
        """
        line one
        line two
        """
    )
    assert str(conjoiner) == dedent(
        """
        line one
        line two
        """
    )


def test_conjoiner_extend():
    conjoiner = Conjoiner()
    conjoiner.extend(["First line", "Second line"])
    conjoiner.extend(
        [
            """
        Dedented third line
        Dedented fourth line
        """
        ]
    )
    conjoiner.extend(
        [
            "    Indented fifth line",
            "    Indented sixth line",
        ],
        should_dedent=False,
    )
    conjoiner.extend(
        [
            "Seventh line",
            "Eighth line",
            "Ninth line",
        ],
        blanks_between=2,
    )

    assert str(conjoiner) == dedent(
        """
        First line
        Second line
        Dedented third line
        Dedented fourth line
            Indented fifth line
            Indented sixth line
        Seventh line


        Eighth line


        Ninth line
        """
    )


def test_conjoiner_add_blank():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.add_blank()
    conjoiner.add("second")
    assert str(conjoiner) == dedent(
        """
        first

        second
        """
    )


def test_conjoiner_add_blanks():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.add_blanks(3)
    conjoiner.add("second")
    assert str(conjoiner) == dedent(
        """
        first



        second
        """
    )


def test_conjoiner_add_blanks_before():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.add("second", blanks_before=2)
    conjoiner.add("third")
    assert str(conjoiner) == dedent(
        """
        first


        second
        third
        """
    )


def test_conjoiner_add_blanks_after():
    conjoiner = Conjoiner()
    conjoiner.add("first", blanks_after=2)
    conjoiner.add("second")
    assert str(conjoiner) == dedent(
        """
        first


        second
        """
    )


def test_conjoiner_add_blanks_before_and_after():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.add("second", blanks_before=1, blanks_after=1)
    conjoiner.add("third")
    assert str(conjoiner) == dedent(
        """
        first

        second

        third
        """
    )


def test_conjoiner_extend_blanks_before_and_after():
    conjoiner = Conjoiner()
    conjoiner.add("first")
    conjoiner.extend(["second", "third"], blanks_before=1, blanks_after=1)
    conjoiner.add("fourth")
    assert str(conjoiner) == dedent(
        """
        first

        second
        third

        fourth
        """
    )
