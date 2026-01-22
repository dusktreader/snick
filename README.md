[![Latest Version](https://img.shields.io/pypi/v/snick?label=pypi-version&logo=python&style=plastic)](https://pypi.org/project/snick/)
[![Python Versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fdusktreader%2Fsnick%2Fmain%2Fpyproject.toml&style=plastic&logo=python&label=python-versions)](https://www.python.org/)
[![Build Status](https://github.com/dusktreader/snick/actions/workflows/main.yaml/badge.svg)](https://github.com/dusktreader/snick/actions/workflows/main.yaml)

# Gadgets for managing indented text

**Zero dependencies** - uses only Python standard library!

This library provides several text manipulation gadgets that are useful when dealing with indentation in text. You might
find them helpful when you are:

* logging blocks of text
* testing output
* formatting machine generated text in a human readable way


## What's with the name?

There's really no very good synonyms for the verb, 'indent'. However, there are several for the act of creating a small
dent in something. one of my favorites was 'snick'. It means "to cut a small notch or incision in". I think I'll use
that!


## Methods

Most of these methods have additional options and arguments that can be used to augment their output. This is just a
cursory over-view. Please consult the source code for more details


### `dedent()`

This method unindents a block of text by aligning all lines with the left most

This is very good if you wish to use python triple-quote strings in your code, like to start the text on its own line,
but do not wish to leave them indented:

```python
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

calling `Whatever.print_some_stuff()` will result in dedented output:

```
Here is some text
    here is some other text
    we don't want this indented
    when it's printed
      (to the console)
```


The dedent method also has an optional `should_strip` parameter that, if set to False, will preserve the newlines before
and after triple quoted text:

```python
    dummy_text = """
        Here is some text
            here is some other text
            we don't want this indented
            when it's printed
              (to the console)
    """
```

Calling `print(snick.dedent(dummy_text, should_strip=False)` will result in dedented output that preserves leading and
following newlines like so:

```

Here is some text
    here is some other text
    we don't want this indented
    when it's printed
      (to the console)

```


### `indent()`

This method indents a block of text. It's a thin wrapper around `textwrap.indent()`. However, it includes a default
prefix of 4 spaces. This could be handy if you want to indent some lines of text that you join with newline:

```python
print(snick.indent('\n'.join([
    'would be so nice',
    'to indent these',
    'i guess',
])))
```

The snippet above will produce:

```
   would be so nice
   to indent these
   i guess
```

The `indent` method also provides an option to skip the first line of text:

```python
print(snick.indent('\n'.join([
    'do not indent me',
    'indent me, though',
    'and me',
])))
```

The snippet above will produce:

```
do not indent me
    indent me, though
    and me
```


### `dedent_all()`

This function just applies a dedent to each argument you pass it separately and then joins them together. This is useful
if you want to dynamically produce some items that you need to add to some other long string. Here's an example:

```python
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

The snippet above would produce:

```python
Here is a long bit of text
as an introduction to the
following dynamic items:
--------------------------
* Item #1
* Item #2
* Item #3
```


### `unwrap()`

This method unwraps a block of text. It does this by joining all lines into a single string. It works on indented text
as well. This might be convenient if you have a very indented block of code and you need to type a long string out. You
could unwrap a triple-quoted block:

```python
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

The above code block would print this:
```
I need to have a very long string here, but it would go way outside of the line length limit and cause me all sorts of grief with the style checker. So, unwrap can help me here
```


### `conjoin`

This method is a lot like the python built-in `join`. The difference is that you don't need to wrap the stuff to wrap in
an iterable like a list or tuple. Instead, you can just pass the items as arguments to the `conjoin()` function. Here's
an example:

```python
print(snick.conjoin(
    "Here are some lines",
    "that I would like to join",
    "and it would be silly",
    "to have to wrap them in a",
    "list instead of just passing",
    "them as plain old arguments",
))
```

The above code would print this:
```
Here are some lines
that I would like to join
and it would be silly
to have to wrap them in a
list instead of just passing
them as plain old arguments
```

The `conjoin()` function also has a keyword argument `join_str` where you can override the default value (newline) with
string you like.


### `strip_whitespace()`

This method just removes all whitespace from a string. This includes newlines, tabs, spaces, etc. This method is handy
for writing tests that need to ignore whitespace used for readability/formatting:

```python
print(snick.strip_whitespace("""
    some text with    whitespace
    and whatnot
"""))
```

The above code block would print out the following:
```
sometextwithwhitespaceandwhatnot
```


### `strip_trailing_whitespace()`

This method just removes all trailing whitespace from each line in a multi-line string:

```python
print(snick.strip_trailing_whitespace(
    snick.conjoin(
        "  here is a string with a bundle of    ",
        "  trailing whitespace. ",
        "  we want it all gone.                    ",
    )
)
```

The above code block would print out the following:
```
  here is a string with a bundle of
  trailing whitespace.
  we want it all gone.
```


### `strip_ansi_escape_sequences()`

This method removes all ANSI escape sequences from text. These are commonly inserted into text by terminal applications
that make use of color and effects in the output.

Here's what text looks like when you show the control characters in the code:

```
\033[31mhere's some text\033[0m with
\033[32mansi control codes\033[0m added
\033[33mincluding a few\033[0m
\033[34mdifferent colors\033[0m
\033[1mand bold text\033[0m.
```

This will print nicely with red, green, blue and yellow text. However, if you need to include the text in a context
where the control characters can't be interpreted (like some instances in Github actions), they will only cause
problems. To remove them, use `strip_ansi_escape_sequences()`:

```python
print(snick.strip_ansi_escape_sequences(snick.dedent(
    """
    \033[31mhere's some text\033[0m with
    \033[32mansi control codes\033[0m added
    \033[33mincluding a few\033[0m
    \033[34mdifferent colors\033[0m
    \033[1mand bold text\033[0m.
    """
)
```

This will result in plan text like this:

```
here's some text with
ansi control codes added
including a few
different colors
and bold text."
```


### `indent_wrap()`

This method is used to wrap a long string and indent each wrapped line. It might be useful for wrapping and indenting
some string that's produced programmatically

```python
print("Here's some filler text:")
print(f"    {snick.indent_wrap(lorem.text())}")
```

The code block above might generate something like this:

```
Here's some filler text:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```


### `pretty_format()`

This method formats a Python data structure (dict, list, tuple, or any combination) with clean indentation and trailing
commas. It uses only Python's standard library and works with any type that has a `repr()`:

```python
data = {
    'name': 'example',
    'values': [1, 2, 3],
    'nested': {
        'key': 'value'
    }
}
print(snick.pretty_format(data))
```

The code block above would produce formatted output like this:
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

The formatter works with exotic types like `datetime`, `Decimal`, and custom classes with `__repr__` methods:

```python
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

This produces:
```
{
  'timestamp': datetime.datetime(2026, 1, 22, 20, 15, 30),
  'amount': Decimal('123.45'),
  'active': True,
  'notes': None,
}
```

You can customize the indentation with the `indent` parameter (defaults to 2 spaces):
```python
print(snick.pretty_format(data, indent=4))
```


### `pretty_print()`

This method is the same as `pretty_format()` but prints to a stream (stdout by default) instead of returning a string:


### `enboxify()`

This method just draws a box around some text. This is especially useful for logging when you want to make something
really pop out:

```python
print(snick.enboxify("""
    here's some text that we
    want to put into a box.
    That will make it look
    so very nice
"""))
```

The code-block above will produce output like this:

```
****************************
* here's some text that we *
* want to put into a box.  *
* That will make it look   *
* so very nice             *
****************************
```


## Builder class

The `Builder` class provides a convenient way to incrementally construct multi-line strings. It's especially useful when
you need to build complex text output programmatically, where different parts of the text may be generated conditionally
or in loops.

For the most common usecases, parts added to the builder will be dedenteds automatically (though this behavior is
configurable). Then, the parts are joined together with newlines (though this is also configurable) when the Builder is
rendered to string. This makes it easy to work with indented triple-quoted strings in your code while producing clean
output.


### Basic Usage

```python
from snick import Builder

builder = Builder()
builder.add("First line")
builder.add("Second line")
print(builder)
```

This will output:
```
First line
Second line
```


### Adding Multiple Parts at Once

You can add multiple parts in a single call:

```python
builder = Builder()
builder.add(
    "Line 1",
    "Line 2",
    "Line 3",
)
print(builder)
```


### Automatic Dedenting

By default, the Builder will dedent each part, making it easy to use indented triple-quoted strings:

```python
builder = Builder()
builder.add(
    """
    This text is indented in the code
    but will be dedented in the output
    """
)
builder.add(
    """
    Same with this text
    it looks nice in the code
    """
)
print(builder)
```

This produces:
```
This text is indented in the code
but will be dedented in the output
Same with this text
it looks nice in the code
```

To preserve indentation, set `should_dedent=False`:

```python
builder = Builder()
builder.add("    Keep this indented", should_dedent=False)
```


### Adding Blank Lines

There are several ways to add blank lines with the Builder:

#### Using `blanks_between`

The `blanks_between` parameter inserts blanks between multiple parts in a single `add()` call:

```python
builder = Builder()
builder.add(
    "Section 1",
    "Section 2",
    "Section 3",
    blanks_between=1,
)
print(builder)
```

This outputs:
```
Section 1

Section 2

Section 3
```

Note that `blanks_between` only applies within a single `add()` call. Multiple `add()` calls will not insert blanks
between them by default:

```python
builder = Builder()
builder.add("First call")
builder.add("Second call")
print(builder)
```

This produces:
```
First call
Second call
```

#### Using `blanks_before` and `blanks_after`

To add blanks before or after a group of parts, use the `blanks_before` and `blanks_after` parameters:

```python
builder = Builder()
builder.add("first")
builder.add("second", blanks_before=1, blanks_after=1)
builder.add("third")
print(builder)
```

This outputs:
```
first

second

third
```

These parameters work with both `add()` and `extend()` methods.

#### Using `add_blank()` and `add_blanks()`

For more explicit control, you can use the `add_blank()` and `add_blanks()` methods:

```python
builder = Builder()
builder.add("first")
builder.add_blanks(2)
builder.add("second")
print(builder)
```

This outputs:
```
first


second
```


### Customizing the Join String

By default, parts are joined with newlines, but you can customize this:

```python
builder = Builder(join_str=" | ")
builder.add("one", "two", "three")
print(builder)
```

This outputs:
```
one | two | three
```


### Customizing Blank Lines

You can also customize what a "blank" line looks like:

```python
builder = Builder(blank="---")
builder.add("First", "Second", blanks_between=2)
print(builder)
```

This produces:
```
First
---
---
Second
```


### Practical Example

Here's a realistic example of building a formatted report:

```python
from snick import Builder

def generate_report(title, items, footer):
    builder = Builder()

    builder.add(f"=== {title} ===", blanks_after=1)

    if items:
        builder.add("Items:")
        builder.extend((f"  {i}. {item}" for (i, item) in enumerate(items, 1)), should_dedent=False)
    else:
        builder.add("_No items found._")

    builder.add(f"--- {footer} ---", blanks_before=1)
    return builder


print(generate_report("Daily Report", ["Task A", "Task B", "Task C"], "End of Report"))
```

This would output:
```
=== Daily Report ===

Items:
  1. Task A
  2. Task B
  3. Task C

--- End of Report ---
```
