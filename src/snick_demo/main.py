from __future__ import annotations

from collections.abc import Callable
from typing import Annotated, Optional

import snick
import typer
from auto_name_enum import AutoNameEnum, auto
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Confirm

from snick_demo.helpers import get_demo_functions, run_demo


class Feature(AutoNameEnum):
    conjoin = auto()
    conjoiner = auto()
    dedent = auto()
    dedent_all = auto()
    enboxify = auto()
    indent = auto()
    pretty = auto()
    strip = auto()
    unwrap = auto()


def start(
    feature: Annotated[
        Optional[Feature],
        typer.Option(
            help="The feature to demo. If not provided, demo ALL",
        ),
    ] = None,
):
    """
    This cli app will demo the features of `snick`!

    Note: If no features are selected for the demo, all of them will be shown.
    """
    features: list[Feature]
    if feature is None:
        features = list(Feature.__members__.values())
    else:
        features = [feature]

    feature_map: dict[Feature, list[Callable[..., None]]] = {}
    for feat in features:
        feature_map[feat] = get_demo_functions(feat)

    override_label_map: dict[Feature, str] = {
        Feature.pretty: "pretty_format() / pretty_print()",
        Feature.strip: "strip_whitespace() / strip_trailing_whitespace() / strip_ansi_escape_sequences()",
    }

    greeting_lines = [
        "Welcome to the `snick` demo!",
        "",
        "This program will show you the different features available in `snick` and what it's like to use them.",
        "",
        "The following features will be included:",
    ]
    for feat in features:
        label = override_label_map.get(feat, f"{feat}()")
        greeting_lines.append(f"- `{label}`")
        for demo in feature_map[feat]:
            greeting_lines.append(f"  - `{demo.__name__}()`")  # ty: ignore[unresolved-attribute]

    console = Console()
    console.clear()
    console.print(
        Panel(
            Markdown(snick.conjoin(*greeting_lines)),
            padding=1,
            title="[green]Welcome to snick![/green]",
            subtitle="[blue]https://github.com/dusktreader/snick[/blue]",
        )
    )
    console.print()
    console.print()
    further: bool = Confirm.ask("Would you like to continue?", default=True)
    if not further:
        return

    for feat, demos in feature_map.items():
        for demo in demos:
            further = run_demo(demo, console, override_label=override_label_map.get(feat))
            if not further:
                break

    console.clear()
    console.print(
        Panel(
            Markdown(
                snick.dedent(
                    """
                    Thanks for checking out `snick`!

                    I hope these features will be useful for you.

                    If you would like to learn more, please check out the
                    [source repository](https://github.com/dusktreader/snick)
                    """
                ),
            ),
            padding=1,
            title="[green]Thanks![/green]",
            subtitle="[blue]https://github.com/dusktreader/snick[/blue]",
        )
    )
    console.print()
    console.print()


def main():
    typer.run(start)
