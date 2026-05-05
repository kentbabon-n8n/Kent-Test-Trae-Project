---
name: python-project-creator
description: "Scaffolds new Python projects or tool components. Trigger when user wants to: (1) Start a new Python script, (2) Create a structured tool directory, (3) Initialize a Python-based skill."
---

# Python Project Creator (Trae Edition)

This skill automates the creation of structured, stdlib-first Python projects and components within the Trae environment.

## Core Workflow

1. **Scaffold**: Create the base directory and standard subdirectories (`scripts/`, `tests/`).
2. **Initialize**: Create a main entry point script with a standard template (argparse, logging, stdlib only).
3. **Skill Integration**: If requested, wrap the Python project as a Trae skill by adding a `SKILL.md` file.

## Rules

- **Stdlib Only**: Favor Python standard library over external dependencies to ensure portability within the AI agent's environment.
- **Agent-First Design**: Scripts should output structured data and use greppable error formats.
- **Absolute Paths**: Always use or accept absolute paths for robustness.

## Scripts

- `scripts/scaffold.py` — The core automation script for creating the project structure.
