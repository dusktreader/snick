# Demo

snick ships with an interactive demo that walks through every feature, one function at a time. It's the quickest
way to see what the library can do before writing any code of your own.


## Installation

The demo depends on `typer`, `rich`, and `auto-name-enum`, which aren't pulled in by a plain `snick` install.
Add them with the `demo` extra:

```shell
uv add snick[demo]
```

To try it without touching your current environment:

```shell
uvx --from=snick[demo] snick-demo
```


## Running the demo

```shell
snick-demo
```

The demo opens with a feature listing and asks whether to continue. Each step shows the source code and the
captured output, then prompts you to move on.

| Feature      | What it covers                                              |
|--------------|-------------------------------------------------------------|
| `conjoin`    | Joining strings with a configurable separator               |
| `conjoiner`  | Building multi-line output incrementally with `Conjoiner`   |
| `dedent`     | Stripping common indentation from triple-quoted strings     |
| `dedent_all` | Dedenting multiple blobs and joining them                   |
| `enboxify`   | Drawing an ASCII box around a block of text                 |
| `indent`     | Adding a prefix to every line                               |
| `unwrap`     | Collapsing a wrapped paragraph into a single line           |
| `strip`      | Removing whitespace and ANSI escape sequences               |
| `pretty`     | Rendering nested data structures with clean indentation     |

To jump straight to one feature, pass `--feature`:

```shell
snick-demo --feature=conjoiner
```

For the full list of options:

```shell
snick-demo --help
```


## Examples

If you prefer reading standalone code over an interactive tour, the
[`examples/`](https://github.com/dusktreader/snick/tree/main/examples) directory has a self-contained script
for every feature:

| Script               | Run it                                    |
|----------------------|-------------------------------------------|
| `examples/conjoin.py`    | `uv run python examples/conjoin.py`   |
| `examples/conjoiner.py`  | `uv run python examples/conjoiner.py` |
| `examples/dedent.py`     | `uv run python examples/dedent.py`    |
| `examples/dedent_all.py` | `uv run python examples/dedent_all.py`|
| `examples/enboxify.py`   | `uv run python examples/enboxify.py`  |
| `examples/indent.py`     | `uv run python examples/indent.py`    |
| `examples/unwrap.py`     | `uv run python examples/unwrap.py`    |
| `examples/strip.py`      | `uv run python examples/strip.py`     |
| `examples/pretty.py`     | `uv run python examples/pretty.py`    |


## Check out the source

The demo source is worth a look if you want concrete examples of how to use each snick function in context.

[Browse it on GitHub](https://github.com/dusktreader/snick/tree/main/src/snick_demo)
