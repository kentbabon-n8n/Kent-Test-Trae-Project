---
name: reflect
description: "Self-correction and optimization engine for Trae. Trigger when: (1) A task fails, (2) User corrects Trae's output, (3) A more efficient way to do something is discovered, (4) User says 'reflect' or 'optimize'."
---

# Reflect (Trae Edition)

This is the meta-cognitive layer of the project. It allows the Trae agent to analyze its own performance, identify bottlenecks, and update project skills/rules autonomously.

## Core Workflow

1. **Failure Analysis**: When a command fails or the user provides a correction, identify the root cause (e.g., outdated rule, missing context, fragile script).
2. **Impact Scan**: Determine which other skills or project rules are affected by this discovery.
3. **Optimization**:
    - Update the relevant `SKILL.md` or `references/`.
    - Refine `.trae/project_rules.md` if the discovery is project-wide.
    - Suggest a new skill if a repetitive pattern is identified.
4. **Verification**: Run a smoke test to ensure the optimization doesn't break existing workflows.

## Rules

- **Don't Over-Optimize**: Only reflect on meaningful failures or repeated friction points.
- **Trace to Source**: Always link the reflection back to a specific user correction or terminal error.
- **Incremental Improvement**: Small, frequent updates are better than massive, infrequent overhauls.

## References

- `file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/.claude/skills/skill-dev/references/reflect-mode.md` — Deep technical details on the reflection process.
