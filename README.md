# stupid-simple-tools

A collection of stupid simple command-line tools.

## Installation

Install the package using pip:

```bash
pip install .
```

Or for development:

```bash
pip install -e .
```

## Universal Invocation

All tools in this suite can be run using the `sst.<toolname>` pattern. This provides a consistent and easy-to-remember interface for accessing any tool.

## Available Tools

### sst.pdf-merge

Concatenate multiple PDF files into a single PDF.

**Usage:**

```bash
sst.pdf-merge --input file1.pdf file2.pdf file3.pdf --output merged.pdf
```

**Arguments:**

- `--input`: List of PDF files to merge (required, one or more files)
- `--output`: Name of the output file (required)

**Example:**

```bash
# Merge three PDF files
sst.pdf-merge --input document1.pdf document2.pdf document3.pdf --output combined.pdf
```

## Adding New Tools

To add a new tool to the suite:

1. Create a new Python module in the `sst/` directory (e.g., `sst/my_tool.py`)
2. Implement a `main()` function as the entry point
3. Add an entry in `pyproject.toml` under `[project.scripts]`:
   ```toml
   "sst.my-tool" = "sst.my_tool:main"
   ```
4. Reinstall the package to register the new command

## License

This project is open source.