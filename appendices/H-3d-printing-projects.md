# Appendix H: 3D Printing Project Briefs and Troubleshooting

Condensed notes on the projects and fault-finding advice in **B**: Robert C. Berls, *Teaching Practical Theatrical 3D Printing: Creating Props for Production* (Routledge/Focal Press, 2024). Headings carry B's printed page ranges. The technology, teaching method, safety notes and source disagreements behind these briefs are in [ch. 30](../guide/30-3d-printing.md). Read that chapter first.

> **[Check current]** B's briefs name Tinkercad, Meshmixer (no longer developed), Fusion 360 (now Autodesk Fusion), a Thingiverse design number and Tinkercad's featured collections. B's publisher hosts editable files for every object in the book (routledge.com/9781032453279). Software features, file locations and links may have changed.

These are summaries in the guide's own words. They give each brief's **specification**, **assessment criteria**, **typical faults** and **extensions**. B's full prompts and rubric wording are in the book. Students should get your own adapted version.

**Shared format for every brief** (B 34 and each project):
- The student submits the print and the **.stl file** (B asks for under 1 MB, named with the student's preferred name, on a flash drive) by a due date.
- Each criterion is scored **4 successful / 3 needs focus on one area / 2 needs focus on two areas / 1 retry with improvement plan**.
- An **average of 2.5 or above** is satisfactory. Students may redo a project to raise their score.
- Close with a **debrief**: what went well, what needs improvement, what you learned, what you'd change about your process (B 38, 55).

## At a glance

| Brief | Level | Criteria assessed | Group? | Main new skill |
|---|---|---|---|---|
| [Lettered card](#level-1-lettered-card-b-3347) | 1 | Manipulation, alignment, manifold, print | No | Primitives, text, recessed shapes, .stl export |
| [Candlestick phone](#level-2-candlestick-phone-b-4859) | 2 | Analysis, manipulation, alignment, arrangement, manifold, print | Optional | Adapting a downloaded design to a show |
| [Scanned button](#level-3-scanned-button-b-6069) | 3 | Manipulation, scan, manifold, print | Optional | 3D scanning |
| [Prosthesis or mask](#level-4-makeup-prosthesis-or-mask-b-7080) | 4 | Manipulation, scan, manifold, print | Optional | Flexible filament, digital sculpting |
| [Linear actuator](#linear-actuator-b-8189) | — | Manipulation, actuator function, use, print | No | Gears, motors, circuits |
| [Large print](#large-print-group-project-b-90101) | — | Manipulation, team process, manifold, print, final fit, finish | **Yes** (2+) | Splitting and joining |
| [Further projects](#further-project-ideas-b-102116) | — | Varies (see each) | Some | Design, research, shop tools |

## Level 1: Lettered card (B 33–47)

**Specification.** A 40 × 80 × 1 mm card. The student's preferred name in **raised letters 6–8 mm tall**, readable by eye. One symbol from the shape library **recessed 0.3 mm** below the top face. Manifold (B 33, 37).

**Tools.** Tinkercad's box tool (type 40, 80 and 1 mm, or drag the handles), text tool and shape library. Turn the symbol into a "hole" to recess it. Export everything with nothing selected (B 38, 43). B suggests setting up a Tinkercad classroom to follow progress (B 35).

**Objectives.** Learn the interface; resize a primitive; add or cut text; produce one printable .stl (B 35).

**Criteria** (B 34, 36):
- **Manipulation**: shapes and letters at the specified sizes.
- **Alignment**: text lines up and touches the card.
- **Manifold**: no holes in the skin, or only ones the slicer can repair.
- **Print**: prints cleanly and survives handling.

**Typical faults.**
- Text and symbol floating above the card, which prints as "spaghetti" (B 43).
- A symbol that only touches the surface, so it doesn't print recessed (B 43).
- Letters too tall, so they break off (B 43).
- Corners lifting; the nozzle knocking letters loose; low infill letting the skin droop (B 47).

**Extensions.** Use an open prompt for confident students. Turn the card into a custom stamp or wax seal (B 36, 47).

## Level 2: Candlestick phone (B 48–59)

**Specification.** Choose a play or story for the phone. Hand in a written **analysis of the phone's requirements and look before designing**. Alter an existing candlestick-phone design (B uses one from Thingiverse) in size or orientation for that hypothetical production, keeping full fit and assembly. Manifold (B 53–54).

**Steps.**
1. Download the design's files and import them one at a time, in **millimetres** (B 49).
2. Mirror the body for the actor's hand (B 49).
3. Scale parts together, using select-all or by exporting and re-importing a group (B 51).
4. Check fit virtually; Fusion 360 does this better than Tinkercad (B 51).
5. Print a prototype at **5–10% infill** (B 51).
6. Lay out the plate: every part landing on the bed, supports added, short parts outside and tall ones in the middle. Add a wipe tower if needed (B 53).
7. Assemble with nuts, bolts and screws. Add a tie-line cord. Prime and paint (advanced) (B 55).

**Criteria** (B 54–55):
- **Analysis**: a concise story and a clear image of the prop that fits it.
- Manipulation, alignment and manifold, as for Level 1.
- **Arrangement**: files placed for print success, with supports.
- **Print**: parts print, fit together and don't break in use.

**Typical faults.** Parts not touching the bed; missing supports; the hook-to-body joint breaking (B 53, 59).

**Extensions** (B 56–57):
- Change the number of polygon sides.
- Design the phone around its owner's character.
- Make the dial spring-loaded.
- Mix filaments.
- Make it work electrically.

**Challenge questions** (B 59): Should the hook be reinforced? What parts are missing? How far away must the audience be for it to read, and does that suit your space? Is it character-driven or just cool? Would someone really use it?

## Level 3: Scanned button (B 60–69)

**Specification.** Scan a button you have only one or two of, make a printable .stl, print copies or new sizes, and sew them onto a costume. Manifold (B 62–63).

**Rig.** A scanner on a **tripod**, with the button on a **hand-turned lazy Susan**. Stand a shanked button on a washer (B 61–62). Before assigning the project, check that the scanner can capture the detail and adjust the brief if not (B 64).

**Criteria** (B 63–64):
- Manipulation.
- **Scan**: from capturing all of the design, down to "more blob than button."
- Manifold.
- Print, including fit.

**A sample CPSG** (common problems and solutions guide) (B 64–65):

| Problem | Fix |
|---|---|
| Scan inaccurate | Keep turntable speed and scanner distance consistent. Slow down |
| Not enough detail | Raise the scanner resolution, following the maker's guidance |
| Not scanning | Check it's plugged in |

**Extensions** (B 65–68):
- Vary nozzle size and layer height (see [ch. 30](../guide/30-3d-printing.md#where-the-sources-disagree) on B's layer-height figures).
- Redesign the shank and shear-test it, orienting the print so its layers don't cross the weak point.
- Research paints that survive costume wear.
- Anneal at 110–160 °C. It may shrink the print; B asks whether it also strengthens it.

## Level 4: Makeup prosthesis or mask (B 70–80)

**Specification.** Scan your face, then sculpt a mask or prosthesis on the scan in Meshmixer (B's example: a tree creature's nose and branch horns). Manifold and printable (B 71–72, 76–77).

**Before starting.**
- Check that the filament's SDS supports skin contact (B 71).
- Brief students on avoiding stereotyped or demeaning depictions (B 70).
- B gives masks only to **advanced students**, because fit and comfort are hard to grade (B 75).

**Printing TPU** (B 71–74):
- Use a direct-drive extruder and start at the cool end of the range.
- If filament bunches, add spool drag (B uses a spring clamp).
- Fix thin shells by adjusting extruder tension or cooling the incoming filament with a fan.

**Wearing** (B 73–74):
- Reshape with a heat gun.
- Attach with spirit gum; remove with baby wipes and the matching remover.
- **Stop at any irritation.**
- Hide layer lines with makeup, or prime with acrylic before application.

**Criteria** (B 77):
- Manipulation.
- **Scan**: detailed enough to build on, down to a scan too inexact to fit.
- Manifold.
- Print, including fit.

**Extensions** (B 78–80):
- Thinned edge "wings" for adhesion.
- Breathing holes, and their effect on the voice.
- Reduced infill for weight.
- Paint that doesn't irritate when dry.
- A surface texture that holds makeup.
- Matching pieces for several performers as a team project.

## Linear actuator (B 81–89)

**Specification.** Use Tinkercad's gear generator to make the drive, then design a drive train and housing and test the actuator. Manifold. It must **open a box lid** (B 85–86).

**Build** (B 81–85):
1. Make a large and a small gear, with a centre hole sized to the motor (bore out if needed).
2. Pin the gears on foam board or corkboard to test.
3. Use a type-130 or salvaged DC motor on 1.5–3 V.
4. Print a gearbox and grease it.
5. Fix a threaded rod to the large gear and trap a nut in a slotted tube, so the nut rides up and down as the rod turns.

**Criteria** (B 85–86):
- Manipulation.
- **Function of the actuator by itself**: works with few problems, needs a small redesign, needs a large redesign, or doesn't work.
- **Use**: opens the box, with evidence of problem-solving.
- Print.

**Troubleshooting** (B 86–87): Is there power? Is the battery charged and the right way round? Is the circuit continuous (multimeter continuity or test lamp)? Does the device work on its own? Are the joints soldered or wire-nutted, not taped?

**Extensions** (B 87–88):
- Reverse the polarity to reverse the motor.
- Change the gear ratio: gear down for lift, up for speed.
- Build a rack and pinion, worm gear or selectable-speed gearbox.
- Add variable speed, or Arduino-driven servos and steppers.

The mechanism must solve a props problem (B 89).

## Large print (group project) (B 90–101)

**Specification.** Teams of at least two. Choose a model from Tinkercad's featured collections. Scale it larger than the printer's bed so it needs **at least three pieces**. Cut it with the box tool set to "hole." Save each piece as its own .stl. Test-assemble on screen. Each student prints at least one piece. The team assembles, primes and paints the whole. Submit all files (B 96–100).

**Before cutting**, decide how pieces will join (pegs, pins, tabs, screws or tape) and design for it. Cut along logical, hidden breaks. Give the model a flat base. Inset letters to show the assembly order (B 93–94, 99).

**Criteria** (B 97):
- Manipulation.
- **Team process**: from a discussed and agreed plan with conflicts resolved, down to "a giant mess."
- Manifold.
- Print.
- **Final fit**: from all parts making a whole, down to not fitting.
- **Finish**: from painted to look like a single item, down to no finish.

**Close** with a written journal or a one-to-one and team debrief on how the group worked (B 101).

## Further project ideas (B 102–116)

| Project | Brief | Suggested assessment |
|---|---|---|
| **Science-fiction communicator** (B 102–104) | An original device for an invented or extended universe, recognisable as a communicator and only slightly beyond current technology. Either mix and match a printed kit of parts (altered with foam clay and salvaged phone parts) or design it whole | Believability; fit with the world; look of function |
| **Museum replica** (B 104–107) | An object for a period display, with the period set by the instructor. Scan it if available and rebuild missing parts. Recreate colour, texture and patina. Smaller version: antique furniture handles | Structure (before paint); accuracy of measurement and scale; finish |
| **Jewellery** (B 107–109) | A ring or pendant designed for **another student** to wear, with detail the audience can read. PETG or ABS preferred to PLA. Optionally a replica of a famous historical piece | Choose one focus (character, age, class, wealth, status, function or detail) and state it clearly in the prompt |
| **Spring clamp** (B 110–111) | Two arms, a pivot and an elastic "compression engine." Variations: a special-purpose clamp, or a spreader clamp | Does it do a real job? |
| **Measuring aid** (B 111–113) | A device that speeds a repetitive marking or measuring task, such as a stair-tread copier or a hem stand | Does it save prep or process time? |
| **Centering jig** (B 114) | A device that marks the centre of a board end or drawer face every time | Is it faster than a straight edge or square? |

**Before assigning any of these** (B 115): Can it be done in the time? Does your filament suit it? Do you have enough printers and print hours for every group? Will the device actually save time or money, or make work safer?

## Troubleshooting quick reference (B 19–22, 43–47, 117–118)

B's three opening questions: **Is it hot? Does it move? Is it sticking to the plate?** (B 117–118).

| Symptom | Likely cause (B) | Fix (B) |
|---|---|---|
| Corners lift; base uneven or squashed | First layer lacks squish | Adjust the z-offset or relevel the bed. Then use glue stick, bed spray or hairspray (B 19, 47) |
| Print won't stick at all | Nozzle too far from the bed; wrong temperatures | Check nozzle height, squish and temperatures for the material (B 118) |
| Layers separate | Nozzle too cool, no heated bed, or wet filament | Raise the temperature or add a heated bed. Dry the filament in a sealed box with desiccant (B 20) |
| Extruder clunks; filament feeds slowly | Hot end too cold | Raise the nozzle temperature in the slicer or during the print (B 20) |
| Molten blobs at intervals | Hot end too hot | Lower the temperature (B 20–21) |
| Too much or too little plastic everywhere | Wrong extruder steps per mm | Correct it in the firmware (B 21) |
| Part undersized on one axis | Loose belt, or stepper-driver current too low | Tighten the belt; adjust the driver following the maker's instructions (B 21) |
| Mirror-image print; axis homes away from its switch | Motor direction reversed | Fix in firmware or software, or reverse the motor plug at the board (B 21) |
| No extrusion, or a partial clog | Blocked nozzle or feed tube | Nozzle-cleaning kit, or one strand of 1/16" steel wire rope pushed through **at temperature**. A filed-down screwdriver clears the upper feed (B 21–22) |
| Parts rattle; quality drifts | Fasteners loosened by vibration | Check and tighten every 10–20 print hours (B 21) |
| Raised letters knocked off | Nozzle rubbing tall details | Check the z-offset; keep raised details low (B 43, 47) |
| Top skin droops or warps | Infill too sparse | Raise the infill density (B 47) |
| Flexible filament bunches in the feed | Filament softening before the hot end; too little drag | Lower the temperature; add spool drag; cool the incoming filament with a fan; adjust tension (B 72–74) |
| Bed covered in glue residue | Built-up adhesive | Razor scraper on glass or spring steel. Solvent, water or alcohol on stick-on beds, or replace them (B 19–20) |
| Electronics dead (actuator projects) | Power, polarity, an open circuit or a dead part | Check each in turn with a multimeter or test lamp; solder or wire-nut the joints (B 86–87) |
| Printer not responding | No power | "Is it plugged in?" (B 65, 117) |
