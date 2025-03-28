# Project: Agentic AI Demos

## Overview

This project contains demos to understand **Agentic AI features**. It showcases real-world use cases of AI agents
interacting with environments, making autonomous decisions, and learning over time.

## Installations

1. Install [uv](https://github.com/astral-sh/uv)
2. Install [direnv](https://github.com/direnv/direnv)
3. Install [playwright](https://github.com/microsoft/playwright)

## Setup

### Virtual Environment Setup

```shell
uv venv
source .venv/bin/activate
```

### Install Dependencies

```shell
uv pip sync requirements.lock
```

```shell
playwright install
```

## Running the Project

### 1. [Demo] Add a product to amazon cart

```shell
task run
```

## Contribution

### Add a new dependency

```shell
uv pip install <package-name>
uv pip freeze > requirements.lock
```

### Update Dependencies

```shell
uv pip install --upgrade -r requirements.lock
uv pip freeze > requirements.lock
```

### Format

```shell
task format
```

### Lint

```shell
task lint
```

### List All Tasks

```shell
task --list
```
