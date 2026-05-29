# Outline

Semantic project analysis tool.

Outline builds a language-agnostic semantic graph from source code and provides tools for rendering and navigating project architecture.

## Features

* Semantic graph generation
* Recursive scope analysis
* Directory semantic objects
* Modular scanners
* Modular renderers
* Tree renderer
* JSON renderer
* .outlineignore

## Development Setup

```bash
git clone git@github.com:dvd314/outline.git
cd outline
uv pip install -e .
```

Outline is currently in active development.

For convenient global access, you can create a shell alias or function:

```bash
outline() {
    uv run --project ~/projects/outline outline "$@"
}
```

## Usage

Initialize project:

```bash
outline init
```

Build semantic graph:

```bash
outline scan
```

Render graph:

```bash
outline render
```

Render raw graph:

```bash
outline render json
```

## Architecture

```text
Source Code
    ↓
Scanner
    ↓
Semantic Graph
    ↓
Renderer
```

## Roadmap

* Semantic object addresses
* Source extraction
* Inspect
* Search
* Replace
* Additional language scanners
* Additional renderers

## License

GNU GPL v3

