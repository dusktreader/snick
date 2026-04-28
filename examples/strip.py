"""
Example: strip utilities

strip_whitespace(), strip_trailing_whitespace(), and strip_ansi_escape_sequences().

Run it: `uv run python examples/strip.py`
"""

import snick

# strip_whitespace — remove ALL whitespace
print(repr(snick.strip_whitespace("  R2  -  D2  \n\t!")))
print()

# strip_trailing_whitespace — trim only trailing whitespace on each line
lines = "  Luke Skywalker   \n  Han Solo\t\n  Leia Organa  "
for line in snick.strip_trailing_whitespace(lines).split("\n"):
    print(repr(line))
print()

# strip_ansi_escape_sequences — remove terminal colour codes
coloured = "\x1b[34mBlue Squadron\x1b[0m and \x1b[31mRed Squadron\x1b[0m"
print("Before:", repr(coloured))
print("After :", repr(snick.strip_ansi_escape_sequences(coloured)))
