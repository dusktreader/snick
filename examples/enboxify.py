"""
Example: enboxify()

Draws an ASCII box around a block of text.

Run it: `uv run python examples/enboxify.py`
"""

import snick

# Default box character
print(snick.enboxify("May the Force be with you."))
print()

# Custom box character
print(snick.enboxify("Do. Or do not. There is no try.", boxchar="#"))
print()

# Extra padding
print(snick.enboxify("I am one with the Force. The Force is with me.", hspace=3, vspace=1))
print()

# Multi-line block — box fits the widest line
print(
    snick.enboxify(
        """
        Rebel Alliance Fleet
        Commander: Admiral Ackbar
        Status: It's a trap!
        """
    )
)
