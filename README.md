# Project: Agentic AI Demos

## Overview

This project contains demos to understand **Agentic AI features**. It showcases real-world use cases of AI agents
interacting with environments, making autonomous decisions, and learning over time.

## Installations

1. Install [uv](https://github.com/astral-sh/uv)
2. Install [direnv](https://github.com/direnv/direnv)

## Initial Setup

### Virtual Environment Setup

```shell
uv venv
source .venv/bin/activate
```

### Install Dependencies

> Use `requirements.lock` for a reproducible environment.
> Use `requirements.txt` for latest compatible versions.

```shell
uv pip sync requirements.lock
```

### Update Dependencies

```shell
uv pip install --upgrade -r requirements.txt
uv pip freeze > requirements.lock
```

### Add a new dependency

```shell
uv pip install <package-name>
uv pip freeze > requirements.lock
```

### Linting & Formatting

```shell
task lint
```

### Type Checking

```shell
task typecheck
```

### Running Tests

```shell
task test
```

### List All Tasks

```shell
task --list
```


## Running the Project

### 1. [Demo] Add a product to amazon cart

```shell
playwright install
python sample/main.py
```