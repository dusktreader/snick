"""
Example: dedent()

Strips common leading indentation from multi-line strings.

Run it: `uv run python examples/dedent.py`
"""

import snick

# Standard usage — removes indentation added by source-code nesting
quote = snick.dedent(
    """
    The Force will be with you.
    Always.
    """
)
print(quote)
print()

# should_strip=False — preserves surrounding blank lines
raw = snick.dedent(
    """
    I find your lack of faith disturbing.
    """,
    should_strip=False,
)
print(repr(raw))
