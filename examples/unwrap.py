"""
Example: unwrap()

Collapses an indented, wrapped paragraph into a single line.

Run it: `uv run python examples/unwrap.py`
"""

import snick

# Flatten a triple-quoted paragraph into one line
crawl = snick.unwrap(
    """
    It is a period of civil war. Rebel spaceships,
    striking from a hidden base, have won their first
    victory against the evil Galactic Empire.
    """
)
print(crawl)
print()

# Custom separator between the original lines
planets = snick.unwrap(
    """
    Tatooine
    Hoth
    Dagobah
    """,
    separator=" / ",
)
print(planets)
