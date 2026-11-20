# MAT-09 · WORK PLAN — Mathematics (041)
*Written 2026-11-20 at the staff meeting she called, with her decisions of that afternoon. CLAUDE.md §12 holds the order; this file holds the plan and its arithmetic. It replaces nothing in the truth rules.*

## §1 · The order (her decision 2026-11-20)
1. **The Physics close comes first**, on the Physics repositories with their own CLAUDE.md: opening fixes, pattern sorting, derive, year checks, year-closes. It is not this repository's work; this repository starts when she opens it.
2. **Batch 0** (`Batch 0.`): the setup with `--init` (it also puts the rule card and an empty addendum into the new vault's `notes/`), the seed (`pyqkit seed` from `MAT-05` and `MAT-06`), inventory, the syllabus check against the official PDF, and the 2026-27 sample paper with its scheme through the full pipeline (its rows are year 2027, exam SQP, as in Physics). The year planner plans board papers only, so after the sample paper's S1 identity commit open its lines yourself, one `G checkpoint --message "B0 planned" --open-line "<text>"` each, chained in one Bash call: `B0 S2a constants of the 2026-27 sample paper`, `B0 S3 SQP2627-041 ledger with its BLUEPRINTS row`, `B0 S5 SQP2627-041 scheme`, `B0 YC year check of the sample paper's rows (Y§11, year 2027)`, `B0 S6 classify the sample paper's rows: the project's first codes (MAT-10 and its note)`. Commit S2a as `S2A-SQP2627` with `--progress "B0 S2a"`, S3 and S5 by the paper id (S5 with `--progress "B0 S5"`), and tick the other two with `--tick "B0 YC"` and `--tick "B0 S6 classify"`. Only the S3 and S5 lines name the paper id, because a commit leaves a line open while any paper id on it is not done (rehearsed on 2026-11-20). Last, tick the kit's own first line, `G checkpoint --message "Batch 0 done" --tick "Batch 0:"`, so the next `Go` starts Maths 2026 instead of Batch 0 again.
3. **Then the years, newest first, alternating subjects in her order:** Chemistry 2026 → Maths 2026 → Chemistry 2025 → Maths 2025 → Chemistry 2024 → Maths 2024 → 2023 → 2022 (Term 1 and Term 2) → older years as far back as she has papers. Each year includes its compartment and visually-impaired papers.
4. **A year closes before the next Maths year opens:** S1 intake → S2 blueprint → S3 and S4 papers → S5 schemes → the year check (`MAT-08` Y§11) → **S6 patterns for that year (`MAT-10`)** → S7 derive → S8 year-close. Patterns are never left for the end (the Physics project owed about 10–12 closing sessions because it did that).
5. When a Maths year closes, the report's next-step line names the Chemistry year that comes next, in `CHEMISTRY-MINING-INSTRUCTIONS`.

## §2 · The arithmetic (from her records, November 2026; the kit's PROGRESS counts replace it as soon as there are real ones)
- A mining session runs a little over an hour and uses about 15% of a Pro week: about 6.7 sessions a week.
- With the lean method, a year's papers and schemes take about 5 sessions; patterns and the close about 2 more: about 7 per closed year. The first year costs most (Physics 2026 took about 15), so budget for it.
- From about 1 Dec 2026 to 31 Jan 2027 that is about 59 sessions shared by both subjects. Their papers: Chemistry on 27 Feb, Maths on 9 Mar.
- If the first year runs long, the dates move and the order doesn't; the report says so plainly, with the numbers.

## §3 · What she supplies (once per year; nothing to rename)
- The year's question papers (ZIP or PDFs) and marking schemes, in repositories she creates, as she did for Physics. The setup finds every repository by content.
- Once, before Batch 0, in this repository: the official 2026-27 syllabus PDF and the 2026-27 sample paper with its marking scheme.

## §4 · Packs for her classes
- Whenever she types `Pack: maths ch <n>.`, build that chapter's pack from the vault as it stands (`MAT-11`). Packs never wait for a year to close and never invent a question.
