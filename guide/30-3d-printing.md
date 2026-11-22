# 30. 3D Printing for Props

> **Sources:** B (whole book, pp. 1–122). Especially pp. 1–22 (how printers work, slicing, infill, filaments, finishing, printer types, troubleshooting), 23–32 (teaching method), 33–101 (five graded projects), 102–116 (further projects and printed shop tools), 117–119 (summary troubleshooting and safety). Also H 10, 58, 66, 68, 165, 172; KF 6–7.
> **Companion:** [Appendix H: 3D Printing Project Briefs and Troubleshooting](../appendices/H-3d-printing-projects.md) condenses B's project specifications, assessment criteria and a fault-finding table.
> **[Check current]** 3D printing changes fast. B (2024, written 2023) names software (Tinkercad, Cura, Slic3r, Meshmixer, Fusion 360, Repetier), printer brands (Prusa, Anycubic, Creality, Ultimaker, Makerbot, Formlabs), a Thingiverse design number, scanning apps (Trnio, Qlone, Skanect) and prices (kits $100–$1,000, core XY from $300, scanners about $500). Two have already changed: Autodesk stopped developing Meshmixer in 2021, and Fusion 360 was renamed Autodesk Fusion in 2024 **[Verified 2026]**. Filament temperatures and safety data vary by brand. **Check each filament's current SDS and your printer's documentation.**

Robert C. Berls is a professor of drama at UNC Asheville and a working designer with about twelve years of 3D-printing experience (B, front matter). He wrote B **for instructors**: it explains printers in plain language and then lays out a sequence of graded classroom projects, each with a prompt, a rubric, common problems and extension ideas. Its core claim is that the printer is a tool, not the lesson. The challenge for students "should not be making the 3D printer work, but in the execution of their designs" (B 118).

The guide has touched on 3D printing only briefly until now, through Hart's 2013 notes on digital fabrication ([ch. 9](09-shop-space-and-tools.md#digital-fabrication-h-10-58)) and plastics ([ch. 16](16-plastics-and-foams.md#3d-printing-note-check-current)). This chapter covers the technology first, then B's teaching method, then the projects. Points not in B are marked **[Added best practice]**.

B focuses on **fused filament fabrication (FFF)**, where a melted plastic strand is laid down layer by layer, because the machines and materials are cheap. It also discusses resin printing (B 8, 18).

## How an FFF printer works (B 1–4)

- **The build volume.** B's reference machine has a build volume of about **8 × 8 × 8 in (512 cu in)**. This "eight-inch cube" is common among kit and pre-assembled printers (B 1–2, 90). The **x-axis** runs left to right, the **y-axis** front to back and the **z-axis** up and down (B 2).
- **Stepper motors** make the moves. A common 1.8° stepper has **200 steps per turn**. Driver chips can subdivide each step ("microstepping"), giving up to **3,200 steps per turn** (B 2). An unpowered stepper turned by hand clicks through these stops.
- **The controller** is an Arduino (B's example is an Arduino Mega with a printer "shield"), a Raspberry Pi or a proprietary board with stepper drivers. It turns the sliced file into pulses (B 2).
- **Belts and threaded rods** convert pulses into distance. Calibrating **steps per millimetre** in the firmware is a matter of simple algebra, and wrong values cause faults that look like other problems (B 3, 21).
- Other motor sizes (larger NEMA 23 and 34, smaller NEMA 14 and 11) exist but may not suit printing. Paper printers use simple DC motors with encoders, which lack the resolution and power for 3D work (B 3–4).

Print resolution, B sums up, comes partly from stepper motors "baby stepped" by hardware and software (B 4).

## Slicing and the first layer (B 4–6)

A **slicer** cuts a 3D model into horizontal layers, usually **0.1–0.3 mm** thick, and writes the toolpaths. B names Cura and Slic3r, and says Slic3r is no longer supported (B 4). **[Check current]** Slic3r's last stable release was 1.3.0 in 2018; PrusaSlicer and other forks grew out of it **[Verified 2026]**.

**The first layer matters most** (B 4). It needs the right amount of **"squish"** against the bed to stick, so the next layers don't drag the part loose.
- Get nozzle and bed temperatures right for the filament.
- When in doubt, put **glue stick** on the build plate (B 4).
- On a Prusa-type clone, B sometimes adjusts the z-axis by hand during warm-up after homing (B 4–5). Other printers need bed levelling or a z-offset change; follow the manufacturer's procedure (B 5).
- Check by touch (run a finger over the first lines) and by eye (B 5).

## Brims, rafts and supports (B 6–8)

| Structure | What it is | Why use it |
|---|---|---|
| **Brim** | An outline printed around the base before the part | Primes the nozzle and clears old filament, shows whether squish is right, and holds down the bed surface (it once held down the painter's tape used as a print surface) (B 6) |
| **Raft** | A grid laid on the bed under the first layer | A steady foundation and good adhesion, especially for a part with a narrow base that widens as it rises. Remove it afterwards (B 6) |
| **Supports** | Removable structures under overhangs: touching the bed only, under overhangs, or full | More likely success at the cost of print time. Some remove more easily than others; pick your settings and use them consistently (B 7) |

## Infill: how solid to print (B 8–12)

A print is never 100% plastic. Even "solid" layered strands leave voids, so a print won't match an injection-moulded part without post-processing (B 8–9).

**How much infill** (B 9):
- B reports that prop makers have concluded **50%** gives the best strength for print time. Above 50%, warping, failures, time and material all increase.
- Functional parts that carry weight or stress may go higher, but test it yourself.
- **30% is usually B's maximum for hand props**, and B calls a 30% average the "sweet spot" of speed and strength.
- **Vary density within a part**: for example, 15% for the first fifth and 45% for the rest because that section is the handle (B 9).

**Which pattern** (B 9–12):

| Pattern | Character | Use it for |
|---|---|---|
| **Grid** | Lines on the 45° bias. B's default: a balance of speed, strength and crush resistance (B 9) | Most props. Its vertical channels let you **pause the print and insert dowels or pour resin** for strength or weight; make sure the insert sits below the current layer before resuming (B 10) |
| **Hexagon (honeycomb)** | More filament and time per layer; more sidewall strength. Not built into some slicers, including Cura at the time of writing (B 11) **[Check current]** | Props that get dropped or stepped on (B 11) |
| **Line** | Parallel lines: strong on two sides, flexible on the other two. Probably fastest (B 11–12) | Speed over strength |

## Filament and other materials (B 12–15)

Filament comes in **1.75 mm** and **3.0 mm** diameters to suit the printer. The **nozzle size** (0.3, 0.4 mm and so on) sets the extruded strand width (B 12). Printers can also use liquid, paste or powder (B 12).

**PLA is B's go-to** for general props: easy to print, cheap, and easy to glue and alter afterwards. It is less durable and less impact-resistant, so B doesn't recommend it for runs of **more than about ten shows** (B 8, 13).

B's filament table, summarised (B 13–14). Temperatures are B's starting points; check the maker's figures for your filament.

| Filament | Nozzle / bed (B) | B's notes | Ventilation (B) |
|---|---|---|---|
| **PLA** | 210 °C / 50 °C | General use, easy, cheap. Absorbs moisture from the air; can warp; not very impact-resistant. Biodegradable | Usually needs only room ventilation |
| **ABS** | 225–245 °C / 90–110 °C | Heat- and impact-resistant; indoor or outdoor use. Can warp badly through poor bed adhesion; absorbs moisture | Strong odour. Fume extraction advisable indoors; check the SDS |
| **PETG** | 220–255 °C / 60–80 °C | "PLA's ease with ABS's strength." B lists it as food-compatible and chemical-resistant, but prone to moisture and to severe warping | Usually no special extraction, but assess your space |
| **Nylon** | 220–250 °C / tune the bed | Very strong; prone to warping; "finicky." Entry-level printers usually can't reach its temperature | Needs full venting. Can cause headaches and burning eyes; may release harmful VOCs |
| **TPU (flexible)** | Check the maker's figures | Rubbery, durable. Can make belting, moulds and similar | Check each maker's SDS |

**[Added best practice]** A filament's food-contact rating doesn't make a printed part food-safe: layer lines trap residue, and nozzles and additives vary. For anything that touches food or mouths, see [ch. 26](26-effects-props.md#food-and-drink-m-78-156157-h-6).

### Read the SDS (B 14–15, 118)

"Not all PLA is completely PLA" (B 14). For every filament, check the SDS for:
- what's actually in it;
- whether printing releases **ultrafine particles**;
- whether it releases **VOCs** when extruded;
- whether you need **HEPA or carbon filtration**, and whether a bolt-on unit is enough or you need a hood with extraction (B 14).

The more exotic the material, the more precautions it needs: "When in doubt, vent it out – safely" (B 15). In the closing chapter B goes further. If you can't find an SDS for a filament, question whether students should use it. **Don't rely on your own judgement** about whether fumes are safe; take the question to your administration or safety office, and wear the PPE the manufacturer recommends (B 118).

**[Verified 2026]** Since B was written, NIOSH has published *Approaches to Safe 3D Printing* (2023) for schools, libraries and makerspaces. It reports exposures to ultrafine particles, VOCs and other emissions from desktop printers, and recommends ventilated enclosures, local exhaust ventilation, administrative controls and PPE. EPA research also finds that ABS releases more particles than PLA. For respirator selection, see [ch. 10](10-health-and-safety.md#respiratory-protection-h-3132-3941). Hart's view on heated-plastic fumes is in [Where the sources disagree](#where-the-sources-disagree).

### Resin printing (B 8, 18)

Resin (photo-curing) printers build the part upside down out of a vat of liquid resin. They give **finer detail** quickly, but:
- resin costs more than filament;
- prints are **more fragile** and can't be heat-joined or easily altered;
- there's no infill: the part is solid or hollowed, and a hollow part needs a **drain hole** so uncured resin can run out;
- **liquid resin can cause skin sensitisation**, and parts usually need a UV curing chamber (B 18).

For these reasons B finds resin less useful for beginning and intermediate prop printing (B 8). For sensitisers and glove choice, see [ch. 10](10-health-and-safety.md#sensitization-h-35-also-h-279-282-304).

## Choosing a printer (B 16–19)

B weighs printers on a **budget–safety–time (BST) triangle**, a cousin of the project triangle in [ch. 5](05-budget-time-and-feasibility.md) (B 16).

| Type | How it moves | B's assessment |
|---|---|---|
| **Gantry / "bed-slinger"** (Mendel, Prusa, "bed y-axis"; commercial brands such as Anycubic, Creality, Ultimaker, Makerbot) | Bed moves in y; head moves in x and rises in z. Four or five steppers on 8 mm (5/16") steel rod | Cheapest. Kits about **$100–$1,000** **[Check current]**. Teaches the maintenance every maker needs. **Check and tighten before each major print, or every 10–20 print hours.** B's go-to: more upkeep, but the best cost-to-output ratio (B 17–19) |
| **Core XY** | Bed moves only up and down; head moves in a flat x–y frame | Less vibration, better quality. From about **$300** **[Check current]**. Usually enclosed against drafts (B 17–18) |
| **Delta** (Kossel, Rostock) | Three towers move a linked head | Few parts, easily scaled tall. Prone to vibration errors, slow, more failures (B 18) |
| **Resin** | See above | Fine detail; higher running cost; fragile prints; skin hazard (B 18) |

## Finishing prints (B 15–16, 55, 92–93)

B names four finishing methods (B 15–16):
1. **Mechanical.** Hand-sand from **220 grit**, working up as far as **2,000** for a factory finish. **Don't power-sand**: the heat melts the print. Sanding is slow and dusty, so wear PPE and choose the space with care. Alternatively, run parts in a **vibratory tumbler** with walnut shell or corncob media, which needs no attention but is noisy and takes space (B 15).
2. **Chemical.** Acetone, alcohol or another solvent (depending on the filament) smooths the surface. Some makers vaporise acetone with heat in a closed container to smooth ABS. This "can be dangerous and highly flammable" (B 15). See [ch. 10](10-health-and-safety.md#fire-safety-h-4244-m-149151).
3. **Coatings**, including paint. Choose materials carefully (B 15).
4. **Heat.** Some makers bake prints in a toaster oven at **160–170 °C** to fuse the outer layers. This can release harmful fumes or start a fire in the oven (B 16). For a button, B gives **110–160 °C**, notes that this annealing can shrink the print, and says it's usually done only with certain PLAs (B 68). See [Where the sources disagree](#where-the-sources-disagree).

**Priming.** For paint, B suggests **auto-body spray primer** (high- or medium-fill) or **PlastiDip**, sprayed or brushed (B 55). For large assemblies B also lists acrylic paint and gesso. Test for rub-off under handling, add a sealer if needed, and schedule repaints (B 93). KF uses PlastiDip on EVA foam too ([ch. 29](29-eva-foam-props.md#filling-and-priming-kf-2829-36-40-47)). General priming is in [ch. 24](24-painting-dyeing-and-finishing.md#priming-h-333334).

## Troubleshooting (B 19–22, 117–118)

B sorts failures into **adhesion, extrusion and mechanical** problems (B 19). Its closing chapter boils them down to three questions: **Is it hot? Does it move? Is it sticking to the plate?** (B 117–118). [Appendix H](../appendices/H-3d-printing-projects.md#troubleshooting-quick-reference-b-1922-4347-117118) has a fault-by-fault table. The main points:

- **Bed adhesion.** Corners lifting means not enough squish. Re-set the z-offset or relevel the bed, and teach students this early. If that fails, use **glue stick** (B's choice: cheap and easy to find), bed spray or hairspray. Clean residue off glass or spring steel with a razor scraper; stick-on surfaces need solvent or replacing; magnetic beds also wear out (B 19–20).
- **Layers not bonding.** Raise the nozzle temperature or add a heated bed. If that doesn't work, the filament may have **absorbed moisture** and be steaming as it extrudes: change it and dry it in a sealed container with desiccant (B 20).
- **Extrusion.** A **clunking** extruder and slow feed mean the nozzle is **too cold**. **Molten blobs** mean it's **too hot**. Too much or too little plastic overall suggests wrong **steps per mm** in the firmware (B 20–21).
- **Mechanical.** Prints short on one axis: loose belts or low stepper-driver current. Mirror-image prints, or an axis homing *away* from its limit switch: a reversed motor direction in firmware, software or wiring (B 21).
- **Clogs.** Use a nozzle-cleaning kit or a **single strand unpicked from 1/16" steel wire rope (aircraft cable)**, pushed through with the hot end at temperature. A cheap flat screwdriver with its edges filed down makes an upper-feed cleaner (B 21–22).
- **Vibration loosens fasteners.** Tighten every 10–20 hours (B 21).

## Teaching with 3D printing (B 23–32)

B's teaching chapter draws on Barbara Blackburn's *Rigor Is Not a Four-Letter Word* (2018). Its central idea is to **assess the process, not only the product** (B 23–24).

- **Failure is the lesson.** B would rather hire someone who failed and then came back to succeed than someone who has never failed (B 24). Allow **one or two "do-overs"** per course to take grade pressure off (B 24).
- **The product is an artifact** of the process and should fill only one or two assessment slots. Use **waypoints** during the work; they also catch software problems early (B 24).
- **Timing "how."** Asking *how will I make it?* too early shuts down design; too late leaves no time to succeed. Start with *why*: "We do not create for prop's sake; we create to move the story forward." Students should analyse the story before designing (B 25–26).
- **Rubrics as a contract.** Treat the rubric as an agreement with each student. Tailor it by adding or removing criteria rather than writing a separate rubric for each person (B 26, 28). B follows Blackburn's three phases: set standards, equip students through instruction and support, and have them meet the standards through the work (B 27).
- **Debrief questions.** "What did you do well?", "What needs improvement?" and "What would you change about your process?" work once trust is built (B 27).
- **Competition.** Useful if it pushes ideas, but **never make grades the prize**, and don't let a class game decide real outcomes such as who designs props for the next show. Those choices need a clear, open process (B 27–28).
- **Individual vs. group.** Individual projects should build on each other; group projects reinforce skills or give a student a second try. Balance teams (B 28–29).
- **Meet students where they are.** Many have grown up with intuitive technology but never learned basic file and software skills. Explain clearly without talking down, and repeat expectations (B 29–30).

### The process lab (B 30–32)

B contrasts the production meeting's "get it done" mindset with a **process lab**, where learning leads. Its steps (B 31):
1. **Process-based rubrics**, starting with a pre-build description or drawing so the student works with intent.
2. **Room to fail**: a chance to redesign after an unsuccessful attempt, with an improvement plan.
3. **Student ownership** of the assessment: students propose what it should focus on.
4. **Honest self-assessment** of effort and obstacles.
5. **A feedback loop** that carries that self-assessment into the next project.

It needs enough **time, budget, tools and safety procedures**, plus room for frustration: walking away is fine as long as the student comes back (B 31). **Blame** is its main enemy (B 32). Ask students to rate their success from one to five and say concretely what would move them up a point. "Do better" isn't an answer (B 32).

## The graded projects (B 33–101)

B's core sequence runs from a flat card to multi-part, moving and wearable prints. Each project has a prompt with a due date, a four-level rubric, a debrief and "additional rigor" options. Full briefs are in [Appendix H](../appendices/H-3d-printing-projects.md).

**The rubric pattern** (B 34 and each project). Every criterion is scored **4 (successful)**, **3 (needs focus on one area)**, **2 (needs focus on two areas)** or **1 (retry with improvement plan)**. An **average of 2.5 or above** counts as satisfactory, and students may redo a project to raise the score (B 34, 55, 64, 78, 86, 97). Criteria change by project: manipulation, alignment, manifold and print for the card; story analysis and plate arrangement added for the phone; scan quality for the scanning projects; mechanism function and use for the actuator; team process, final fit and finish for the group print.

| Level | Project | New skills | Software (B) |
|---|---|---|---|
| 1 | **Lettered card** (B 33–47) | Resizing primitives, raised text, recessed symbols, manifold export to .stl | Tinkercad |
| 2 | **Candlestick phone** (B 48–59) | Modifying a downloaded design for a show; mirroring; multi-part fit; supports and plate layout; licences | Tinkercad (Fusion 360 for fit checks) |
| 3 | **Scanned button** (B 60–69) | 3D scanning; copies and resizing; layer orientation and strength | Scanner software |
| 4 | **Makeup prosthesis or mask** (B 70–80) | Flexible filament; scanning a face; digital sculpting; skin adhesives | Meshmixer |
| — | **Linear actuator** (B 81–89) | Gears, DC motors, simple circuits, rotary-to-linear motion | Tinkercad gear generator |
| — | **Large print, group** (B 90–101) | Splitting a model, joining, seam finishing, teamwork | Tinkercad |

### Level 1: lettered card (B 33–47)

A 4 × 8 cm, 1 mm-thick card with the student's name in raised letters **6–8 mm** tall and a symbol recessed **0.3 mm** (B 33). It teaches the basics used in every later project: resizing primitives, adding or cutting text and shapes, and making the model **manifold** (a closed skin with no holes) (B 35).
- **Open or constrained prompt.** An open prompt gives room to play but can overwhelm. A constrained prompt states every dimension and gives you clear grading points. Put the overall shape first, then the details: "First body, then limbs" (B 36–37).
- **Common faults:** text or symbol not touching the card ("spaghetti for everyone"), a symbol that only "kisses" the surface so it doesn't print recessed, and tall letters that snap off (B 43). In printing: corners lifting from poor squish, the nozzle rubbing letters loose, and low infill letting the top skin droop (B 47).
- **For props:** the same skills make stamps and wax seals. Always ask whether the detail will read and whether it serves the story (B 47). Compare [ch. 25](25-graphics-and-paper-props.md).

### Level 2: candlestick phone (B 48–59)

Students download an existing candlestick-telephone design from Thingiverse (B gives the design number) and alter it for a show they choose, writing a **story and character analysis before they design** (B 48, 53).
- **Licences.** B explains Creative Commons licences on Thingiverse as attribution (you may sell prints if you credit the designer) and non-commercial (personal use only), sometimes combined, and asks students to respect each design's terms (B 48–49). **[Check current]** **[Verified 2026]** Creative Commons actually uses four elements (BY attribution, NC non-commercial, SA share-alike, ND no derivatives) combined into six licences, and every one requires attribution. See [ch. 25](25-graphics-and-paper-props.md#copyright-and-trademarks-h-355).
- **Import in millimetres.** Importing a millimetre file as inches turns each millimetre into a foot, giving a phone too big for the stage (B 49).
- **Mirror** the body to move the earpiece hook for a **left- or right-handed actor** (B 49). Squash the height for a different look (B 51).
- **Check fit virtually** before printing (B suggests Fusion 360 for better fit tools), then print a **prototype at 5–10% infill** to check size, fit and use with little material (B 51).
- **Plate layout.** A common beginner error is parts not "landing" on the bed. Generate supports. Place short parts at the edges and the tallest in the middle, or print one part at a time. A wipe tower helps with over-extrusion (B 53).
- **Finishing:** assemble with nuts, bolts and screws; make the cord from tie line; prime as above (B 55). Expect students to want to keep their phones, so print spares for stock (B 56).
- **Extensions:** change the polygon count (raw prints look scalloped), design for a character trait, spring-load the dial, mix filaments, or wire it with working electronics (B 56–57). "Almost everything that can be classified as a prop is meant to interact with the human body in some way. Can someone actually use it?" (B 57).

### Level 3: scanning a real button (B 60–69)

**Ways to digitise an object** (B 60–61): photogrammetry (many photos processed into a model); a touch probe on a CNC machine; a 3D camera with the object on a turntable; or measuring it and modelling it by hand. Budget options include an old Xbox **Kinect** with a PC adapter and free scanning software, phone apps that use the camera or LIDAR, or a low-end scanner for about **$500** **[Check current]** (B 60–61).

**Scanning technique** (B 61–62):
- Mount the scanner on a **tripod** to cut vibration.
- Keep distance and speed **consistent**, and capture every angle.
- **Small object with a flat base: turntable** (B uses a hand-turned lazy Susan). **Statue or large object: walk around it.**
- Stand a shanked button on a washer to keep it level.

The brief: scan a button you have one or two of, then print enough copies (or new sizes) to finish a costume, and sew them on (B 62–63). **Check first that your scanner can capture the detail**, and write a **common problems and solutions guide (CPSG)** for your rig (B 64). Don't single out students who struggle; help one-to-one (B 65).

**Extensions** (B 65–68):
- **Layer height and nozzle size** trade detail against time. B says 0.1 mm layers show more detail, then suggests trying 0.5 mm to see whether it reveals all the detail (B 65).
- **Layer "grain."** Prints are layered like plywood and break along the layers. Orient the part so the layers don't run across a weak point such as the shank, and **shear-test** it on the costume (B 66–68). Compare grain in [ch. 17](17-structure-and-armatures.md#grain-h-188189).
- **Paint** that survives costume wear, and annealing (see [Finishing](#finishing-prints-b-1516-55-9293)) (B 68).

### Level 4: makeup prosthesis or mask (B 70–80)

B admits that gluing printed **TPU** to faces isn't usually the props department's job, but sees it as a logical next step (B 70). B also asks instructors to steer students away from **racist, sexist or stereotyped** exaggeration of facial features (B 70).

- **Flexible filament is temperamental.** Within a window of about **10 °C** it either flows well, won't extrude or bunches in the feed. Test first (B 71). B uses an older Prusa i3 clone with a **direct-drive extruder** and adjustable tension, which is easier to feed and watch (B 71).
- **Skin safety.** The TPU B used had an SDS showing no skin-contact hazard. **Check every product, because the same material from another maker may differ**, and keep checking as new data appear (B 71).
- **Workflow:** scan your nose and forehead, sculpt in **Meshmixer** (B finds its sculpt brush closest to theatre-degree skills; Fusion 360 or Blender also work), leave space for the real nose, export, and print at the low end of the temperature range (B 71–72). **[Check current]** Meshmixer is no longer developed **[Verified 2026]**.
- **If the filament bunches,** add drag to the spool. B clips a **spring clamp** against it (B 73). Thin shells and gaps in the infill come from feed problems; adjust extruder tension or blow a fan on the filament entering the hot end (B 74).
- **Fitting and wearing.** Reshape with a heat gun. B attaches with spirit gum and removes with baby wipes and the matching remover. **Any discomfort or irritation: stop**, adjust, or switch to another filament such as flexible PLA (B 73–74).
- **Layer lines** are hidden with makeup after application or acrylic primer beforehand (B 74).
- **Masks.** Scan the face as a base. B's printed Commedia masks in flexible PLA took **four hours** to print, spring back when crushed, and need only small adjustments per actor. Moleskin helps with sweat and comfort. B gives this only to **advanced students**, because fit and comfort are hard to grade (B 75).
- **Extensions:** thin the edges into "wings" for better adhesion; design **breathing holes** and test how the piece changes the voice; check whether paint fumes irritate once dry, and whether makeup sticks (B 78–80).

For moulded alternatives and life casting, see [ch. 21](21-molding-and-casting.md#molding-the-human-body-h-286290).

### Moving parts: a linear actuator (B 81–89)

The project needs basic **soldering** ([ch. 15](15-metalworking.md)) and small DC motors: salvaged from toys or printers, or bought as type-130 motors (B 81).
1. Make a large and a small gear with Tinkercad's **gear generator**. Pin them to foam board or corkboard to test the drive train, then run the motor from a **1.5–3 V** battery (B 81–84).
2. If the drive works, print a **gearbox** and grease it (B uses white lithium grease) (B 84).
3. **Rotary to linear:** fix a threaded rod to the large gear and trap a nut in a slotted tube. As the rod turns, the nut travels up or down. This can drive wings, lifts and similar effects (B 84–85). The test is whether it **opens a box lid** (B 85–86).

**Electrical troubleshooting** for students (B 86–87): Is there power? Is the battery charged and connected the right way round? Is the circuit continuous? Does the device work? **Test components before installing them**, using a multimeter on continuity or a test lamp. Make joints with **solder or wire nuts, not tape** (B 87).

**Gear ratio** (B 87–88): reversing polarity reverses the motor. A small gear on the motor driving a larger one (or more gears) **slows the rod and increases lift**; the reverse **increases speed and reduces lift**. Extensions: rack and pinion, worm gear, a selectable-speed gearbox, variable speed, or Arduino-controlled servos and steppers. But "these projects must do something other than exist": open a mailbox remotely, move the eyes of a creepy portrait, make a plant grow and flower (B 88). B notes that coding and electronics may take the project beyond a printing course (B 88). See [ch. 17](17-structure-and-armatures.md) and [ch. 26](26-effects-props.md#practicals-and-electrics-m-10-32-h-2).

## Large prints on small printers (B 90–101)

To print something bigger than the bed, **cut the model into parts** or buy a large-format printer (B 90). B's shop most often splits **statues and busts** (B 93).

**Plan the cuts** (B 93–94):
- **Cut at logical breaks** where seams will hide, for example around the outside of a face, not down its middle.
- Plan for the best-looking result, not a grid or the easiest line.
- Give the model a **flat base** to build up from.
- Add **printed pegs or dowels** to align parts ("think mortise and tenon").
- **Inset reference letters** (as on the lettered card) to show the assembly order. Assemble from the bottom up or outward from the most detailed area.

**Joining** (B 90–92):

| Method | B's notes |
|---|---|
| **Screws or bolts** in printed bosses | Slow; the print can crack around the metal (B 90) |
| **Polyurethane glue** | Bonds well to PLA and can be sanded, but **foams** as it reacts with moisture; look for a low-foam product (B 90–92) |
| **Super glue (CA)** | Needs perfectly flat faces; otherwise use **thick CA** from a radio-control model shop (B 92) |
| **Not** high-temperature hot glue or construction adhesive | The heat or the solvents deform the print (B 92) |
| **Automotive double-sided tape** | A very good bond, though the part grows by the tape's thickness (B 92) |

**Finishing seams:** sand, or fill with **acrylic caulk**, **low-temperature hot glue**, or **hot air** (from a paint-stripping heat gun to an electronics rework tool) (B 93). Then prime and paint (B 93). Clamp or tape parts while they set, ideally on a **dedicated table**, because vibration is a major problem (B 94–96).

The group brief: each partner prints at least one part of a model divided into **at least three pieces**, then the team assembles, primes and paints it. B's example is a triceratops skull cut into four with Tinkercad's box tool set to "hole," each part saved as its own file and test-assembled on screen first (B 96–100). Close with a **reflective journal** or debrief on teamwork (B 101). See also [ch. 13](13-adhesives-fasteners-and-assembly.md) and [ch. 23](23-surfaces-texture-and-coatings.md).

## Further projects (B 102–116)

- **Science-fiction communicator** (B 102–104). Not a copy of a franchise device but a new one, in a universe the student invents or extends. Either print a kit of bodies, buttons, grilles and "screens" to mix and match (altered with foam clay, plus parts salvaged from old phones), or design and print it whole for a manufactured look. It should look **just slightly beyond today's technology**, so the audience believes it works. Assess believability, fit with the world, and the look of function. Steampunk or dieselpunk versions work too.
- **Museum replica** (B 104–107). Fix the period for students. Scan an available object and rebuild missing parts digitally. Recreate colour, texture and patina with traditional paint. A smaller version is replacement **handles and hardware for antique furniture**, which demands careful measuring ([ch. 12](12-drawings-measuring-and-layout.md)). Assess structure, accuracy and finish. Pairs with [ch. 27](27-period-research.md).
- **Jewellery** (B 107–109). Rings and pendants with detail **the audience can read**, not just the actor. B suggests PETG or ABS over brittle PLA. **Design for another student to wear**, since prop makers build for actors, not themselves. B recommends jewellery-supply catalogues and period references (B cites Newman 1994 and Duncan James 2008). Possible focuses are character, age, class, wealth, status and function. Keep the prompt tight, because the project "can get out of control." Try different nozzle sizes (this may need a firmware change). B also mentions wax printers for **lost-wax metal casting**, and metal jetting and laser sintering (B 109). See [ch. 21](21-molding-and-casting.md).
- **Printed shop tools** (B 110–114). B picked tools that don't take impacts:
  - **Spring clamps**: two arms, a pivot and a "compression engine" (rubber bands, hair ties or surgical tubing), or a **spreader clamp** that pushes apart (B 110–111).
  - **Measuring aids**: a **stair-tread marking device** (two bolts, two printed parts and a scrap of wood) that copies a damaged tread for replacement, and a **hem stand** that also works for hemming curtains in place (B 111–113).
  - **Centering jigs**: for example, one that marks the centre of a board end for the lathe (B 114).

  Compare jigs in [ch. 12](12-drawings-measuring-and-layout.md#jigs-h-9799).

**Is the device worth it?** (B 115). B times a technical director's preference for 25° bevels on both short sides of platform legs. A plain cut took 30 s; each bevel added 35 s, so each leg took 1 min 40 s. Over 450 legs that came to about nine extra hours: roughly $500 of labour, $60 of electricity and $150 of blades, "a little over $700 for a preference." A printed jig or gadget should save time or money, or make the shop safer (B 115). Compare the needs-and-means approach in [ch. 11](11-the-build-method.md).

## Planning a course (B 117–118)

- **Pace.** For students and instructors new to printing, B's projects fill **more than a semester**. With some experience, the projects in B's chapters 3–8 fit **one semester**, depending on how many printers you have and which filaments you use (B 117).
- **Capacity.** Before assigning a project, ask whether it fits the time, whether your filament suits it, and whether you have **enough printers and print hours** for every group (B 115).
- **Keep growing.** Repeating the same projects starves your own creativity; start small and expand (B 118).

**[Added best practice]** Put printers on the shop safety checklist ([ch. 10](10-health-and-safety.md)). That means a hot-surface warning, never leaving a print running unattended without a plan for fire, ventilation matched to the filament, and a log of print hours for B's 10–20-hour maintenance checks.

## Where the sources disagree

| Topic | B says | Other source says |
|---|---|---|
| Polyurethane glue's foaming | Foaming is the downside of polyurethane glue on prints; look for a low-foam product (B 90–92) | It foams slightly, which fills small gaps (H 68) |
| High-melt hot glue | Don't use high-temperature hot glue on prints; the heat deforms them. Low-temperature hot glue can blend seams (B 92–93) | Use high-melt hot glue for structural joints (H 66). (Hart isn't discussing printed plastic) |
| Typical hobby filament | PLA is the go-to; ABS needs more heat and fume extraction (B 8, 13) | Hart (2013) describes hobby printers as mostly ABS extrusion (H 10, 58, 165) |
| Spray primer | Auto-body spray primer works on prints (B 55, 93) | On EVA foam, "stay far away from spray paints," which crack when the foam flexes (KF 7). (Different substrates) |
| Fumes from heated plastic | PLA usually needs only room ventilation; ABS, nylon and TPU need extraction; "when in doubt, vent it out" (B 13–15) | Heated thermoplastic fumes are a mix no respirator cartridge is rated for; use minimum heat and extract the fumes (H 172) |
| Heat-finishing temperature (B against itself) | 160–170 °C in a toaster oven to fuse outer layers (B 16) | 110–160 °C to anneal a PLA button (B 68) |
| Infill "sweet spot" (B against itself) | Prop makers find 50% gives the best strength for print time (B 9) | 30% is the usual maximum for hand props and the "sweet spot" (B 9–10) |
| Layer height for detail (B against itself) | Slicers use 0.1–0.3 mm layers; 0.1 mm shows more detail (B 4, 65) | Try 0.5 mm to see whether it reveals all the detail (B 65) |

## Key terms

FFF / FDM · resin (photo-curing) printing · build volume · x/y/z axes · stepper motor · microstepping · steps per mm · firmware · slicer · layer height · first layer / squish · z-offset · bed levelling · brim · raft · supports · infill (grid / hexagon / line) · manifold · .stl · PLA · ABS · PETG · TPU · nozzle · hot end · direct drive vs. Bowden · heated bed · ultrafine particles · VOCs · gantry (bed-slinger) · core XY · delta (Kossel/Rostock) · BST triangle · annealing · vibratory tumbler · photogrammetry · turntable scan · CPSG · Creative Commons licence · spool drag · linear actuator · gear ratio · wipe tower · process lab · improvement plan

## For the classroom

- **Lettered card to wax seal.** Run B's lettered card (B 33–47; [Appendix H](../appendices/H-3d-printing-projects.md#level-1-lettered-card-b-3347)), then have students turn the same skills into a wax-seal stamp or signet for a show on your season, and test it in real sealing wax ([ch. 25](25-graphics-and-paper-props.md)).
- **Infill shoot-out.** Print the same handle at 15%, 30% and 50% in grid, hexagon and line infill. Time each print, weigh it, then drop-test and crush-test it. Compare the results with B's figures, including the two "sweet spots" (B 9–12).
- **Character phone.** Following B's Level 2, students choose a play, write the owner's character analysis first, then alter a downloaded phone (mirroring for the actor's hand, proportion, polygon count) and present how each change serves the character (B 48–59). Add a licensing check against the design's actual Creative Commons terms.
- **Scan and replicate.** Students scan a costume button or a piece of antique furniture hardware, print copies, then test strength in the layer direction and paint to match (B 60–69, 106).
- **Mechanism with a purpose.** Teams build B's linear actuator, then use it in a small stage effect: a box that opens itself, a portrait with moving eyes, a growing flower. They must test every component with a multimeter before installing it (B 81–89; [ch. 26](26-effects-props.md)).
- **Worth printing?** Students propose a printed shop jig or tool and justify it with a time and cost estimate in the style of B's platform-leg example, compared with doing the task by hand (B 110–115; [ch. 11](11-the-build-method.md)).
