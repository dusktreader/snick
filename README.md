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

```
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

```
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


### unwrap

This method unwraps a block of text. It does this by joining all lines into
a single string. It works on indented text as well. This might be convenient
if you have a very indented block of code and you need to type a long string
out. You could unwrap a triple-quoted block:

```
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


# strip_whitespace

This method just removes all whitespace from a string. This includes newlines,
tabs, spaces, etc. This method is handy for writing tests that need to ignore
whitespace used for readability/formatting:

```
print(snick.strip_whitespace("""
    some text with    whitespace
    and whatnot
"""))
```

The above code block would print out the following:
```
sometextwithwhitespaceandwhatnot
```


# indent_wrap

This method is used to wrap a long string and indent each wrapped line. It might
be useful for wrapping and indenting some string that's produced programatically

```
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


# pretty_print

This method can be used to pretty-print a dictionary:

```
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


# pretty_format

This method is the same as pretty_print but returns the string instead of
printing to a IO stream


# enboxify

This method just draws a box around some text. This is especially useful for
logging when you want to make something really pop out:

```
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
