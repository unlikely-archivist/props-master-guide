# Instructions for Claude

This repo is a **props master guide** for university teaching and a possible textbook. It's one consolidated guide (`guide/` chapters in part folders plus `appendices/`) built from several books. **The goal is a master reference that stands in for reading every source**: someone who reads it should know what all the books teach, and be able to look up any part of the job and find the reference information, methods, safety and projects in one place. Each book has a citation code and page references. The user's usual request is "here's my next source, add it to the guide". Follow this file end to end without asking for setup details.

## Hard rules

- **Never write slurs**, even when quoting, flagging or repeating a source. Describe them instead (e.g., "an ethnic slur on p. 165").
- **Never write a standalone guide.** Every new source goes *into* the existing chapters. **Weave it in by topic**: a new book's adhesive advice goes in ch. 25, its safety points in ch. 20, its material methods in the Part 5 chapter for that material. Don't give a book its own chapter just because it's a new book. Add a new chapter only for a subject the guide doesn't cover yet.
- **When sources disagree, state each position with its citation and stop.** For example: "FF says X (FF 38); Hart says the opposite (H 267)." Don't pick a winner, recommend one side, or add advice that resolves it. This includes a source disagreeing with itself ("FF gives both 50 s (FF 73) and 90 s (FF 77)").
- **Write in your own words.** Summarise and reorganise. No long quotations, no reproduced images, tables or forms. Brief quotes need a page citation.

## Step 0: get the real guide before doing anything

The session's clone may start **empty** or on a branch without the guide. That caused a whole wasted pass once.
1. `git fetch origin` and `git branch -r`. Find the default branch with `git ls-remote --symref origin HEAD` (or `git remote show origin | grep "HEAD branch"`). As of Nov 2026 it is `claude/eloquent-cray-cbyf6u`.
2. Base your working branch (the one the session tells you to use) on `origin/<default branch>`. If your branch already exists with unrelated history, merge the default branch in.
3. Read `README.md`, `STATUS.md` and `appendices/C-sources-and-editions.md` before writing.

## Step 1: read the source

- Uploaded PDFs are often large OCR scans. Extract the text with `pdftotext` (with and without `-layout`), then read **all** of it. Don't skim.
- Ingredient boxes, tables and captions are often missing from the text layer. Render those pages (`pdftoppm -r 160 -png`) and read the images.
- **Work out the page offset** between PDF pages and the book's printed pages, and cite printed pages. Record the offset in Appendix C.
- If the file is truncated or garbled, say so in STATUS.md. Don't guess at numbers you can't read; describe the gap instead.

## Step 2: check the edition

Web-search for the book's current edition and any sequels or companion volumes. Record the edition you used, the current edition, ISBNs and the source URLs. Mark facts you checked **[Verified YYYY]**.

## Step 3: integrate

**Citation code.** Choose a short new code that isn't already taken. Existing codes:

| Code | Source |
|---|---|
| M | Mussman 2008 |
| H | Hart, *Prop Building Guidebook*, 1st ed. 2013 |
| HE | Hart, *Prop Effects Guidebook* (truncated, not yet used) |
| J | James 1992 |
| FF | Harrison & Honesty, *Fake Food Cookbook*, 2018 |
| KF | Quindt (Kamui Cosplay), *The Book of Foam Props*, 2019 |
| B | Berls, *Teaching Practical Theatrical 3D Printing*, 2024 |

Cite as `(CODE page)` or `(CODE page–page)`. Add the source's page ranges to section headings, e.g. `## Release agents (H 265–267)`.

**Structure.** Chapters live in part folders. Chapters 1–53 are numbered continuously; any new chapter takes the next free number (54+) inside the right part folder, so existing links never change:

| Folder | Part | Chapters |
|---|---|---|
| `guide/1-intro/` | Intro: what a prop and a prop master are, media, theory, history | 1–5 |
| `guide/2-admin/` | Admin: script breakdown, research, budgets, staffing, departments, buy/source/build, rehearsals, strike, rules to live by | 6–14 |
| `guide/3-sourcing/` | Shopping, renting, borrowing, altering, reusing | 15–19 |
| `guide/4-fabrication-core/` | Safety, tools, build method, drawing, patterning, glues, structure, surfaces, paint | 20–28 |
| `guide/5-materials/` | One chapter per medium (wood, metal, plastics, foams, EVA, fabric, leather, shells, sculpting, casting, paper, 3D printing, prop food) | 29–41 |
| `guide/6-weapons/` | Safety and policy, firearms, blades, other weapons and armour | 42–45 |
| `guide/7-effects/` | Breakaways, eating/drinking/smoking, flame/smoke/sound, practicals and mechanisms, blood | 46–50 |
| `guide/8-wider-craft/` | Set dressing, greens and florals, careers | 51–53 |

**Fold it in, don't add it on.** The test of a good integration: a reader of any chapter can't tell which book arrived last. Work in this order.

1. **Make a topic map first** (in your scratchpad, not the repo). For every section of the new book, write: what it teaches → the guide chapter and section it belongs in (use the routing table below) → whether it **agrees with**, **adds to**, or **disagrees with** what's already there, or **fills a [General knowledge] gap**. Only after the map is complete, start editing.
2. **Agrees** → don't repeat it. Add the new citation to the existing sentence, e.g. "(H 66; NEW 12)". Add any extra detail (a number, a tip, an example) into that same bullet or table row.
3. **Adds to** → put it inside the existing section: a new bullet in the list, a new row or column in the table, a new step in the procedure. Re-order or re-head the section if needed so it reads as one synthesis. Don't create "What NEW says" blocks; attribute through citations, not separate paragraphs. A distinctive named method can be introduced by name ("Quindt's magnet joint…") within the flow.
4. **Disagrees** → state both positions neutrally inline where it matters, and add a row to that chapter's `## Where the sources disagree` table (`Topic | <new> says | Other source says`; create the table if the chapter has none, placed before Key terms). See Hard rules.
5. **Fills a gap** → where a section or line is marked **[General knowledge]** and the new book covers it, rewrite it from the source with citations and remove the marker. Keep general-knowledge lines that the source doesn't cover, still marked.
6. **Tutorials, recipes, worked builds** → add them to the matching companion file beside the material chapter (`NN-…-projects.md` or `NN-…-recipes.md`; every Part 5 chapter and chs. 27–28 already has one). Fold steps into an existing project when it's the same build; otherwise add a new numbered project. Add or update rows in [Appendix F](appendices/F-i-need-to-make.md) for any prop type the book teaches you to make.
7. **Genuinely new subjects only** → if no chapter covers a subject, first try a new section in the closest chapter. Only if it's a whole new area, add a chapter in the right part folder with the **next free number (54, 55…)**, so existing numbers and links don't change, and add it to the README contents under its part.
8. **Update `> **Sources:**` lines** of every chapter you contributed to substantively.
9. **Self-check before Step 4:** `grep -c "(CODE " guide -r` should show the new code spread across many chapters, not concentrated in one. Re-read each touched section once to make sure it flows as a single text.

**Routing table: where does it go?**

| The book covers… | Goes in |
|---|---|
| Definitions, categories, the job, film/TV differences, theory, history | chs. 1–5 |
| Script breakdown, research, budgets, scheduling, staffing, departments, rehearsals, strike, storage | chs. 6–13 (and rules worth quoting → ch. 14) |
| Shopping, rental, borrowing, alteration, reuse | chs. 15–19 |
| Safety, PPE, ventilation, chemicals | ch. 20 (plus a short pointer in the material chapter) |
| Tools and shop setup | ch. 21 |
| Design process, drawings, patterns | chs. 22–24 |
| Glues, fasteners, tapes | ch. 25 |
| Structure, armatures | ch. 26 |
| Fillers, texture, distressing, coatings, flame-proofing | ch. 27 (+ recipes file) |
| Paint, dye, faux finishes, stain | ch. 28 (+ recipes file) |
| A specific material (wood, metal, plastics, foams, EVA, fabric, leather, shells, sculpting, casting, paper, 3D printing, food) | its Part 5 chapter, chs. 29–41 (+ projects file) |
| Weapons, stage combat, firearms, armour | chs. 42–45 |
| Breakaways, food/drink/smoking onstage, flame/smoke/sound, practicals/electrics/mechanisms, blood | chs. 46–50 |
| Set dressing, greens, careers | chs. 51–53 |
| Dates and period objects | ch. 7 and Appendix E |

**Chapter format** (copy any existing chapter, e.g. `guide/5-materials/41-prop-food.md`):
```
# NN. Title

> **Sources:** CODE ch.X (pp. a–b); ...
> **Companion:** (if there's a projects or recipes file)
> **[Check current]** what in this chapter dates quickly

...sections with page cites in headings...

## Key terms
term · term · term

## For the classroom
- **Bold title.** A discussion or hands-on prompt (aim for 4–6).
```

**Markers**
- **[Check current]**: volatile facts (products, prices, law, regulations, technology, URLs). Also add each one to the volatile-information register in Appendix C.
- **[Verified YYYY]**: facts you checked by web search. List the URLs in Appendix C.
- **[Added best practice]** / **[Suggestion]**: points that aren't in any source. Never use these to settle a disagreement.
- **[General knowledge]**: sections written from widely available knowledge to fill a gap no source covers yet. Mark it at the section or line level. Never use it to settle a disagreement between sources.

**Style.** Plain, direct teaching prose. Bullets and tables for procedures and numbers. Keep the source's numbers (ratios, temperatures, times) with page cites. Use US units if the source does.

## Step 4: update every shared file (checklist)

- [ ] **README.md:** the source count ("brings N books together"), the chapter list (only if you added a chapter), the appendix list, the citation-key table row (with edition notes), the example citation line, and the status line.
- [ ] **appendices/C-sources-and-editions.md:** a core-sources table row (edition used, current edition, ISBNs, page offset, scan quality, which chapters use it), verification-source URLs, and rows in the volatile-information register.
- [ ] **appendices/D-concordance.md:** the code in the intro paragraph; add the code's pages to the "Other sources" column of each chapter row it contributes to (and a row for any new chapter); and a new `## <Author> (CODE) by subject` table (Subject | pages | related guide chapters).
- [ ] **Companion files and finder:** tutorials and recipes in the matching projects/recipes files; new rows in Appendix F.
- [ ] **[General knowledge] markers:** removed wherever the new source now covers the content; STATUS item 1 updated to match.
- [ ] **appendices/A-glossary.md:** new terms in **alphabetical order**, formatted `**Term** — definition. (ch. N)`. Extend existing entries rather than duplicating them.
- [ ] **STATUS.md:** under Done, what was added. Under Blocked/open, any OCR gaps, truncation or unverified facts. Update "Last updated". STATUS is handoff context; stable facts belong in the README and Appendix C.
- [ ] **Cross-references:** add one- or two-line pointers from related existing chapters to the new material.

## Step 5: verify, merge, report

1. Run `python3 tools/check_links.py`. It must report 0 broken links. Anchors use GitHub slugs: lowercase, punctuation dropped (en dashes too), spaces become hyphens.
2. Commit with a descriptive message and push your working branch.
3. **Merge everything into the default branch.** Fast-forward or merge your branch into `origin/<default>` and push. Then check `git branch -r`: every `claude/*` branch with work should be merged into the default branch, and the default branch should be up to date.
4. Report back briefly: how the book was folded in (which chapters and companion files it touched, and which [General knowledge] sections it replaced), the disagreements found (stated neutrally), OCR or truncation gaps, the edition-check result, and anything left open.
