# Features

snick provides a comprehensive set of text manipulation functions and a powerful `Conjoiner` class for constructing multi-line strings. All functions accept additional keyword arguments to customize their behavior.

## Core Functions

### `dedent()`

Unindents a block of text by aligning all lines with the leftmost non-whitespace character. This is especially useful for triple-quoted strings in your code:

```python linenums="1" title="dedent() example"
import snick

class Whatever:
    @staticmethod
    def print_some_stuff():
        print(snick.dedent("""
            Here is some text
                here is some other text
                we don't want this indented
                when it's printed
                  (to the console)
        """))
```

Output:
```
Here is some text
    here is some other text
    we don't want this indented
    when it's printed
      (to the console)
```

**Parameters:**

* `should_strip` (bool): If `False`, preserves leading and trailing newlines. Default is `True`.

```python linenums="1" title="dedent() with should_strip=False"
dummy_text = """
    Here is some text
        here is some other text
"""
print(snick.dedent(dummy_text, should_strip=False))
```

Output (with blank lines preserved):
```

Here is some text
    here is some other text

```

### `indent()`

Indents a block of text. This is a thin wrapper around `textwrap.indent()` with sensible defaults:

```python linenums="1" title="indent() example"
print(snick.indent('\n'.join([
    'would be so nice',
    'to indent these',
    'i guess',
])))
```

Output:
```
    would be so nice
    to indent these
    i guess
```

**Parameters:**

* `prefix` (str): The string to prepend to each line. Default is `"    "` (4 spaces).
* `predicate` (callable): A function to determine which lines to indent.
* `skip_first_line` (bool): If `True`, the first line is not indented. Default is `False`.

```python linenums="1" title="indent() with skip_first_line"
print(snick.indent('\n'.join([
    'do not indent me',
    'indent me, though',
    'and me',
]), skip_first_line=True))
```

Output:
```
do not indent me
    indent me, though
    and me
```

### `dedent_all()`

Applies `dedent()` to each argument separately and joins them together:

```python linenums="1" title="dedent_all() example"
print(snick.dedent_all(
    """
    Here is a long bit of text
    as an introduction to the
    following dynamic items:
    --------------------------
    """,
    *(f"* Item #{i}" for i in range(1, 4)),
))
```

Output:
```
Here is a long bit of text
as an introduction to the
following dynamic items:
--------------------------
* Item #1
* Item #2
* Item #3
```

### `unwrap()`

Unwraps a block of text by joining all lines into a single string. Useful for long strings in deeply indented code:

```python linenums="1" title="unwrap() example"
if True:
    if True:
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            if True:
                                print(snick.unwrap("""
                                    I need to have a very long string here, but
                                    it would go way outside of the line length
                                    limit and cause me all sorts of grief with
                                    the style checker. So, unwrap can help me
                                    here
                                """))
```

Output:
```
I need to have a very long string here, but it would go way outside of the line length limit and cause me all sorts of grief with the style checker. So, unwrap can help me here
```

### `conjoin()`

Like Python's built-in `join()`, but accepts items as arguments instead of requiring an iterable:

```python linenums="1" title="conjoin() example"
print(snick.conjoin(
    "Here are some lines",
    "that I would like to join",
    "and it would be silly",
    "to have to wrap them in a",
    "list instead of just passing",
    "them as plain old arguments",
))
```

Output:
```
Here are some lines
that I would like to join
and it would be silly
to have to wrap them in a
list instead of just passing
them as plain old arguments
```

**Parameters:**

* `join_str` (str): The string used to join the arguments. Default is `"\n"`.

### `strip_whitespace()`

Removes all whitespace from a string, including newlines, tabs, and spaces. Handy for tests:

```python linenums="1" title="strip_whitespace() example"
print(snick.strip_whitespace("""
    some text with    whitespace
    and whatnot
"""))
```

Output:
```
sometextwithwhitespaceandwhatnot
```

### `strip_trailing_whitespace()`

Removes trailing whitespace from each line in a multi-line string:

```python linenums="1" title="strip_trailing_whitespace() example"
print(snick.strip_trailing_whitespace(
    snick.conjoin(
        "  here is a string with a bundle of    ",
        "  trailing whitespace. ",
        "  we want it all gone.                    ",
    )
))
```

Output:
```
  here is a string with a bundle of
  trailing whitespace.
  we want it all gone.
```

### `strip_ansi_escape_sequences()`

Removes ANSI escape sequences from text. These are commonly added by terminal applications for color and formatting:

```python linenums="1" title="strip_ansi_escape_sequences() example"
print(snick.strip_ansi_escape_sequences(snick.dedent("""
    \033[31mhere's some text\033[0m with
    \033[32mansi control codes\033[0m added
    \033[33mincluding a few\033[0m
    \033[34mdifferent colors\033[0m
    \033[1mand bold text\033[0m.
""")))
```

Output:
```
here's some text with
ansi control codes added
including a few
different colors
and bold text.
```

### `indent_wrap()`

Wraps a long string and indents each wrapped line:

```python linenums="1" title="indent_wrap() example"
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print("Here's some filler text:")
print(snick.indent_wrap(long_text, width=70, indent=4))
```

Output:
```
Here's some filler text:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

**Parameters:**

* `width` (int): The maximum width of each line. Default is `80`.
* `indent` (int): Number of spaces to indent. Default is `4`.

### `pretty_format()`

Formats Python data structures (dict, list, tuple, or combinations) with clean indentation and trailing commas:

```python linenums="1" title="pretty_format() example"
data = {
    'name': 'example',
    'values': [1, 2, 3],
    'nested': {
        'key': 'value'
    }
}
print(snick.pretty_format(data))
```

Output:
```
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

Works with exotic types like `datetime`, `Decimal`, and custom classes:

```python linenums="1" title="pretty_format() with datetime and Decimal"
from datetime import datetime
from decimal import Decimal

data = {
    'timestamp': datetime(2026, 1, 22, 20, 15, 30),
    'amount': Decimal('123.45'),
    'active': True,
    'notes': None,
}
print(snick.pretty_format(data))
```

Output:
```
{
  'timestamp': datetime.datetime(2026, 1, 22, 20, 15, 30),
  'amount': Decimal('123.45'),
  'active': True,
  'notes': None,
}
```

**Parameters:**

* `indent` (int): Number of spaces per indentation level. Default is `2`.

### `pretty_print()`

Same as `pretty_format()` but prints to a stream instead of returning a string:

```python linenums="1" title="pretty_print() example"
snick.pretty_print(data)  # Prints to stdout
```

**Parameters:**

* `stream` (file-like): The output stream. Default is `sys.stdout`.
* `indent` (int): Number of spaces per indentation level. Default is `2`.

### `enboxify()`

Draws a box around text. Great for making log messages stand out:

```python linenums="1" title="enboxify() example"
print(snick.enboxify("""
    here's some text that we
    want to put into a box.
    That will make it look
    so very nice
"""))
```

Output:
```
****************************
* here's some text that we *
* want to put into a box.  *
* That will make it look   *
* so very nice             *
****************************
```

**Parameters:**

* `width` (int): The width of the box. If not specified, auto-calculates based on content.
* `box_char` (str): The character to use for the box. Default is `"*"`.

## Conjoiner Class

The `Conjoiner` class provides a convenient way to incrementally construct multi-line strings. It's especially useful for complex text output that's generated programmatically.

### Basic Usage

```python linenums="1" title="Conjoiner basic usage"
from snick import Conjoiner

conjoiner = Conjoiner()
conjoiner.add("First line")
conjoiner.add("Second line")
print(conjoiner)
```

Output:
```
First line
Second line
```

### Adding Multiple Parts

Add multiple parts in a single call:

```python linenums="1" title="Conjoiner adding multiple parts"
conjoiner = Conjoiner()
conjoiner.add(
    "Line 1",
    "Line 2",
    "Line 3",
)
print(conjoiner)
```

### Automatic Dedenting

By default, Conjoiner dedents each part:

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

Output:
```
This text is indented in the code
but will be dedented in the output
Same with this text
it looks nice in the code
```

To preserve indentation, use `should_dedent=False`:

```python linenums="1" title="Conjoiner preserving indentation"
conjoiner = Conjoiner()
conjoiner.add("    Keep this indented", should_dedent=False)
```

### Adding Blank Lines

#### Using `blanks_between`

Insert blank lines between parts within a single `add()` call:

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

Output:
```
Section 1

Section 2

Section 3
```

Note: `blanks_between` only applies within a single `add()` call. Multiple `add()` calls won't insert blanks by default.

#### Using `blanks_before` and `blanks_after`

```python linenums="1" title="Conjoiner with blanks_before and blanks_after"
conjoiner = Conjoiner()
conjoiner.add("first")
conjoiner.add("second", blanks_before=1, blanks_after=1)
conjoiner.add("third")
print(conjoiner)
```

Output:
```
first

second

third
```

#### Using `add_blank()` and `add_blanks()`

For explicit control:

```python linenums="1" title="Conjoiner with add_blanks()"
conjoiner = Conjoiner()
conjoiner.add("first")
conjoiner.add_blanks(2)
conjoiner.add("second")
print(conjoiner)
```

Output:
```
first


second
```

### Customizing Join String

```python linenums="1" title="Conjoiner with custom join string"
conjoiner = Conjoiner(join_str=" | ")
conjoiner.add("one", "two", "three")
print(conjoiner)
```

Output:
```
one | two | three
```

### Customizing Blank Lines

```python linenums="1" title="Conjoiner with custom blank character"
conjoiner = Conjoiner(blank="---")
conjoiner.add("First", "Second", blanks_between=2)
print(conjoiner)
```

Output:
```
First
---
---
Second
```

### Practical Example

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

Output:
```
=== Daily Report ===

Items:
  1. Task A
  2. Task B
  3. Task C

--- End of Report ---
```

## API Reference

For detailed API documentation including all parameters and return types, see the [Reference](reference.md) page.
