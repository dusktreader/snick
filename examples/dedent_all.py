"""
Example: dedent_all()

Dedents each string blob independently and then joins them.

Run it: `uv run python examples/dedent_all.py`
"""

import snick

# Compose a passage from separately-indented blocks
passage = snick.dedent_all(
    """
    In my experience, there is no such thing as luck.
    """,
    """
    Your eyes can deceive you.
    Don't trust them.
    """,
)
print(passage)
print()

# Custom join_str between blocks
dialogue = snick.dedent_all(
    """
    The dark side of the Force is a pathway
    to many abilities some consider to be unnatural.
    """,
    """
    It's not a story the Jedi would tell you.
    """,
    join_str="\n\n---\n\n",
)
print(dialogue)
