# Kromoss DMD 8-step review, set C (sci-fi, fantasy, environments, impossible geometry, effects)

50 images, 309 checks. Mean score **4.12** (5: 15, 4: 28, 3: 5, 2: 2). Checks: **76% pass**, 20% partial, 4% fail.
Standouts: C003, C004, C018, C019, C026, C035, C036, C050.

## Pass rate by check type

Requested text 100% (n=13) · style/medium 100% (6) · smoke/fire/glow 100% (12) · water reflections 93% (14) · camera viewpoint 86% (7) · props/placement ~85% · anatomy 58% (12) · impossible geometry 57% (7) · counts 44% (16) · glass optics 43% (7) · directed light on a subject 32% (19) · size ratios 0% (3)

## Failure modes

1. **Unrequested watermarks and signatures on painted styles.** 12 of 25 painted or illustrated prompts got one; 0 of 25 photo or film-still prompts did. Worst is C005 (a gibberish URL strip); also C006, C013, C025, C031, C037, C038, C040, C041, C046, C047, C049.
2. **Counts drift, usually up by one.** 6 domes for 5 (C015), 4 towers for 3 (C012), 4 hydra heads for 3 (C038), 2 braziers for 1 (C048), about 5 hands on the four-armed alien (C049). Under: 5 vehicles for 6 (C034), 1 wheel for 2 (C030). Threes mostly held (C003, C008, C025, C026, C037).
3. **Directed light doesn't land.** The shaft misses the altar (C024), the sphere doesn't light the face (C013), and the atrium isn't half-lit (C044). The stairwell doesn't darken (C021); the rim light (C001) and floodlight (C045) are weak. This matches set F.
4. **Size ratios are ignored in both directions.** The golem is 10x the girl, not 3x (C011), and the stack 3x the castle, not 10x (C012). The giant only matches the trees (C025), and the kraken is ship-sized (C037).
5. **Named or hybrid concepts become a default.** The Penrose triangle is a plain triangle (C029). The griffin's front talons are lion legs (C010). Geodesic glazing became radial (C044), and rigid sails are cloth (C008).
6. **Nested build lists collapse.** C030 lost its warship and second wheel. Long scene inventories held (C008, C018, C044), so this rests on one image.

## What worked

- **All 13 quoted strings were exact.** That includes small second lines ("DISTRESS SIGNAL", C026), a five-word sign (C049), and "HALLORAN ST" mirrored correctly in water (C050). Unasked text is gibberish (C045, C049).
- **Reflections and translucency** are strong (C020, C022, C026, C048, C050).
- **Architectural photography is the best category:** C017-C020 and C043.
- **Spelled-out creature anatomy held** (C009 dragon, C035 six-legged deer).

## What correlated with success

- **Short prompts scored lowest:** 3.5 at 30 words or fewer (n=6), 4.22 at 31-200 (n=40), 4.0 over 300 (n=4). Four of the six short ones carry watermarks and two were named concepts (C010, C029), so this is confounded.
- **Photo vs painted is close:** 4.16 vs 4.08. Unlike sets A and B, illustration did not win.
- **Text prompts scored 4.38** (n=8). **Impossible-geometry prompts scored 3.25** (n=4); C028, described part by part, beat C029, named only.

## Prompting advice

1. For painted styles, budget for watermark cleanup or reroll (cfg 1 has no negative prompt; a positive "no watermark" is untested).
2. Use quoted text freely, even several lines.
3. Keep exact counts at three or fewer, or expect one off.
4. Show scale with a tiny reference figure (C009, C016, C018, C036, C039), not a ratio.
5. Describe impossible geometry and hybrid creatures by their visible parts, not by name. This is untested; only the failures are shown.
6. For light that must hit a subject, state its visible result there and run several seeds.
