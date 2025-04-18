import snick


def test_dedent__default():
    indented_text = """
            this is indented text
            it looks nice.
            I would like to remove
            leading space
            when I print it out
        """
    expected_dedented_text = "\n".join(
        [
            "this is indented text",
            "it looks nice.",
            "I would like to remove",
            "leading space",
            "when I print it out",
        ]
    )
    assert snick.dedent(indented_text) == expected_dedented_text


def test_dedent__should_not_strip():
    indented_text = """
            this is indented text
            it looks nice.
            I would like to remove
            leading space
            when I print it out
            but not the leading and trailing newline.
        """
    expected_dedented_text = "\n".join(
        [
            "\nthis is indented text",
            "it looks nice.",
            "I would like to remove",
            "leading space",
            "when I print it out",
            "but not the leading and trailing newline.\n",
        ]
    )
    assert snick.dedent(indented_text, should_strip=False) == expected_dedented_text


def test_conjoin__default():
    joined_text = snick.conjoin(
        "Here are some lines",
        "that should be joined",
        "into a single multi-line string",
    )
    assert joined_text == snick.dedent(
        """
        Here are some lines
        that should be joined
        into a single multi-line string
        """
    )


def test_conjoin__with_join_str_param():
    joined_text = snick.conjoin(
        "Here are some lines",
        "that should be joined",
        "with a separator",
        join_str=" -- ",
    )
    assert joined_text == "Here are some lines -- that should be joined -- with a separator"


def test_dedent_all__default():
    dedented_joined_text = snick.dedent_all(
        """
        Here is the first blob
        with 8 spaces of indentation
        that should be dedented first.
        """,
        "  Here is another single line with 2 spaces of indent.",
        "This line has no indentation.",
    )
    assert dedented_joined_text == snick.dedent(
        """
        Here is the first blob
        with 8 spaces of indentation
        that should be dedented first.
        Here is another single line with 2 spaces of indent.
        This line has no indentation.
        """
    )


def test_dedent_all__with_params():
    dedented_joined_text = snick.dedent_all(
        """
        Here is the first blob
        with 8 spaces of indentation
        that should be dedented first.
        """,
        "  Here is another single line with 2 spaces of indent.",
        "This line has no indentation.\n",
        should_strip=False,
        join_str="\n\n",
    )
    assert dedented_joined_text == snick.dedent(
        """
        Here is the first blob
        with 8 spaces of indentation
        that should be dedented first.


        Here is another single line with 2 spaces of indent.

        This line has no indentation.
        """,
        should_strip=False,
    )


def test_indent__basic():
    dedented_text = "\n".join(
        [
            "this is non-indented text",
            "it looks nice.",
            "",
            "but it has blank lines",
            "",
            "those should not be indented",
        ]
    )
    expected_indented_text = "\n".join(
        [
            "    this is non-indented text",
            "    it looks nice.",
            "",
            "    but it has blank lines",
            "",
            "    those should not be indented",
        ]
    )
    assert snick.indent(dedented_text) == expected_indented_text


def test_indent__skip_first_line():
    dedented_text = "\n".join(
        [
            "    this is partially-indented text.",
            "the first line is already indented.",
            "it should not be indented.",
            "only the remaining lines.",
        ]
    )
    expected_indented_text = "\n".join(
        [
            "    this is partially-indented text.",
            "    the first line is already indented.",
            "    it should not be indented.",
            "    only the remaining lines.",
        ]
    )
    assert snick.indent(dedented_text, skip_first_line=True) == expected_indented_text


def test_unwrap():
    indented_text = """
        this is indented text
        it looks nice.
        I would like to remove
        leading space
        when I print it out
    """
    expected_unwrapped_text = (
        "this is indented text it looks nice. I would like to remove leading space when I print it out"
    )
    assert snick.unwrap(indented_text) == expected_unwrapped_text


def test_strip_whitespace():
    whitespace_city = """
        here is a string with a bundle of
        different \t kinds of whitespace.
        we want it all gone.
    """
    expected_stripped_text = "hereisastringwithabundleofdifferentkindsofwhitespace.wewantitallgone."
    assert snick.strip_whitespace(whitespace_city) == expected_stripped_text


def test_indent_wrap():
    unindented_text = "   All wrapped lines should be started with 4 spaces"
    expected_wrapped_text = "\n".join(
        [
            "   All wrapped lines",
            "   should be started",
            "   with 4 spaces",
        ]
    )
    assert snick.indent_wrap(unindented_text, width=20) == expected_wrapped_text


def test_pretty_format():
    assert snick.pretty_format({"a": {"b": 1, "c": {"d": 2}, "e": 3}, "f": 4}) == snick.dedent(
        """
          {
            'a': {
              'b': 1,
              'c': {
                'd': 2,
              },
              'e': 3,
            },
            'f': 4,
          }
        """
    )


def test_enboxify():
    indented_unboxed_text = """
        here's some text that we
        want to put into a box.
        That will make it look
        so very nice
    """
    expected_boxed_text = snick.dedent(
        """
        ****************************
        * here's some text that we *
        * want to put into a box.  *
        * That will make it look   *
        * so very nice             *
        ****************************
        """
    )
    assert snick.enboxify(indented_unboxed_text) == expected_boxed_text
