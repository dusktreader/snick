import re
import sys
import textwrap

import pprintpp


def indent(text, prefix="    ", **kwargs):
    """
    Simple wrapper for the textwrap.indent() method but includes a
    default prefix
    """
    return textwrap.indent(text, prefix=prefix, **kwargs)


def dedent(text, should_strip=True):
    """
    Dedents a paragraph after removing leading and trailing whitespace

    :param text:         The text to dedent
    :param should_strip: Strip leading whitespace. Useful if you you like the first line of triple-quoted text
                         to start on the next line after the triple-quote. Defaults to ``True``
    """
    dedented = textwrap.dedent(text)
    return (dedented.strip() if should_strip else dedented)


def unwrap(text, should_strip=True):
    """
    Converts a paragraph of (possibly) indented, wrapped text and unwraps it
    into a single line

    :param text:         The text to unwrap
    :param should_strip: Strip leading whitespace. Passed on to ``dedent()``
    """
    return " ".join(dedent(text, should_strip=should_strip).split("\n"))


def strip_whitespace(text):
    """
    Removes all whitespace from a string
    """
    return re.sub(r"\s+", "", text)


def indent_wrap(text, **kwargs):
    """
    Wraps a long string using textwrap args and indents all the lines using
    the same indent as the first line
    """
    match = re.match(r"(\s+).*", text)
    if match:
        kwargs["subsequent_indent"] = match.group(1)
    return textwrap.fill(text, **kwargs)


def pretty_print(data, *args, stream=sys.stdout, **kwargs):
    """
    Prints to a stream (stdout by default) a data item using the
    pretty_format method
    """
    print(pretty_format(data, *args, **kwargs), file=stream)


def pretty_format(data, *args, indent=2, **kwargs):
    """
    Pretty-formats a python data structure
    """
    kwargs["width"] = 1
    return pprintpp.pformat(data, indent=indent, **kwargs)


def enboxify(text, boxchar="*", hspace=1, vspace=0, should_strip=True):
    """
    Draws a box around a block of text

    :param text:         The text to enboxify
    :param boxchar:      The text to use for drawing the box
    :param hspace:       Horizontal padding around text and box
    :param vspace:       Vertical padding around text and box
    :param should_strip: Strip leading whitespace. Passed on to ``dedent()``
    """
    if len(boxchar) > 1:
        raise Exception("boxchar must be a single character")
    if hspace < 0:
        raise Exception("hspace must be 0 or greater")
    if vspace < 0:
        raise Exception("vspace must be 0 or greater")
    text = dedent(text, should_strip=should_strip)
    lines = [""] * vspace + text.split("\n") + [""] * vspace
    box_width = max([len(l) for l in lines]) + 2 + hspace * 2
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
