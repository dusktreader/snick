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
        """
    expected_dedented_text = "\n".join(
        [
            "",
            "this is indented text",
            "it looks nice.",
            "I would like to remove",
            "leading space",
            "when I print it out",
            "",
        ]
    )
    assert snick.dedent(indented_text, should_strip=False) == expected_dedented_text


def test_indent():
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
