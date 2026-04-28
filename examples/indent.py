"""
Example: indent()

Adds a prefix to every line of a string.

Run it: `uv run python examples/indent.py`
"""

import snick

# Default 4-space indent
print(snick.indent("Luke Skywalker\nHan Solo\nLeia Organa"))
print()

# Custom prefix — useful for quoted text or comment blocks
print(snick.indent("Luke Skywalker\nHan Solo\nLeia Organa", prefix="> "))
print()

# skip_first_line — leave a label unindented while indenting the rest
print(snick.indent("Jedi Order:\nObi-Wan Kenobi\nYoda\nMace Windu", skip_first_line=True))
