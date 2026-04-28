# snick

![snick-hero](images/snick-hero.png){ .hero-image width=500 }

**Handy gadgets for taming indented text**

A small collection of practical utilities for working with indented strings and text formatting:

- **Dedent** triple-quoted strings without giving up indented code
- **Build** multi-line output line by line with `Conjoiner`
- **Format** data structures like `pprint`, but with `json.dumps`-style indentation and trailing commas
- **Strip** ANSI codes and stray whitespace from terminal output
- **Wrap and indent** text blocks for logs and reports

Built on the Python standard library. Nothing extra to install.


## Quickstart

### Requirements

- Python 3.10 or greater


### Installation

Install the latest release from PyPI:

```shell
pip install snick
```


### Basic usage

Dedent a triple-quoted string without sacrificing indented code:

```python linenums="1" title="dedent() example"
import snick

def my_function():
    return snick.dedent(
        """
        Oops! Something went wrong.
        Here's what happened:
            - The flux capacitor overheated
            - Time circuits malfunctioned
        Please try again later.
        """
    )

print(my_function())
```

```text title="output"
Oops! Something went wrong.
Here's what happened:
    - The flux capacitor overheated
    - Time circuits malfunctioned
Please try again later.
```

Build multi-line output line by line:

```python linenums="1" title="Conjoiner example"
def generate_report(name, tasks):
    report = snick.Conjoiner()
    report.add(f"Daily Report for {name}", blanks_after=1)

    if tasks:
        report.add("Completed Tasks:")
        report.extend(f"  ✓ {task}" for task in tasks)
    else:
        report.add("No tasks completed today.")

    return str(report)

print(generate_report("Alice", ["Fix bug #123", "Review PR #456", "Deploy v2.0"]))
```

```text title="output"
Daily Report for Alice

Completed Tasks:
  ✓ Fix bug #123
  ✓ Review PR #456
  ✓ Deploy v2.0
```

Format a data structure with consistent indentation:

```python linenums="1" title="pretty_format() example"
data = {
    'user': 'bob',
    'permissions': ['read', 'write', 'execute'],
    'metadata': {'created': '2026-01-22', 'active': True}
}
print(snick.pretty_format(data))
```

```text title="output"
{
  'user': 'bob',
  'permissions': [
    'read',
    'write',
    'execute',
  ],
  'metadata': {
    'created': '2026-01-22',
    'active': True,
  },
}
```

For more examples, see the [Features](features.md) page.


!!! tip "See it in action"
    The fastest way to get a feel for snick is to run the interactive demo:

    ```shell
    uvx --from=snick[demo] snick-demo
    ```

    No install required. See the [Demo](demo.md) page for a full overview of what it covers.

    Prefer reading code? The [`examples/`](https://github.com/dusktreader/snick/tree/main/examples)
    directory has a standalone script for every feature.


## What's with the name?

There aren't many good synonyms for the verb "indent", but there are a few for the act of making a small dent in
something. "Snick" means "to cut a small notch or incision in." Close enough.
