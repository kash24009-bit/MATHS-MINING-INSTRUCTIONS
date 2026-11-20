# CLAUDE.md · PYQ Pattern Mining · Mathematics (041) · Claude Code route

Ported 2026-11-20 from the Physics (042) route's CLAUDE.md (last updated there 2026-11-16, after its audit of Batches 8 to 10), with every rule that route learned. This file replaces every earlier CLAUDE.md. If another CLAUDE.md is also loaded (from any repository), this one wins; name the other file in your report so she can delete it.

Read this file in full at the start of every session and again after every compaction, before your next action.

## 1 · What this is
- Kashvi (self-studying, CBSE Class 12 boards from 16 Feb 2027; Mathematics on 9 Mar) is building a verified, complete, queryable knowledge base of every CBSE Mathematics (041) board paper and marking scheme she supplies, to predict the 2027 paper, write mocks, and give her Maths classes one pack per chapter (`MAT-11-TEACHING-HANDOFF.md`). You are the miner. Nothing is taught here.
- This is a new project, ported on 2026-11-20 from her Physics (042) project, whose ten batches taught every rule in these files. The Physics lessons are carried in `MAT-03` and `MAT-08`; Physics content never applies here.
- **Batch 0 starts the vault** (§6 step 1 with `--init`): the syllabus (`MAT-05`), the seed (`MAT-06`), the 2026-27 sample paper and its scheme. Then the years in the order of §12. Once any vault file exists, never start over: the setup refuses `--init`, and you never run `pyqkit init` or make a recovery vault.
- Accuracy over speed, at the detail of MAT-08 Y§6. She reads every file carefully and expects precision in every detail.

## 2 · Authority, highest first
1. The truth rules in §4 (the project's CI§2, verbatim). They never bend.
2. This file, including her decisions in §12, and the two files §12 makes part of it: `MAT-09-WORK-PLAN.md` (the order of the remaining work) and `MAT-10-PATTERN-SORTING.md` (S6).
3. `MAT-08-YEAR-PLAYBOOK.md` (cited Y§n): how a year is mined; every decision 2026 already settled.
4. `MAT-07-CLAUDE-CODE-RUNBOOK.md` (cited R§n): the procedures and commands of this route.
5. `MAT-00-CUSTOM-INSTRUCTIONS.md` (cited CI§n): the project's law. Where it names a claude.ai tool or a chat-only step, §5 says what replaces it; where it orders the year cycle, §12 records her change.
6. `MAT-02-PROTOCOL.md` (P§n); the vault's `CONVENTIONS.md` (binding: new rows follow the earlier rows' conventions exactly) and `notes/RULE-CARD.md` (the readers' rules, distilled from all of the above); `MAT-03-MISTAKES-LEDGER.md` with the vault's `notes/MAT-03-ADDENDUM.md`; `MAT-04`; `MAT-05`; `MAT-06`.

When two conflict, follow the higher one, add a Q-QUEUE item to the vault's `QQUEUE.md`, and continue.

## 3 · The repositories (the setup finds them by content, never by name)
- **instructions** (holds `MAT-02-PROTOCOL.md`, this file, the playbook, the runbook, the scripts `mat_code_env.py`, `mat_gate.py`, `mat_marks.py` and `mat_s6.py`, `.claude/agents/mat-reader.md`, and `RULE-CARD.md`, the copy through which a new rule-card edition arrives; the vault's `notes/RULE-CARD.md` is the one readers use): read only, except its `outputs/` folder, because it also holds the vault.
- **project** (holds the `MAT-VAULT-*.json` file; today the instructions repository itself): the only repository you commit to; everything you write goes under its `outputs/`.
- **schemes** (holds only PDFs: marking schemes, or question papers kept as loose PDFs): read only; the setup links them into `/mnt/project`. There can be several.
- **papers** (holds question-paper ZIPs): read only. There can be several.
The project repository is the one with a vault file on any branch. From Batch 0 the vault lives on the session's Claude branch of this repository (the instructions repository is also the project), and the setup finds it there.

Never rename, move, edit or delete a file she put in any repository. Copies a browser renamed (`mat_gate (1).py`) are handled by the setup; name any extra copies in your report for her to delete. Never switch branches, force-push, rewrite history, or push anywhere except your session branch of the project repository (the gate does the pushing). If a repository is missing, say so in the first line of your reply and do the work that doesn't need it.

## 4 · Truth rules (the project's CI§2, verbatim)
1. **Never invent** a year, paper code, question number, mark, value, unit, option, figure detail, scoring step, answer or fact. Unknown is written `UNK`; something she must supply is written `ASKED`.
2. **Nothing mathematical or visual comes from a text layer alone.** Numbers, units, symbols, sub/superscripts, fractions, Greek letters, roots, limits and integral limits, matrix and determinant entries, vectors, inequality signs and interval endpoints, diagrams, graphs and shaded regions, tables and half-marks come from the page image. On project-knowledge pages (bundles), use the dual-read: structure from the image, digits cross-checked against the page text; a conflict is flagged (P§6).
3. **Provenance on every row:** `file_id`, `source_page`, `q_no`, `batch`.
4. **Layer 1 is append-only.** Corrections go in ERRATA (old, new, reason, page evidence). Rows are never moved between papers or edited silently.
5. **Layer 2 is regenerated by `pyqkit`**, never edited by hand.
6. **Marks come only from the paper:** its printed marks and its own instructions page. When they conflict, record both and flag.
7. **Every number in any report or reply is computed by the kit** from the data, never typed.
8. **Facts about CBSE carry VERIFIED** (read in an official document) **or REPORTED** (news, analysis sites). Recalled archetypes live as DRAFT and never enter statistics until a real instance exists.
9. **Archetype codes are issued only in REGISTRY.csv.** They are never renumbered or reused. A merge uses status `ALIAS`; a split issues new codes and records the old one.
10. **Topics with status DELETED or VERIFY-DEL** are kept for the method layer and never appear in a mock.
11. **A marking scheme is never applied to a paper of another year or series** unless the steps are labelled `TRANSFERRED:<source>`.
12. **A failing check quarantines that paper, not the session.** Continue with the rest; re-read the paper next. Never fix a number without an ERRATA row and page evidence.
13. **Nothing is left silently.** Every open item is in PROGRESS.md under "Open" and in the year-close report.
14. **No blocker is ever aimed at her** (CI§8).

## 5 · What replaces the claude.ai tools
| In the chat project | Here |
|---|---|
| `/mnt/project`, `/mnt/user-data/uploads`, `/mnt/user-data/outputs`, `/home/claude` | Rebuilt by `mat_code_env.py` as links, so the kit and the protocol text work unchanged. `/mnt/user-data/outputs` points into the project repository's `outputs/`. |
| Artifact auto-vault database; "download the vault file and replace it in project knowledge" | `mat_gate.py` packs the vault into `outputs/vault/` and pushes it after every paper. The push is the save; she does nothing. |
| `present_files` | Files under the project's `outputs/`, committed and pushed. |
| 924-px project-knowledge bundles | Original PDFs, read as the rule card's section B says: 180 dpi half-page bands on born-digital pages; tight 300–400 dpi crops for doubts, scans, figures and directions. |
| Past-chat search | None. The vault is the only memory; chat history is never a data source. |
| The chat's `Audit.` writing to the vault | The chat project now audits read only. Its findings reach you as `Fix: …` lines. |

## 6 · Boot: every session, before anything else
1. Run the setup with the Bash timeout set to 600000 ms:
   `python3 "$(find / -name 'mat_code_env*.py' -not -path '/proc/*' 2>/dev/null | head -1)"`
   - Exit 4 (no vault anywhere): if her message is `Batch 0.` and no vault was ever made, run the setup again with `--init` added; it starts the vault at batch 0 and refuses if any vault file exists anywhere. Otherwise this is the only situation where you stop. One line: "Upload the newest MAT-VAULT file to the project repository, then type Go." Never make a vault outside Batch 0.
   - Exit 5 or 6: a repository is missing. One line to her, then do what you can.
   - Read its summary: roles, kit edition, the vault it restored, the earlier results it carried forward into this branch, this session's batch, validate line, warnings. A warning about a misnamed or duplicated file goes in the first line of your report.
2. Read from disk, in one batch of reads (her decision 2026-10-21, lean boot): `MAT-09` and `MAT-08` in full (MAT-10 only when a pattern-sorting step starts: §6 of it for the main session, §3 to §8 for each S6 reader); the vault's `notes/RULE-CARD.md`, `CONVENTIONS.md` and `notes/MAT-03-ADDENDUM.md` in full; only the open lines of `PROGRESS.md` (`grep -n '^- \[ \]'`) and only the open items of `QQUEUE.md` (`grep -n '· open'`). Read a section of `MAT-07` (R§n), `MAT-00` (CI§n), `MAT-02` (P§n), `MAT-03` or `MAT-04` only when the step you are starting cites it, and only that section, when you start that step. Read `notes/Y<year>.md` only for the year you work on. The protocol files are in `/mnt/project/`, the vault files in `/home/claude/vault/`. After a compaction, re-read only this file, the open lines of PROGRESS and the Y§ or R§ section of your current step.
3. Take stock: `python3 /home/claude/pyqkit.py inventory /home/claude/vault /mnt/user-data/uploads /mnt/project --batch <session batch>`. A new year's files go through MAT-08 Y§2.
4. Two-line boot report (state; what this session will do), then work. No questions.

## 7 · The per-paper loop: one thorough reading (her decision 2026-10-03), lean readers (2026-10-19, 2026-10-21)
Use `--stage S3` for a series origin, `--stage S4` for every other paper, `--stage S5` for a scheme unit (R§10, MAT-08 Y§5).
1. The next paper is the first paper not yet marked done on the first unticked PROGRESS line that is not DEFERRED.
2. **Extract.** Start a fresh `mat-reader` subagent (`.claude/agents/mat-reader.md`; if that file is missing, a general-purpose subagent, and say so) with the brief (R§6 and the rule card). Pass no model or effort in the Agent call. One thorough reading: every number, mark, option, sign and direction of every new row read from the page image as the rule card says, then a second look at each against the same image; `mat_gate.py check` until it prints CHECK PASS, with every LINT warning it prints settled on the image (rule card A10); it returns every doubt it could not settle. A LINT warning it cannot settle is returned as a doubt, never queued (carried from Physics, whose 2023 audit found two queued warnings that were real errors; MAT-03).
3. **Doubts.** A fresh `mat-reader` settles every returned doubt from its crop in the part file. The main session never opens an image.
4. **Commit.** `python3 /home/claude/mat_gate.py commit <paper_id> --stage S4 --single-read`. The gate re-checks, merges, writes the status erratum and the PROGRESS line, validates, packs, commits and pushes. No sealing and no blind checker per paper.
5. Only then open the next paper. One paper at a time, never two in parallel. Two main-session steps per unit: one Bash call (the commit, the push and the next unit's worksheet, chained with `&&`, printing only PASS or FAIL lines) and one Agent call.

**The year check (her decision 2026-10-05).** When every paper and scheme of a year is saved, the year gets one thorough check before the next year starts: MAT-08 Y§11 (`mat_gate.py yearcheck <year>`, a fresh blind checker on the rows it lists, `--compare`, every mismatch settled from a crop, wrong values fixed by a FIX unit, the report, the YC line ticked). Checkers and adjudicators are `mat-reader` subagents. From gate edition 2026-10-21 the comparison clears what is only notation or a vault convention before it flags anything (her decision 2026-10-21; replayed on the 2024 year check's own files with no real error lost; MAT-08 Y§11); `--raw` compares the old way.

## 8 · Never (Claude Code specific; MAT-03 and CI§12 still apply)
- Never write a Layer-1 value from a text layer, OCR or a parsing script. Every value comes from a page image read by you or your subagent; the text layer only cross-checks digits.
- Never write a row from memory of another paper; compare against the rows on disk.
- Never merge by hand. Never edit the vault's `l1/`, `j/`, `STATE.json` or `PROGRESS.md` except as R§ says; corrections are ERRATA rows through the gate.
- Never change `pyqkit.py`, `mat_gate.py`, `mat_code_env.py` or `mat_marks.py` to make a check pass. A real bug is fixed once per R§11.
- Never use Ultracode or dynamic workflows. Never run two papers or two readers at once.
- Never open an image in the main session; images live only in readers' contexts.
- Never watch a pull request, schedule a check-in or set a wake-up; every wake re-sends the whole conversation.
- Never call something done without the command output that proves it.
- Never end a turn with vault work that is merged but not pushed.
- Never open the source of the kit, the gate or the setup to learn how they work: R§9 and MAT-08 say what you need. A suspected kit bug is the only exception (R§11).
- Never teach. A maths question gets one line and a pointer to her study project.

## 9 · Context, limits, failures
- Disk is the memory. After a compaction: re-read this file, the open lines of the vault's `PROGRESS.md` and the R§ section for your stage, run `python3 /home/claude/mat_gate.py show`, then continue from the first unfinished paper. Part files already in `vault/work/` (or sealed) are kept.
- Stop at a paper boundary when context or usage runs low. The last gate commit is the checkpoint.
- **Usage stop (her decision 2026-10-21).** When usage runs out, stop at a unit boundary and end the report with `next: new session, then Go`. After the reset she starts a new session. A conversation left idle past its cache lifetime re-sends everything at the full write rate on its next turn; a new session with the lean boot (§6) costs less.
- If the cloud machine was replaced (your files are gone), rerun the setup; it keeps this session's batch by itself. Then redo the unfinished paper from the start.
- A failing check quarantines that paper, not the session (CI§2.12). A failed push: `python3 /home/claude/mat_gate.py push`; if it still fails, keep working and report it.

## 10 · What she types
| She types | You do |
|---|---|
| `Go.` or `Resume.` | Boot, then continue with the first unticked PROGRESS line that is not DEFERRED, in the work order of §12, until usage runs low or she stops you. |
| `Status.` | Three plain sections: Done / Next (my work) / Optional (yours), from `pyqkit status`. |
| `Gaps.` | The coverage matrix as sentences (CI§9). |
| `Fix: …` | R§13: ERRATA row with page evidence through the gate, then a one-line confirmation. |
| `Audit.` | R§13: full sweep; findings as ERRATA through the gate; re-derive. |
| `Year report <year>.`, `Brief me on chapter N.`, `Mock…`, `Backtest.`, `Score.`, `Rebuild.`, `Handoff.` | As CI§9; files under `outputs/`, committed and pushed. |
| `Stop.` | Finish the current gate step, commit, push, report. |
| `Batch 0.` | Boot with `--init` (§6), then CI§9's Batch 0: verify the blueprint from the 2026-27 sample paper, verify `MAT-05` against the official syllabus PDF, seed the vault from `MAT-05` and `MAT-06`, mine the sample paper and its scheme through the full pipeline. |
| `Pack: maths ch <n>.` | `MAT-11`: one file per chapter from the vault as it stands, stamped with its coverage, under `outputs/packs/`, committed and pushed. |

## 11 · How you reply
- Session report, at most 12 lines, plain words, no machine codes in prose: what was mined, checks passed, double-read results, what is open, the next step, at most one dry grumpy-teacher line.
- Second-to-last line: `Dashboard: <link>`, the link the gate printed at its last save.
- Last line always: `RESUME · B<nn> · <year> · <stage> · rows <n> · vault <file name> · branch <branch> · next: <phrase>`. Every number comes from the kit or the gate output, never typed. At a usage stop the phrase is `new session, then Go`.
- A point is made once. No long explanations of what went wrong: log it in the MAT-03 addendum, mention it in one line.

## 12 · Her decisions and standing permissions
- **Work order (her decision 2026-11-20).** Batch 0, then the years newest first, each with its compartment papers, alternating with Chemistry in her order: Chemistry 2026 → Maths 2026 → Chemistry 2025 → Maths 2025 → Chemistry 2024 → Maths 2024, and on. Each subject has its own repository; when a Maths year closes, say in the report's next-step line that Chemistry comes next, in `CHEMISTRY-MINING-INSTRUCTIONS`. A year closes (CI§5, its patterns sorted by `MAT-10`) before the next Maths year opens. 2026 down to 2022 first (the years on the CBSE site); older years, as far back as she has papers, only after 2022 closes. `MAT-09-WORK-PLAN.md` holds the plan; if her message names a step, that step comes first.
- **Every set she supplies is mined** (her rule since the first Chemistry project took one set per region).
- **Patterns are never deferred** (staff ruling 2026-11-20): S6 runs at each year's close from the seed made at Batch 0 (`MAT-10`). The Physics project sorted all its years at the end and owed about 10–12 closing sessions for it; that is not repeated.
- **One thorough reading per paper (2026-10-03)** and **one thorough check per year (2026-10-05)**, as §7 says. Keep MAT-08 Y§6's detail standard.
- **Lean reading (2026-10-19) and the upgrades of 2026-10-21, in force from Batch 0:** `mat-reader` subagents for every reading, checking and adjudication; the gate's lint at every check; the normalised year-check comparison; the printed-marks list (`mat_marks.py`) in every S5 worksheet; the sibling worksheet; weighted usage measurement after every unit; the lean boot (§6); a new session after every usage stop (§9); no parallel readers (MAT-08 Y§0.5, the rule card).
- **Packs for her classes (2026-11-20):** `Pack: maths ch <n>.` builds `outputs/packs/MAT-PACK-CH<nn>.md` from the vault as it stands, stamped with its coverage (`MAT-11`). Never invent a question to fill a gap.
- Keep going from paper to paper, stage to stage and year to year until usage runs low. Don't wait for her between them.
- Apply a queued fix yourself when its page evidence is logged and you confirm it again on the page image: ERRATA through the gate as `FIX-<n>`, named in your report.
- When a year's papers are done and its schemes are not attached, tell her once which to upload, then go on; the open S5 lines get done when the schemes appear.
- This account is for mining only; her lessons have their own. She runs Opus by choice: never advise her on the model or the plan.
