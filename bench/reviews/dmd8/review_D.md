# Kromoss DMD 8-step review, set D (cartoon, anime and art-style range)

50 images, 296 checks. Mean score **4.24** (5: 17, 4: 28, 3: 5). Checks: **81% pass**, 16% partial, 3% fail.
Standouts: D003, D009, D012, D021, D035, D037, D039, D040.

## Style fidelity by family

Craft/physical media 4.50 (n=8) · paint and drawing 4.40 (10) · anime/manga captions 4.40 (5) · print traditions 4.27 (11) · anime tags 4.17 (6) · flat digital and pixel 3.80 (5) · western cartoon/comics 3.75 (4)

- **The medium landed in 44 of 50 style checks, with no anime drift.** Ukiyo-e (D012), Mucha (D013), steel engraving (D039), manuscript (D035), embroidery (D021), riso (D029), ink wash (D032) and 90s cel (D004) all read as the real thing.
- **Drift goes toward clean modern commercial rendering.** The engraved plate became a smooth digital botanical (D026), plasticine became vinyl toys (D017), impasto shows only in the clouds (D050), and the 1930s rocket-train is a bullet train (D033).
- **Texture terms are underplayed or taken literally.** Ben-Day dots are faint (D007), there is no dithering (D015), and "fingerprints" became inked whorls (D038).

## Caption vs tags

Tags 4.20 (n=10), captions 4.25 (n=40). Tag checks passed 87% against 80%, but tag checks were simpler. Tags carried style well (D042, D046, D048). They failed on relations a tag cannot bind: sitting on the motorcycle (D042, broken handlebar), who holds which instrument (D049), and whether the ladle is held (D047). This is suggestive only (n=10).

## Multi-panel and speech bubbles

- **Panel count and order were right in all four layouts** (D006 five panels right-to-left, D008, D040, D044).
- **Every requested dialogue line was exact** (D006, D008, D040). The misses were "SKRRTT" and a thought cloud drawn as a speech balloon (D006).
- **Continuity broke twice.** D008 panel 2 duplicates the penguin and drops the walrus. D044's girl changes hair, and its balloons are pseudo-kana.

## Failure modes

1. **Deliberate deviations revert to the default.**
   - The frog knight became human (D015).
   - The three-legged dog has four legs (D018).
   - Pie-cut eyes became round (D002).
   - The ballerina stands en pointe instead of sitting (D022).
   - The knitted cap became a flat cap (D011).
2. **Interactions and staging slip.** The ladle floats in the pot (D047), the raccoon is not behind the can (D001), the courier does not leap (D006), and the cat is not by the fire (D030).
3. **Secondary text degrades.** The slogan reads "BUILD THIE FUTURE" (D014), "SUGAR" is illegible (D017), and D027 has garbled extra labels. Accents were correct (D013, D037).
4. **Fake signatures and watermarks appear unasked** (D005, D022, D023, D047, D050).
5. **Loose counts drift by one** (D016, D025).

## What correlated with success

- **Length did not matter.** 30 words or fewer: 4.18 (n=11). 31-160: 4.29 (n=35). Over 160: 4.00 (n=4). D003 scored 5 at 373 words.
- **Historical styles with strong signatures scored best.** Generic digital styles (vector, pixel) scored lowest.
- **Inventory beats relations.** Named objects appear. Poses and holding cause most partials.

## Prompting advice

1. Name the medium plus 2-3 physical tells.
2. To deviate from a default (three legs, a frog knight), state it early and run seeds. Restating it is untested.
3. Make critical text the largest string and proofread it.
4. Use captions when who-holds-what matters (n=3 tag failures).
5. Describe texture as appearance, not as object nouns.
6. Expect signatures and watermarks to need cropping. cfg 1 allows no negative prompt.
7. Check character identity in every panel.
