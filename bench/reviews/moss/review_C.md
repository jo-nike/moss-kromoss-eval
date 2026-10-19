# MOSS-Image review, set C (sci-fi, fantasy, environments, impossible geometry, physical effects)

50 images, 309 checks. Mean score **4.1** (5: 15, 4: 27, 3: 6, 2: 2). Checks: **80% pass**, 17% partial, 3% fail.
Standouts: C002, C004, C010, C018, C032, C038, C042, C050.

## Pass rate by check type

Objects 93% (n=114) · smoke/fire/glow 93% (14) · requested text 92% (13) · architecture 92% (38) · style 88% (8) · interactions 86% (14) · reflection/refraction 69% (26) · camera 67% (12) · creature anatomy 67% (18) · size ratios 55% (11) · light acting on the scene 52% (23) · exact counts 45% (11) · impossible geometry 0% (7)

## Failure modes

1. **Impossible geometry comes out possible.** The Penrose sculpture is an ordinary triangle (C029, score 2). Escher stairs are ordinary (C028); the spiral stair is stacked rings (C021).
2. **Lens and split-view optics are faked.** The sphere shows the window upright, not inverted (C023). The galleon has no hull below the waterline and no tentacle touches it (C037, score 2). Reflections drop parts (C020, C022).
3. **Light sources do not act on the scene.** The spell sphere leaves her face neutral and her shadow points at the camera (C013). Also C001, C009, C012, C046. Same as set F.
4. **Ratios shrink and loose counts drift.** The golem is 2.2x the girl, not 3x (C011). The giant is 1.4x the trees, not 2x (C025). The stack is 3x the castle, not 10x (C012). Loose counts drift too (C001, C003, C043).
5. **Specific shapes revert to defaults.** Leaf panels became rectangles and the spiral tower became rings (C008). The teardrop sub is a tram (C015), and the monorail is ordinary track (C033). See also C006, C027.
6. **Camera instructions soften.** "Straight up" became a tilt (C044); see also C001, C039.

## What worked

- **12 of 13 strings exact**, including "NO WEAPONS BEYOND THIS POINT" (C049) and a correctly mirrored "HALLORAN ST" (C050). The one miss was "DISTRIESS SIGNAL", in a smaller second line (C026).
- **Classic creatures were clean**: the dragon has 2 wings and 4 legs (C009), the griffin is correct (C010) and the hydra has exactly 3 heads (C038). Invented anatomy failed: the six-legged deer shows about 5 legs (C035), and the alien's four arms tangle (C049).
- **Explicitly numbered objects landed** (C015, C024, C034, C030).
- **Flat reflections worked** (C004, C042, C043, C050).

## What correlated with success

- **Length did not matter.** 30 words or fewer: 4.17 (n=6). 31-160: 4.09 (n=35). Over 160: 4.11 (n=9). The four prompts over 350 words scored 5, 4, 4 and 3, and C044 failed on its camera angle.
- **Medium did not matter.** Photo/film 4.08, painted 4.12 (n=25 each). The medium was always honoured.
- **Sub-type mattered.** Impossible geometry: 2.67 (n=3, small). Optics-centred prompts: 3.6 (n=8). Text prompts: 4.25 (n=8).
- **Inventory beats relations.** Named things appear 93% of the time. Size, light, count and mirror relations pass 45-69%.

## Prompting advice

1. Don't rely on MOSS for impossible objects or Escher logic. Spelling out the contradiction is untested.
2. Flat mirrors are safe. Lens inversion, refraction and split waterlines are not.
3. State the light's effect on the subject, and run seeds. This is untested; set F agrees.
4. Exaggerate size ratios. They came out at a third to two thirds of the request; overstating is untested.
5. Give objects exact numbers.
6. Keep critical text large and on the first line, and proofread smaller lines.
7. Invented creatures default to familiar animals. Describing each limb pair is untested.
8. Put a composition-defining camera instruction first.
