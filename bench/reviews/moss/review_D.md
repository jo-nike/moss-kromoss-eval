# MOSS-Image review, set D (cartoon, anime and art-style range)

50 images, 296 checks. Mean score **4.24** (5: 16, 4: 30, 3: 4). Checks: **83% pass**, 14% partial, 2% fail.
Standouts: D003, D004, D006, D007, D012, D013, D027, D037.

## Style fidelity by family

- **Print and graphic styles are strongest** (4.31, n=13): ukiyo-e (D012), Mucha poster (D013), blueprint (D027), botanical plate (D026), engraving (D039).
- **Craft and 3D** (4.38, n=8): embroidery (D021), papercraft (D019), low-poly (D016) and claymation (D017) look photographed.
- **Retro animation is era-accurate**: 90s cel (D004, D042), rubber-hose (D002), Bronze Age comics (D007).
- **Drift goes toward polish.** Gouache became smooth digital paint (D010), and pastel (D022), "loose" charcoal (D023) and crayon (D036) are too tidy. The chibi became a 3D vinyl figure (D005), the photomontage an engraving (D014). Art Deco got a photoreal Earth and bullet train (D033).
- **Pixel art was never crisp** (3 of 3: D015, D030, D045): the edges are soft or anti-aliased.

## Caption vs tags

Captions 4.28 (n=40), tags 4.10 (n=10), with equal check pass rates (83% vs 85%). Single-subject tags work (D046, D048 scored 5). Tags fail where roles must be assigned: the instruments were not bound to individual girls (D049), and "multiple panels, speech bubble" gave overlapping panels and gibberish (D044). Only 10 tags images.

## Multi-panel and speech bubbles

- **Per-panel captions worked**: D006 (5 panels, right-to-left), D008 (4 across) and D040 (4 stacked) had the right counts, order and character consistency.
- **58 of 59 requested strings were exact**, including È, É, "·" and a 7-string blueprint. The miss was a doubled SKRRT (D006).
- **Bubble mechanics slip.** One tail points to the wrong speaker (D008), a speech balloon was drawn as a thought bubble (D006), quotes were added (D009) and "3/20" was printed twice (D031).
- **Unrequested text is gibberish** (D029, D044).

## Failure modes

1. **Unusual traits revert to defaults**: the three-legged dog has four legs (D018), panther became leopard (D025), the pie-cut eyes are normal (D002), the crescent Earth is a globe (D033), and the baby was dropped (D036).
2. **Positions are ignored**: the fox is at the front window, not the back (D029). See also D010, D019, D003 and D001.
3. **Props split or duplicate** (D028, D006, D031).
4. **Lighting direction is weak** (D011), as in sets A, C and F.
5. **Few hand or limb errors** (D042, D049, D022). The anthropomorphic animals were all clean.

**SLG overblow is not systematic.** The clear cases are D049 (neon bloom) and D047 (orange cast), with mild muddiness in D041, and all three are tags prompts. The caption anime (D003, D004, D040) is saturated but controlled. This rests on 2-3 images.

## What correlated with success

- **Naming a medium's physical signs** (paper, ink, stitch, plate) beat naming a mood.
- **Length barely mattered.** 30 words or fewer: 4.09 (n=11, including all the tags prompts). 31-160 words: 4.29 (n=35). Over 160 words: 4.25 (n=4).
- **Per-panel captions with quoted dialogue** gave the best comics.

## Prompting advice

1. For comics, write one sentence per panel with its position and its quoted line. Don't use tags for layouts.
2. Quote every string. Name the speaker the tail points to, and check it.
3. For loose media, ask for the imperfection itself ("bare paper in the shadows"). Expect some tidying anyway.
4. For pixel art, plan to downscale and re-quantise. Whether resolution wording helps is untested.
5. State unusual traits early and plainly, and run seeds.
6. In multi-character scenes, bind attributes in prose. Dropping the stacked quality tags under SLG is untested (2-3 images).
