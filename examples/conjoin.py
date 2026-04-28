"""
Example: conjoin()

Joins multiple strings with a configurable separator.

Run it: `uv run python examples/conjoin.py`
"""

import snick

# Default separator — newline
crawl = snick.conjoin(
    "A long time ago in a galaxy far,",
    "far away....",
)
print(crawl)
print()

# Custom separator
roster = snick.conjoin("Luke Skywalker", "Han Solo", "Leia Organa", join_str=" | ")
print(roster)
