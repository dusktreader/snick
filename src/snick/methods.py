import re
import sys
import textwrap
from typing import TextIO, Any, cast

import pprintpp  # pyright: ignore[reportMissingTypeStubs]


def indent(text: str, prefix: str = "    ", skip_first_line: bool = False, **kwargs: Any) -> str:
    """
    Wrap the `textwrap.indent()` method but include a default prefix.

    Args:
        prefix:          The preix to pass to `textwrap.indent()`. Defaults to 4 spaces
        skip_first_line: If `True`, the first line will not be indented. Defaults to `False`.
    """
    if skip_first_line:
        lines = text.split("\n")
        return "\n".join([lines[0], textwrap.indent("\n".join(lines[1:]), prefix, **kwargs)])
    return textwrap.indent(text, prefix, **kwargs)


def dedent(text: str, should_strip: bool = True) -> str:
    """
    Dedent a paragraph after removing leading and trailing whitespace.

    Args:
        text:         The text to dedent
        should_strip: Strip leading whitespace. Useful if you you like the first line of triple-quoted text
                      to start on the next line after the triple-quote. Defaults to ``True``
    """
    dedented = textwrap.dedent(text)
    return dedented.strip() if should_strip else dedented


def conjoin(*items: str, join_str: str = "\n") -> str:
    """
    Join strings supplied as args.

    Thinly wraps `str.join()` without having to pack strings in an iterable and with a default joining string.

    Args:
        items:    Positional arguments for strings that should be joined
        join_str: The string used to join the strings. Defaults to newline character.
    """
    return join_str.join(items)


def dedent_all(*texts: str, should_strip: bool = True, join_str: str = "\n") -> str:
    """
    Dedent each blob supplied as an argument and then joins them.

    Args:
        texts:        Positional text arguments to dedent and then join.
        should_strip: Passed along to each call to `dedent()`
        join_str:     Passed along to the call to `conjoin()`
    """
    return conjoin(*(dedent(t, should_strip=should_strip) for t in texts), join_str=join_str)


def unwrap(text: str, should_strip: bool = True) -> str:
    """
    Convert a paragraph of (possibly) indented, wrapped text and unwrap it into a single line.

    Args:
        text:         The text to unwrap
        should_strip: If set to `True`, strip leading whitespace. Passed on to `dedent()`.
    """
    return " ".join(dedent(text, should_strip=should_strip).split("\n"))


def strip_whitespace(text: str) -> str:
    """
    Remove all whitespace from a string.
    """
    return re.sub(r"\s+", "", text)


def indent_wrap(text: str, **kwargs: Any) -> str:
    """
    Wrap a long string using textwrap args and indent all the lines using the same indent as the first line.
    """
    match = re.match(r"(\s+).*", text)
    if match:
        kwargs["subsequent_indent"] = match.group(1)
    return textwrap.fill(text, **kwargs)


def pretty_print(data: dict[Any, Any], *args: Any, stream: TextIO = sys.stdout, **kwargs: Any):
    """
    Print to a stream (stdout by default) a data item using the pretty_format method.

    Args:
        data:   The data to pretty print.
        args:   Positional arguments to pass to `pretty_format()`
        stream: The stream to print to. Defaults to `sys.stdout`.
        kwargs: Keyword arguments to pass to `pretty_format()`
    """
    print(pretty_format(data, *args, **kwargs), file=stream)


def pretty_format(data: dict[Any, Any], *args: Any, indent: int = 2, width: int = 1, **kwargs: Any) -> str:
    """
    Pretty-format a python data structure using `pprintpp.pformat()`.

    Args:
        data:   The data to pretty print.
        args:   Positional arguments to pass to `pprintpp.pformat()`
        indent: The `indent` value to pass along to `pprintpp.pformat()`. Defaults to 2.
        width:  The `width` value to pass along to `pprintpp.pformat()`. Defaults to 1.
        kwargs: Keyword arguments to pass to `pprintpp.pformant()`
    """
    return cast(str, pprintpp.pformat(data, *args, indent=indent, width=width, **kwargs))  # pyright: ignore[reportUnknownMemberType]


def enboxify(text: str, boxchar: str = "*", hspace: int = 1, vspace: int = 0, should_strip: bool = True) -> str:
    """
    Draw a box around a block of text.

    Args:
        text:         The text to enboxify
        boxchar:      The text to use for drawing the box
        hspace:       Horizontal padding around text and box
        vspace:       Vertical padding around text and box
        should_strip: Strip leading whitespace. Passed on to `dedent()`
    """
    if len(boxchar) > 1:
        raise Exception("boxchar must be a single character")
    if hspace < 0:
        raise Exception("hspace must be 0 or greater")
    if vspace < 0:
        raise Exception("vspace must be 0 or greater")
    text = dedent(text, should_strip=should_strip)
    lines = [""] * vspace + text.split("\n") + [""] * vspace
    box_width = max([len(ln) for ln in lines]) + 2 + hspace * 2
    newlines = [boxchar * box_width]
    for line in lines:
        newlines += [
            "{bc}{bs}{line}{spacer}{bs}{bc}".format(
                bc=boxchar,
                line=line,
                spacer=" " * (box_width - len(line) - 2 - hspace * 2),
                bs=" " * hspace,
            )
        ]
    newlines += [boxchar * box_width]
    return "\n".join(newlines)
