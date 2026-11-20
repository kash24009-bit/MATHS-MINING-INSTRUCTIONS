# Port progress · Mathematics (041), from the Physics (042) instructions

Each step is committed and pushed when it is done, so a usage stop loses nothing. A new session continues from the first open line.

- [x] 1. Tools ported and tested: `pyqkit.py` (subject blocks: question types, step kinds, registers R01–R08, mock section types, blueprint class), `mat_code_env.py` (Batch 0 `--init`, refused when any vault exists), `mat_gate.py`, `mat_marks.py`, `mat_s6.py`. All compile; a fresh vault passes validate 16/16; the setup with `--init` starts a vault at batch 0, and without it stops as before.
- [x] 2. Instruction documents: subject content in CLAUDE.md (Batch 0, her work order, packs), MAT-00, MAT-02 (notation, figures, blueprint classes, registers), RULE-CARD (section B-MAT: this subject's reading rules) and the reader agent. MAT-07, MAT-08 and MAT-10 keep every Physics procedure and lesson, with a note that their examples are Physics history.
- [x] 3. MAT-03 mistakes ledger: every lesson carried from Physics, marked as carried history.
- [x] 4. MAT-05 syllabus: 55 rows, RECALLED from the rationalised syllabus (the official 2026-27 PDF could not be read from here); Batch 0 verifies every row.
- [x] 5. MAT-06 pattern seed: 89 DRAFT patterns, each with a plain name, an "asks you to" line and a scoring skeleton; a fresh vault seeds them and validates 16/16.
- [ ] 6. MAT-09 work plan, MAT-11 teaching handoff, README.
- [ ] 7. Final checks, then the pull request.
