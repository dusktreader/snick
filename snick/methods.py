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


def dedent(text):
    """
    Dedents a paragraph after removing leading and trailing whitespace
    """
    return textwrap.dedent(text).strip()


def unwrap(text):
    """
    Converts a paragraph of (possibly) indented, wrapped text and unwraps it
    into a single line
    """
    return " ".join(dedent(text).split("\n"))


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


def enboxify(text, boxchar="*", hspace=1, vspace=0):
    """
    Draws a box around a block of text
    """
    if len(boxchar) > 1:
        raise Exception("boxchar must be a single character")
    if hspace < 0:
        raise Exception("hspace must be 0 or greater")
    if vspace < 0:
        raise Exception("vspace must be 0 or greater")
    text = dedent(text)
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
