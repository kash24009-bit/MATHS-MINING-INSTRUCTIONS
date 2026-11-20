# Port progress · Mathematics (041), from the Physics (042) instructions

Each step is committed and pushed when it is done, so a usage stop loses nothing. A new session continues from the first open line.

- [x] 1. Tools ported and tested: `pyqkit.py` (subject blocks: question types, step kinds, registers R01–R08, mock section types, blueprint class), `mat_code_env.py` (Batch 0 `--init`, refused when any vault exists), `mat_gate.py`, `mat_marks.py`, `mat_s6.py`. All compile; a fresh vault passes validate 16/16; the setup with `--init` starts a vault at batch 0, and without it stops as before.
- [ ] 2. Instruction documents: subject content in CLAUDE.md, MAT-00, MAT-02, MAT-04, MAT-07, MAT-08, MAT-10, RULE-CARD and the reader agent.
- [ ] 3. MAT-03 mistakes ledger: every lesson carried from Physics, marked as carried.
- [ ] 4. MAT-05 syllabus from the official 2026-27 syllabus.
- [ ] 5. MAT-06 draft pattern seed; the kit seeds and validates it.
- [ ] 6. MAT-09 work plan, MAT-11 teaching handoff, README.
- [ ] 7. Final checks, then the pull request.
