# Features

snick provides a set of text manipulation functions and a `Conjoiner` class for building multi-line strings
incrementally. All functions accept additional keyword arguments to customize their behavior.


## Core functions

### `dedent()`

Unindents a block of text by aligning all lines with the leftmost non-whitespace character. Useful for
triple-quoted strings inside indented code.


#### Example

```python linenums="1" title="dedent() example"
import snick

class Whatever:
    @staticmethod
    def print_some_stuff():
        print(
            snick.dedent(
                """
                Here is some text
                    here is some other text
                    we don't want this indented
                    when it's printed
                      (to the console)
                """
            )
        )
```

```text title="output"
Here is some text
    here is some other text
    we don't want this indented
    when it's printed
      (to the console)
```


#### Parameters

##### `should_strip` (bool)

If `False`, `should_strip` preserves leading and trailing newlines. Default is `True`.

```python linenums="1" title="dedent() with should_strip=False"
dummy_text = """
    Here is some text
        here is some other text
"""
print(snick.dedent(dummy_text, should_strip=False))
```

```text title="output (with blank lines preserved)"

Here is some text
    here is some other text

```

----

### `indent()`

Indents a block of text. This is a thin wrapper around `textwrap.indent()` with sensible defaults.


#### Example

```python linenums="1" title="indent() example"
lines = [
    "would be so nice",
    "to indent these",
    "i guess",
]
print(snick.indent("\n".join(lines)))
```

```text title="output"
    would be so nice
    to indent these
    i guess
```


#### Parameters

##### `prefix` (str)

The string to prepend to each line. Default is `"    "` (4 spaces).

```python linenums="1" title="indent() with prefix"
lines = [
    "would be so nice",
    "to indent these",
    "i guess",
]
print(snick.indent("\n".join(lines), prefix=">> "))
```

```text title="output"
>> would be so nice
>> to indent these
>> i guess
```


##### `predicate` (callable)

A function that determines which lines to indent. Only lines for which it returns `True` are prefixed.

```python linenums="1" title="indent() with predicate"
lines = [
    "would be so nice",
    "to indent these",
    "i guess",
]
print(snick.indent("\n".join(lines), predicate=lambda line: "indent" in line))
```

```text title="output"
would be so nice
    to indent these
i guess
```


##### `skip_first_line` (bool)

If `True`, the first line is not indented. Default is `False`.

```python linenums="1" title="indent() with skip_first_line"
lines = [
    "do not indent me",
    "indent me, though",
    "and me",
]
print(snick.indent("\n".join(lines)), skip_first_line=True))
```

```text title="output"
do not indent me
    indent me, though
    and me
```


### `dedent_all()`

Applies `dedent()` to each argument separately and joins them together (using [`conjoin()`](#conjoin).


#### Example

```python linenums="1" title="dedent_all() example"
print(
    snick.dedent_all(
        """
        Here is a long bit of text
        as an introduction to the
        following dynamic items:
        --------------------------
        """,
        *(f"* Item #{i}" for i in range(1, 4)),
    )
)
```

```text title="output"
Here is a long bit of text
as an introduction to the
following dynamic items:
--------------------------
* Item #1
* Item #2
* Item #3
```


#### Parameters

##### `should_strip` (bool)

Passed through to each `dedent()` call. See [`dedent()`](#dedent).


##### `join_str` (str)

The string used to join the dedented parts. See [`conjoin()`](#conjoin).

----

### `unwrap()`

Joins all lines in a block of text into a single string. Useful for long strings in deeply indented code.


#### Example

```python linenums="1" title="unwrap() example"
if True:
    if True:
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            if True:
                                print(
                                    snick.unwrap(
                                        """
                                        I need to have a very long string here, but
                                        it would go way outside of the line length
                                        limit and cause me all sorts of grief with
                                        the style checker. So, unwrap can help me
                                        here
                                        """
                                    )
                                )
```

```text title="output"
I need to have a very long string here, but it would go way outside of the line length limit and cause me all sorts of grief with the style checker. So, unwrap can help me here
```


#### Parameters

##### `should_strip` (bool)

Passed through to the internal `dedent()` call. See [`dedent()`](#dedent).


##### `separator` (str)

The string used to join lines after dedenting. Default is `" "` (a single space).

```python linenums="1" title="unwrap() with separator"
print(
    snick.unwrap(
        """
        These lines
        need to be joined
        with a custom separator
        """,
        separator=" / ",
    )
)
```

```text title="output"
These lines / need to be joined / with a custom separator
```

----

### `conjoin()`

Like Python's built-in `join()`, but accepts items as arguments instead of requiring an iterable.


#### Example

```python linenums="1" title="conjoin() example"
print(
    snick.conjoin(
        "Here are some lines",
        "that I would like to join",
        "and it would be silly",
        "to have to wrap them in a",
        "list instead of just passing",
        "them as plain old arguments",
    )
)
```

```text title="output"
Here are some lines
that I would like to join
and it would be silly
to have to wrap them in a
list instead of just passing
them as plain old arguments
```


#### Parameters

##### `join_str` (str)

The string used to join the arguments. Default is `"\n"`.

```python linenums="1" title="conjoin() with join_str"
print(
    snick.conjoin(
        "These lines",
        "need to be joined",
        "with a custom separator",
        join_str=" / ",
    )
)
```

```text title="output"
These lines / need to be joined / with a custom separator
```

----

### `strip_whitespace()`

Removes all whitespace from a string, including newlines, tabs, and spaces. Handy for tests.


#### Example

```python linenums="1" title="strip_whitespace() example"
print(
    snick.strip_whitespace(
        """
        some text with    whitespace
        and whatnot
        """
    )
)
```

```text title="output"
sometextwithwhitespaceandwhatnot
```

----

### `strip_trailing_whitespace()`

Removes trailing whitespace from each line in a multi-line string.


#### Example

```python linenums="1" title="strip_trailing_whitespace() example"
print(snick.strip_trailing_whitespace(
    snick.conjoin(
        "  here is a string with a bundle of    ",
        "  trailing whitespace. ",
        "  we want it all gone.                    ",
    )
))
```

```text title="output"
  here is a string with a bundle of
  trailing whitespace.
  we want it all gone.
```

----

### `strip_ansi_escape_sequences()`

Removes ANSI escape sequences from text, such as those added by terminal applications for color and formatting.


#### Example

```python linenums="1" title="strip_ansi_escape_sequences() example"
print(
    snick.strip_ansi_escape_sequences(
        snick.dedent(
            """
            \033[31mhere's some text\033[0m with
            \033[32mansi control codes\033[0m added
            \033[33mincluding a few\033[0m
            \033[34mdifferent colors\033[0m
            \033[1mand bold text\033[0m.
            """
        )
    )
)
```

```text title="output"
here's some text with
ansi control codes added
including a few
different colors
and bold text.
```

----

### `indent_wrap()`

Wraps a long string and indents each wrapped line.


#### Example

```python linenums="1" title="indent_wrap() example"
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print("Here's some filler text:")
print(snick.indent_wrap(long_text, width=70, indent=4))
```

```text title="output"
Here's some filler text:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua.
```


#### Parameters

All keyword arguments are passed through to `textwrap.fill()`. The most commonly useful ones are:


##### `width` (int)

The maximum line width. Default is `80`.


##### `indent` (int)

Number of spaces to prefix each line with. Passed to `textwrap.fill()` as `initial_indent`. Default is `4`.


##### `subsequent_indent` (str)

The prefix applied to all lines after the first. `indent_wrap` sets this automatically to match any leading
whitespace on the input text, but you can override it explicitly.


##### `break_long_words` (bool)

If `True`, words longer than `width` are broken across lines. Default is `True`.


##### `break_on_hyphens` (bool)

If `True`, wrapping may occur on hyphens in compound words. Default is `True`.

----

### `pretty_format()`

Formats Python data structures (dict, list, tuple, or combinations) with consistent indentation and trailing
commas, similar to `json.dumps(indent=2)` but for arbitrary Python objects.


#### Example

```python linenums="1" title="pretty_format() example"
data = {
    "name": "example",
    "values": [1, 2, 3],
    "nested": {
        "key": "value"
    }
}
print(snick.pretty_format(data))
```

```text title="output"
{
  'name': 'example',
  'values': [
    1,
    2,
    3,
  ],
  'nested': {
    'key': 'value',
  },
}
```

It also works with types like `datetime`, `Decimal`, and custom classes:

```python linenums="1" title="pretty_format() with datetime and Decimal"
from datetime import datetime
from decimal import Decimal

data = {
    "timestamp": datetime(2026, 1, 22, 20, 15, 30),
    "amount": Decimal("123.45"),
    "active": True,
    "notes": None,
}
print(snick.pretty_format(data))
```

```text title="output"
{
  'timestamp': datetime.datetime(2026, 1, 22, 20, 15, 30),
  'amount': Decimal('123.45'),
  'active': True,
  'notes': None,
}
```

#### Parameters

##### `indent` (int)

Number of spaces per indentation level. Default is `2`.

----

### `pretty_print()`

Same as `pretty_format()` but prints to a stream instead of returning a string.


#### Example

```python linenums="1" title="pretty_print() example"
snick.pretty_print(data)  # prints to stdout
```

#### Parameters

##### `stream` (file-like)

The output stream to print to. Default is `sys.stdout`.

```python linenums="1" title="pretty_print() with stream"
import sys

data = {
    "name": "example",
    "values": [1, 2, 3],
}
snick.pretty_print(data, stream=sys.stderr)
```


##### `indent` (int)

Number of spaces per indentation level. Default is `2`.

```python linenums="1" title="pretty_print() with indent"
data = {
    "name": "example",
    "values": [1, 2, 3],
}
snick.pretty_print(data, indent=4)
```

```text title="output"
{
    'name': 'example',
    'values': [
        1,
        2,
        3,
    ],
}
```

----

### `enboxify()`

Draws a box around a block of text.


#### Example

```python linenums="1" title="enboxify() example"
print(
    snick.enboxify(
        """
        here's some text that we
        want to put into a box.
        That will make it look
        so very nice
        """
    )
)
```

```text title="output"
****************************
* here's some text that we *
* want to put into a box.  *
* That will make it look   *
* so very nice             *
****************************
```

#### Parameters

##### `boxchar` (str)

The single character used to draw the box. Default is `"*"`.

```python linenums="1" title="enboxify() with boxchar"
print(
    snick.enboxify(
        """
        here's some text that we
        want to put into a box.
        """,
        boxchar="#",
    )
)
```

```text title="output"
############################
# here's some text that we #
# want to put into a box.  #
############################
```


##### `hspace` (int)

Number of spaces between the text and the box on the left and right. Default is `1`.

```python linenums="1" title="enboxify() with hspace"
print(
    snick.enboxify(
        """
        here's some text that we
        want to put into a box.
        """,
        hspace=3,
    )
)
```

```text title="output"
********************************
*   here's some text that we   *
*   want to put into a box.    *
********************************
```


##### `vspace` (int)

Number of blank lines between the text and the box on the top and bottom. Default is `0`.

```python linenums="1" title="enboxify() with vspace"
print(
    snick.enboxify(
        """
        here's some text that we
        want to put into a box.
        """,
        vspace=1,
    )
)
```

```text title="output"
****************************
*                          *
* here's some text that we *
* want to put into a box.  *
*                          *
****************************
```


##### `should_strip` (bool)

Passed through to the internal `dedent()` call. See [`dedent()`](#dedent).

----

## Conjoiner class

`Conjoiner` builds multi-line strings incrementally. You add lines or blocks one at a time and convert to a
string at the end.


### Basic usage

```python linenums="1" title="Conjoiner basic usage"
from snick import Conjoiner

conjoiner = Conjoiner()
conjoiner.add("First line")
conjoiner.add("Second line")
print(conjoiner)
```

```text title="output"
First line
Second line
```


### Adding multiple parts

Pass multiple arguments to `add()` in a single call:

```python linenums="1" title="Conjoiner adding multiple parts"
conjoiner = Conjoiner()
conjoiner.add(
    "Line 1",
    "Line 2",
    "Line 3",
)
print(conjoiner)
```


### Automatic dedenting

By default, `Conjoiner` dedents each part:

```python linenums="1" title="Conjoiner with automatic dedenting"
conjoiner = Conjoiner()
conjoiner.add(
    """
    This text is indented in the code
    but will be dedented in the output
    """
)
conjoiner.add(
    """
    Same with this text
    it looks nice in the code
    """
)
print(conjoiner)
```

```text title="output"
This text is indented in the code
but will be dedented in the output
Same with this text
it looks nice in the code
```

To preserve indentation, pass `should_dedent=False`:

```python linenums="1" title="Conjoiner preserving indentation"
conjoiner = Conjoiner()
conjoiner.add("    Keep this indented", should_dedent=False)
```


### Adding blank lines

Insert blank lines between parts within a single `add()` call using `blanks_between`:

```python linenums="1" title="Conjoiner with blanks_between"
conjoiner = Conjoiner()
conjoiner.add(
    "Section 1",
    "Section 2",
    "Section 3",
    blanks_between=1,
)
print(conjoiner)
```

```text title="output"
Section 1

Section 2

Section 3
```

`blanks_between` only applies within a single `add()` call. Use `blanks_before` and `blanks_after` to control
spacing across calls:

```python linenums="1" title="Conjoiner with blanks_before and blanks_after"
conjoiner = Conjoiner()
conjoiner.add("first")
conjoiner.add("second", blanks_before=1, blanks_after=1)
conjoiner.add("third")
print(conjoiner)
```

```text title="output"
first

second

third
```

For explicit control, use `add_blank()` or `add_blanks()`:

```python linenums="1" title="Conjoiner with add_blanks()"
conjoiner = Conjoiner()
conjoiner.add("first")
conjoiner.add_blanks(2)
conjoiner.add("second")
print(conjoiner)
```

```text title="output"
first


second
```


### Customizing the join string

```python linenums="1" title="Conjoiner with custom join string"
conjoiner = Conjoiner(join_str=" | ")
conjoiner.add("one", "two", "three")
print(conjoiner)
```

```text title="output"
one | two | three
```


### Customizing blank lines

```python linenums="1" title="Conjoiner with custom blank character"
conjoiner = Conjoiner(blank="---")
conjoiner.add("First", "Second", blanks_between=2)
print(conjoiner)
```

```text title="output"
First
---
---
Second
```


### Practical example

Building a formatted report:

```python linenums="1" title="Conjoiner practical report example"
from snick import Conjoiner

def generate_report(title, items, footer):
    conjoiner = Conjoiner()

    conjoiner.add(f"=== {title} ===", blanks_after=1)

    if items:
        conjoiner.add("Items:")
        conjoiner.extend((f"  {i}. {item}" for (i, item) in enumerate(items, 1)), should_dedent=False)
    else:
        conjoiner.add("_No items found._")

    conjoiner.add(f"--- {footer} ---", blanks_before=1)
    return conjoiner

print(generate_report("Daily Report", ["Task A", "Task B", "Task C"], "End of Report"))
```

```text title="output"
=== Daily Report ===

Items:
  1. Task A
  2. Task B
  3. Task C

--- End of Report ---
```

----

## API reference

For full parameter and return type documentation, see the [Reference](reference.md) page.
