# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


# Unreleased

# v2.1.0 - 2025-04-18

- Added `strip_ansi_escape_sequences()` method.


# v2.0.0 - 2025-04-18

- Dropped support for python 3.8
- Converted to a uv project


# v1.5.0 - 2025-04-18

- Added `skip_first_line` option to `indent()`

# v1.4.1 - 2024-10-17

- Fixed links in project metadata


# v1.4.0 - 2024-10-17

- Dropped support for python 3.6 and 3.7
- Added support for python 3.11 and 3.12
- Loosened dependencies
- Added more metadata to pyproject.toml


# v1.3.0 - 2022-03-29

- Restored support for python 3.6


# v1.2.0 - 2022-03-04

- Added `conjoin()`` function
- Added ``dedent_all()`` function


# v1.1.0 - 2021-11-24

- Added optional parameter ``should_strip`` to ``dedent``
- Added support for mypy with typehints
- Added Makefile
- Enhanced quality checks


# v1.0.0 - 2020-11-23

- Renamed to 'snick'
- Released as open source on pypi & github


# v0.3.1 - 2020-10-02

- Downgraded back to python 3.7 for compatibility


# v0.3.0 - 2020-10-02

- Renamed package to pa-text-tools
- Upgraded to python 3.8
- Added black, isort, and others as dev dependencies
- Added pre-commit hooks


# v0.2.3 - 2019-05-20

- Enriched README


# v0.2.2 - 2019-05-17

- Added missing source files back


# v0.2.1 - 2019-05-16

- Added dedent method


# v0.2.0 - 2019-05-13

- Added this CHANGELOG
- Moved methods into a methods module
- Added more tools like strip_whitespace, pretty_format, and enboxify
