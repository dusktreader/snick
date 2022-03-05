# Gadgets for managing indented text

This library provides several text manipulation gadgets that are useful when
dealing with indentation in text. You might find them helpful when you are:

* logging blocks of text
* testing output
* formatting machine generated text in a human readable way


## What's with the name?

There's really no very good synonyms for the verb, 'indent'. However, there
are several for the act of creating a small dent in something. one of my
favorites was 'snick'. It means "to cut a small notch or incision in". I
think I'll use that!


## Methods

Most of these methods have additional options and arguments that can be used
to augment their output. This is just a cursory over-view. Please consult the
source code for more details


### dedent

This method unindents a block of text by aligning all lines with the left most

This is very good if you wish to use python triple-quote strings in your code,
like to start the text on its own line, but do not wish to leave them indented:

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


The dedent method also has an optional `should_strip` parameter that, if set to False,
will preserve the newlines before and after triple quoted text:

```python
    dummy_text = """
        Here is some text
            here is some other text
            we don't want this indented
            when it's printed
              (to the console)
    """
```

calling `print(snick.dedent(dummy_text, should_strip=False)` will result in dedented
output that preserves leading and following newlines like so:

```

Here is some text
    here is some other text
    we don't want this indented
    when it's printed
      (to the console)

```


### indent

This method indents a block of text. It's a thin wrapper around `textwrap.indent()`.
However, it includes a default prefix of 4 spaces. This could be handy if you want
to indent some lines of text that you join with newline:

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


### dedent_all

This function just applies a dedent to each argument you pass it separately and then
joins them together. This is useful if you want to dynamically produce some items
that you need to add to some other long string. Here's an example:

```python
print(snick.dedent_all(
    """
    Here is a long bit of text
    as an introduction to the
    folowing dynamic items:
    --------------------------
    """,
    *(f"* Item #{i}" for i in range(1, 4)),
))
```

The snippet above would produce:

```python
Here is a long bit of text
as an introduction to the
folowing dynamic items:
--------------------------
* Item #1
* Item #2
* Item #3
```


### unwrap

This method unwraps a block of text. It does this by joining all lines into
a single string. It works on indented text as well. This might be convenient
if you have a very indented block of code and you need to type a long string
out. You could unwrap a triple-quoted block:

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


### conjoin

This method is a lot like the python built-in `join`. The difference is that you don't
need to wrap the stuff to wrap in an iterable like a list or tuple. Instead, you can
just pass the items as arguments to the `conjoin()` function. Here's an example:

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

The `conjoin()` function also has a keyword argument `join_str` where you can override
the default value (newline) with string you like.


### strip_whitespace

This method just removes all whitespace from a string. This includes newlines,
tabs, spaces, etc. This method is handy for writing tests that need to ignore
whitespace used for readability/formatting:

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


### indent_wrap

This method is used to wrap a long string and indent each wrapped line. It might
be useful for wrapping and indenting some string that's produced programatically

```python
print("Here's some filler text:")
print(f"    {snick.indent_wrap(lorem.text())}")
```

The code block above might generate somethign like this:

```
Here's some filler text:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```


### pretty_print

This method can be used to pretty-print a dictionary:

```python
snick.pretty_print("'a': {'b': 1, 'c': {'d': 2}, 'e': 3}, 'f': 4}")
```

The code block above would produce formatted output like this:
```
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
```


### pretty_format

This method is the same as `pretty_print()` but returns the string instead of
printing to a IO stream


### enboxify

This method just draws a box around some text. This is especially useful for
logging when you want to make something really pop out:

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
