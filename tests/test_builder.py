from snick.builder import Builder
from snick.methods import dedent


def test_builder_basic():
    builder = Builder()
    builder.add("First line", "Second line")
    builder.add(
        """
        Dedented third line
        Dedented fourth line
        """
    )
    builder.add(
        "    Indented fifth line",
        "    Indented sixth line",
        should_dedent=False,
    )
    builder.add(
        "Seventh line",
        "Eighth line",
        "Ninth line",
        blanks_between=2,
    )

    assert str(builder) == dedent(
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


def test_builder_empty():
    builder = Builder()
    assert str(builder) == ""


def test_builder_single_part():
    builder = Builder()
    builder.add("Single line")
    assert str(builder) == "Single line"


def test_builder_custom_join_str():
    builder = Builder(join_str=" | ")
    builder.add("first", "second", "third")
    assert str(builder) == "first | second | third"


def test_builder_custom_blank():
    builder = Builder(blank="---")
    builder.add("first", "second", blanks_between=2)
    assert str(builder) == dedent(
        """
        first
        ---
        ---
        second
        """
    )


def test_builder_no_dedent():
    builder = Builder()
    builder.add("    indented", should_dedent=False)
    assert str(builder) == "    indented"


def test_builder_blanks_between_multiple_adds():
    builder = Builder()
    builder.add("first")
    builder.add("second")
    assert str(builder) == dedent(
        """
        first
        second
        """
    )


def test_builder_blanks_between():
    builder = Builder()
    builder.add("first", "second", "third", blanks_between=2)
    assert str(builder) == dedent(
        """
        first


        second


        third
        """
    )


def test_builder_mixed_dedent():
    builder = Builder()
    builder.add("    dedented", should_dedent=True)
    builder.add("    not dedented", should_dedent=False)
    assert str(builder) == "dedented\n    not dedented"


def test_builder_multiple_calls_with_blanks():
    builder = Builder()
    builder.add("first", "second", blanks_between=1)
    builder.add("third")
    assert str(builder) == dedent(
        """
        first

        second
        third
        """
    )


def test_builder_empty_string_part():
    builder = Builder()
    builder.add("first", "", "third")
    assert str(builder) == dedent(
        """
        first

        third
        """
    )


def test_builder_multiline_dedent():
    builder = Builder()
    builder.add(
        """
        line one
        line two
        """
    )
    assert str(builder) == dedent(
        """
        line one
        line two
        """
    )


def test_builder_extend():
    builder = Builder()
    builder.extend(["First line", "Second line"])
    builder.extend([
        """
        Dedented third line
        Dedented fourth line
        """
    ])
    builder.extend(
        [
            "    Indented fifth line",
            "    Indented sixth line",
        ],
        should_dedent=False,
    )
    builder.extend(
        [
            "Seventh line",
            "Eighth line",
            "Ninth line",
        ],
        blanks_between=2,
    )

    assert str(builder) == dedent(
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


def test_builder_add_blank():
    builder = Builder()
    builder.add("first")
    builder.add_blank()
    builder.add("second")
    assert str(builder) == dedent(
        """
        first

        second
        """
    )


def test_builder_add_blanks():
    builder = Builder()
    builder.add("first")
    builder.add_blanks(3)
    builder.add("second")
    assert str(builder) == dedent(
        """
        first



        second
        """
    )


def test_builder_add_blanks_before():
    builder = Builder()
    builder.add("first")
    builder.add("second", blanks_before=2)
    builder.add("third")
    assert str(builder) == dedent(
        """
        first


        second
        third
        """
    )


def test_builder_add_blanks_after():
    builder = Builder()
    builder.add("first", blanks_after=2)
    builder.add("second")
    assert str(builder) == dedent(
        """
        first


        second
        """
    )


def test_builder_add_blanks_before_and_after():
    builder = Builder()
    builder.add("first")
    builder.add("second", blanks_before=1, blanks_after=1)
    builder.add("third")
    assert str(builder) == dedent(
        """
        first

        second

        third
        """
    )


def test_builder_extend_blanks_before_and_after():
    builder = Builder()
    builder.add("first")
    builder.extend(["second", "third"], blanks_before=1, blanks_after=1)
    builder.add("fourth")
    assert str(builder) == dedent(
        """
        first

        second
        third

        fourth
        """
    )
