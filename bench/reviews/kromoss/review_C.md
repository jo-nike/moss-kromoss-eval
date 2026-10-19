# Kromoss review, set C (sci-fi, fantasy, environments, impossible geometry, tricky effects)

50 images, 309 checks. Mean score **4.04** (5: 13, 4: 27, 3: 9, 2: 1). Checks: **79% pass**, 18% partial, 3% fail.
Standouts: C003, C016, C018, C019, C022, C026, C031, C050.

## Pass rate by check type

Requested text 100% (n=13) · style/medium 100% (8) · reflection/refraction 85% (26) · perspective/architecture 83% (30) · elements/placement/action 83% (130) · light, smoke, fire 81% (53) · counts 56% (16) · scale cues 55% (11) · creature/robot anatomy 47% (17) · impossible geometry 20% (5)

## Failure modes

1. **Size ratios in words are ignored.** Golem 10x the girl, not 3x (C011). Fire giant tree height, not twice (C025). Sea stack 3x the castle, not 10x (C012). Kraken about ship-sized (C037). "Ten-storey" mech about four (C045). A tiny figure as the scale cue works (C016, C036, C009).
2. **Defining anatomy breaks on hybrids and multi-headed creatures.** Four heads for "exactly three" (C038, the only 2). Wingless griffin (C010; the prompt never said "wings"). About eight legs on the six-legged deer (C035). The standard dragon was correct (C009).
3. **The key interaction drops while the props stay.** The robot's can is away from the poppy (C032). No tentacle touches the hull, which is not drawn below the water (C037). The orb swallows the wizard's head (C013). The beam misses the altar (C024). The queen is not climbing (C048).
4. **Secondary counts drift; the headline count holds.** Held: moons, domes, braziers, riders (C003, C015, C024, C025). Slipped: 5 vehicles for 6 (C034), 4 arches for 7 columns (C043), 1 footbridge for 2 (C044), towers (C012), spokes and panels (C030).
5. **Specific lens physics fails; plain reflections succeed.** There is no inverted window in the sphere (C023). The lake reflection drops the deck (C020), and the android's refraction is weak (C027). Still-water mirrors were right in C022, C043 and C050, where the reflected text is correctly flipped.
6. **Impossible geometry reads as odd but possible** (C028, C029). Only two images.
7. **One-offs.** Sails float with no ships (C008); a near-nude body shows under the raincoat despite the nsfw negative (C004).

## What worked

- **All 13 quoted strings were exact** (C001, C004, C026, C030, C031, C033, C049, C050). Unasked background text is gibberish (C031).
- **Every requested medium was honoured:** gouache (C006), watercolor and pencil (C047), engraving (C028), litho (C033), model shot (C030).
- **Architecture and one-point perspective were strong:** C014, C017, C018, C019, C043.

## What correlated with success

- **Length barely mattered.** 30 words or fewer: 4.0 (n=6). 31-140: 3.91 (23). 141-200: 4.24 (17). Over 300: 4.0 (4). C018 met all 8 checks at 357 words; C008 got a 3 at 351.
- **Photoreal and painted were level:** 4.08 vs 4.0 (25 each).
- **Subject type mattered most.** Text prompts averaged 4.38 (n=8), creature prompts 3.33 (n=6) and impossible geometry 3.0 (n=2).

## Prompting advice

1. Show scale with a reference object in the frame, not a ratio.
2. List every creature part with its count, including obvious ones ("two feathered wings"). Place each head ("one left, one middle, one right; no other heads"). Untested.
3. State the main interaction early as visible contact ("the spout directly above the poppy").
4. Short quoted text is safe on any surface.
5. Run several seeds for lens effects. Still-water reflections are reliable.
6. Avoid Penrose and Escher constructions unless you can iterate.
7. Treat counts of secondary objects as approximate. Make the count you need the subject of the image.
