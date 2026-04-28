"""
Example: Conjoiner

Accumulates string parts and produces a joined string on demand.

Run it: `uv run python examples/conjoiner.py`
"""

from snick import Conjoiner

# Build a report incrementally
report = Conjoiner()
report.add("Rebel Alliance — Mission Briefing")
report.add("Objective", "Destroy the Death Star", blanks_before=1, blanks_between=1)
report.add("Pilots:", blanks_before=1)
report.extend(["  - Luke Skywalker", "  - Wedge Antilles", "  - Biggs Darklighter"])
report.add("May the Force be with you.", blanks_before=1)

print(str(report))
print()

# The += operator as a shorthand for add()
haiku = Conjoiner()
haiku += "Stars guide the bold ship"
haiku += "The Force hums through every heart"
haiku += "Hope ignites the dark"
print(str(haiku))
