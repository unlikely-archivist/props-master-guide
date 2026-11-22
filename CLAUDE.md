# Instructions for Claude

This repo is a **props master guide** for university teaching and a possible textbook. It's one consolidated guide (`guide/` chapters in part folders plus `appendices/`) built from several books. **The goal is a master reference that stands in for reading every source**: someone who reads it should know what all the books teach, and be able to look up any part of the job and find the reference information, methods, safety and projects in one place. Each book has a citation code and page references. The user's usual request is "here's my next source, add it to the guide". Follow this file end to end without asking for setup details.

## Hard rules

- **Never write slurs**, even when quoting, flagging or repeating a source. Describe them instead (e.g., "an ethnic slur on p. 165").
- **Never write a standalone guide.** Every new source goes *into* the existing chapters. **Weave it in by topic**: a new book's adhesive advice goes in ch. 25, its safety points in ch. 20, its material methods in the Part 5 chapter for that material. Don't give a book its own chapter just because it's a new book. Add a new chapter only for a subject the guide doesn't cover yet.
- **When sources disagree, state each position with its citation and stop.** For example: "FF says X (FF 38); Hart says the opposite (H 267)." Don't pick a winner, recommend one side, or add advice that resolves it. This includes a source disagreeing with itself ("FF gives both 50 s (FF 73) and 90 s (FF 77)").
- **Write in your own words.** Summarise and reorganise. No long quotations, no reproduced images, tables or forms. Brief quotes need a page citation.

## Step 0: get the real guide before doing anything

The session's clone may start **empty** or on a branch without the guide. That caused a whole wasted pass once.
1. `git fetch origin` and `git branch -r`. Find the default branch with `git remote show origin | grep "HEAD branch"`.
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

**Structure.** Chapters live in part folders, numbered continuously across the guide:

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

**Where the material goes**
- **Topics that existing chapters already cover:** add passages there, citing the new code, so each chapter reads as one synthesis rather than a list of book summaries. Add the code to that chapter's `> **Sources:**` line if it's a substantial contribution. Where a chapter section is marked **[General knowledge]**, replace or support it with the sourced material and remove the marker where the source now covers it.
- **Subjects the guide doesn't cover yet:** add a new chapter `guide/<part folder>/NN-slug.md` in the right part. Inserting a chapter means renumbering later chapters and every reference to them; prefer adding to an existing chapter, or append at the end of a part only if the numbers allow. If a source has project tutorials or reference-style detail (recipes, build walkthroughs, project briefs, catalogues), put them in a companion file beside the material chapter (`NN-slug-projects.md` or `NN-slug-recipes.md`) and link it from the chapter's `> **Companion:**` line. Use appendices only for guide-wide reference (glossary, templates, sources, concordance, timeline).
- **Disagreements:** collect them in a `## Where the sources disagree` table (`Topic | <new> says | Other source says`) and repeat them inline where they matter. Use neutral wording only (see Hard rules).

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

- [ ] **README.md:** the source count ("brings N books together"), the Part and chapter list, the appendix list, the citation-key table row (with edition notes), the example citation line, and the status line.
- [ ] **appendices/C-sources-and-editions.md:** a core-sources table row (edition used, current edition, ISBNs, page offset, scan quality, which chapters use it), verification-source URLs, and rows in the volatile-information register.
- [ ] **appendices/D-concordance.md:** the code in the intro paragraph, a row in "By guide chapter" for any new chapter or appendix, and a new `## <Author> (CODE) by subject` table (Subject | pages | related chapters).
- [ ] **appendices/A-glossary.md:** new terms in **alphabetical order**, formatted `**Term** — definition. (ch. N)`. Extend existing entries rather than duplicating them.
- [ ] **STATUS.md:** under Done, what was added. Under Blocked/open, any OCR gaps, truncation or unverified facts. Update "Last updated". STATUS is handoff context; stable facts belong in the README and Appendix C.
- [ ] **Cross-references:** add one- or two-line pointers from related existing chapters to the new material.

## Step 5: verify, merge, report

1. Run `python3 tools/check_links.py`. It must report 0 broken links. Anchors use GitHub slugs: lowercase, punctuation dropped (en dashes too), spaces become hyphens.
2. Commit with a descriptive message and push your working branch.
3. **Merge everything into the default branch.** Fast-forward or merge your branch into `origin/<default>` and push. Then check `git branch -r`: every `claude/*` branch with work should be merged into the default branch, and the default branch should be up to date.
4. Report back briefly: what was added and where, the disagreements found (stated neutrally), OCR or truncation gaps, the edition-check result, and anything left open.
