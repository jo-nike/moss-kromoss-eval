# Kromoss set A review (people, portraits, anatomy)

50 images, 303 checks. Mean score **3.90** (scores of 5: 9, 4: 28, 3: 12, 2: 1). Checks: **74% pass**, 20% partial, 5% fail.

## Pass rate by check type (keyword buckets, overlapping)

| Type | n | pass | fail |
|---|---|---|---|
| Props, wardrobe, setting | 144 | 84% | 2% |
| Art medium/style | 13 | 92% | 0% |
| Expression | 18 | 78% | 0% |
| Limbs, feet, gross pose | 49 | 73% | 2% |
| Hands, fingers, grips | 74 | 59% | 15% |
| Left/right assignment | 43 | 53% | 12% |
| Lighting direction, shadows | 18 | 56% | 11% |

Text (3 prompts): "100" exact (A033); "R. OKAFOR, RN" lost its comma (A043); "417" partly occluded (A011). Unrequested text is gibberish (A045 "COEM").

## Common failure modes

1. **Named hand configurations.** Finger counts are usually right; the hand shapes are not. ASL "I love you" came out as an F/OK sign (A038). The "three fingers" hand has only 4 digits (A007). The rest: no G chord (A005), no octave span (A037), no mixed grip (A032), tattoo machine held needle-up (A020). Stray or deformed digits: A044, A048.
2. **Left/right swaps.** A004, A016, A026, and the ring on the wrong hand in A006.
3. **Contact physics.** The umbrella has no shaft (A023), candle flames stay upright while she blows (A033), a hand sits in the wok instead of on the handle (A026), and a phantom shadow falls in an empty spotlight (A010).
4. **Secondary lighting dropped.** Monitor blue key (A021), long backlit shadow (A012), lens flare (A019), half-face shadow (A001).
5. **Fine sports mechanics.** No heel hook (A040), tilted ollie board (A050), deadlift not at lockout (A032). Gross poses are strong: jeté, Warrior III, handstand, sprint (A010-A013).

## Correlations

- **Length did not hurt.** The four ~340-word prompts averaged 4.25 (A010, A025, A036, A048) and their prop lists were nearly complete. The six sub-30-word prompts averaged 3.83, with A039 and A046 both scoring 5. Both groups are small (4 and 6 prompts).
- **Illustrated media are reliable.** Medium adherence was 12/13, and illustrations averaged 4.0 against 3.88 for photos. Anatomy degrades in loose styles (A030 body, A031 tool logic).
- **"hands:" prompts are weakest.** They averaged 3.56 with 13% fails. Relaxed or static hands look excellent (A041, A006, A049, A028). Hands performing a precise named action fail.
- **Mirrors do surprisingly well.** A022, A024 and A044 all scored 4, though glasses reflections didn't match between lenses (A021). Only 4 images, so treat this as tentative.

## Prompting advice

- Describe gestures by their visible geometry ("index and middle raised in a V, others curled"), not by name (ASL, chord names). Expect to inpaint. Evidence: A005, A007, A038.
- Don't depend on left/right. Anchor actions to frame position or objects. Evidence: A004, A016, A026.
- State physical links explicitly (umbrella shaft in hand, hand on wok handle), and verify them in the output. Evidence: A023, A026.
- Long, inventory-style captions are safe. Treat secondary light effects as likely to be dropped. Evidence: A012, A019, A021.
- For art media, name the medium plus 2-3 material traits (craquelure, pencil underdrawing, toned paper). Evidence: A028, A029, A046.

Standouts: A002, A018, A028, A036, A041, A046, A047, A049.
