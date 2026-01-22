# snick

**Handy gadgets for taming indented text**

Stop wrestling with indented triple-quoted strings and awkward text formatting. snick makes it effortless to:

* **Dedent** triple-quoted strings while keeping your code beautifully indented
* **Build** complex multi-line output programmatically with the powerful `Conjoiner` class
* **Format** data structures with clean indentation and trailing commas
* **Clean up** terminal output by stripping ANSI codes and whitespace
* **Wrap and indent** long text blocks for logs and reports

All with **zero** dependencies.


## Quickstart

### Requirements

* Python 3.10 or greater


### Installation

Install the latest release from PyPI:

```bash
pip install snick
```


### Basic Usage

Ever struggle with indented triple-quoted strings in your code?

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

Output:
```
Oops! Something went wrong.
Here's what happened:
    - The flux capacitor overheated
    - Time circuits malfunctioned
Please try again later.
```

Build complex output on the fly:

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

Output:
```
Daily Report for Alice

Completed Tasks:
  ✓ Fix bug #123
  ✓ Review PR #456
  ✓ Deploy v2.0
```

Format data structures with proper indentation:

```python linenums="1" title="pretty_format() example"
data = {
    'user': 'bob',
    'permissions': ['read', 'write', 'execute'],
    'metadata': {'created': '2026-01-22', 'active': True}
}
print(snick.pretty_format(data))
```

Output:
```
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


For more examples and detailed documentation, see the [Features](features.md) page.


## What's with the name?

There's really no very good synonyms for the verb, 'indent'. However, there are several for the act of creating a small
dent in something. One of my favorites was 'snick'. It means "to cut a small notch or incision in". I think I'll use
that!
