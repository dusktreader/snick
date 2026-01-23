from collections.abc import Iterable
from dataclasses import dataclass, field
import sys

if sys.version_info >= (3, 12):
    from typing import override
else:

    def override(f):  # pyright: ignore[reportUnreachable]
        return f


from snick.methods import dedent


@dataclass
class Conjoiner:
    """
    Conjoins text parts into a single string.

    This is most useful when building multi-line strings where you want to add parts as you go and then
    produce a final, joined string.
    """

    parts: list[str] = field(default_factory=list)
    join_str: str = "\n"
    blank: str = ""

    @override
    def __str__(self) -> str:
        return self.join_str.join(self.parts)

    def add(
        self,
        *parts: str,
        should_dedent: bool = True,
        blanks_between: int = 0,
        blanks_before: int = 0,
        blanks_after: int = 0,
    ) -> None:
        """
        Add a new part(s) to the conjoiner.

        Args:
            parts:          One or more string parts to add.
            should_dedent:  If `True`, dedent each part before adding it. Defaults to `True`.
            blanks_between: Number of blanks to insert between each part for multiple parts. Defaults to `0`.
            blanks_before:  Number of blanks to insert before the first part. Defaults to `0`.
            blanks_after:   Number of blanks to insert after the last part. Defaults to `0`.
        """
        self.add_blanks(blanks_before)
        for i, part in enumerate(parts):
            if i > 0:
                self.parts.extend([self.blank] * blanks_between)
            if should_dedent:
                part = dedent(part)
            self.parts.append(part)
        self.add_blanks(blanks_after)

    def extend(
        self,
        parts: Iterable[str],
        should_dedent: bool = True,
        blanks_between: int = 0,
        blanks_before: int = 0,
        blanks_after: int = 0,
    ) -> None:
        """
        Add new parts to the conjoiner.

        This is just a convenience method that takes a list of parts instead of variadic arguments.

        Args:
            parts:          One or more string parts to add.
            should_dedent:  If `True`, dedent each part before adding it. Defaults to `True`.
            blanks_between: Number of blanks to insert between each part for multiple parts. Defaults to `0`.
            blanks_before:  Number of blanks to insert before the first part. Defaults to `0`.
            blanks_after:   Number of blanks to insert after the last part. Defaults to `0`.
        """
        self.add(
            *parts,
            should_dedent=should_dedent,
            blanks_between=blanks_between,
            blanks_before=blanks_before,
            blanks_after=blanks_after,
        )

    def add_blanks(self, count: int) -> None:
        """
        Add blanks to the conjoiner.

        Args:
            count: Number of blank lines to add.
        """
        self.parts.extend([self.blank] * count)

    def add_blank(self) -> None:
        """
        Add a single blank to the conjoiner.
        """
        self.add_blanks(1)
