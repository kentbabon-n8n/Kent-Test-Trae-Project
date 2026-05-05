# Project Rules

## 🧩 Skill Evolution Framework (Trae Optimized)
- **Skill-Based Execution**: All complex workflows MUST be defined as skills in `.claude/skills/`.
- **Skill Structure**: Each skill must contain `SKILL.md` (instructions), `scripts/` (tools), and `references/` (deep docs).
- **Trae Tool Integration**: Skills should prefer using Trae's native tools (`SearchCodebase`, `RunCommand`, `Read`, `Write`) over generic shell commands.
- **Progressive Loading**: Always read the `SKILL.md` first, then load specific `references/` or run `scripts/` only when needed to save context.

## 🧹 Lead Generation Rules
- **WAT Framework**: Follow the Workflows, Agents, Tools, and Data structure defined in [Trae.md](file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/Trae.md).
- **Efficiency-First Filtering**: Proactively skip vague leads. Prioritize B2B leads with clear decision-maker associations.
- **Data Integrity**: Sync all changes to GitHub and maintain `.tmp/` data integrity.
