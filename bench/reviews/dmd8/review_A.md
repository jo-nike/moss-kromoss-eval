# Kromoss DMD-8: set A (people, portraits, anatomy)

**Mean score 3.70** across 50 images (5: 6, 4: 28, 3: 11, 2: 5). **Checks: 214 of 303 pass (70.6%)**, 70 partial, 19 fail. Nothing was broken, but strict instruction-following trails the image quality.

## Pass rate by check type (keyword-bucketed, approximate)

| Type | n | Pass | Fails |
|---|---|---|---|
| Mirrors/reflections | 14 | 50% | A022 |
| Lighting/physics | 18 | 61% | A033, A050 |
| Medium details | 16 | 62% | none |
| Digit/limb counts | 39 | 64% | A007, A014, A031, A038 |
| Body pose/viewpoint | 45 | 67% | A050 |
| Hand pose/role | 42 | 69% | A026, A032, A037, A048 |
| Expression/age | 26 | 73% | A003 |
| Props/clothing/setting | 99 | 81% | A044 |

## Common failure modes

1. **Specific hand shapes snap to a familiar gesture.** "Three fingers" became a peace sign (A007) and ASL "I love you" became the horns sign (A038). The G chord (A005), the octave span (A037) and the mixed grip (A032) were all ignored. Simple, natural hands are reliable (A009, A015, A043, A049).
2. **Extra digits or hands when the hand is the subject:** six digits (A014), a third hand (A031).
3. **Left/right roles swapped or dropped:** A026, A048, and ambiguously A040.
4. **No mirror geometry.** In A022 the lipstick hand flips side, and in A024 the reflections are three independent copies. Surface reflections work: glasses (A021), lens (A045), infinity mirror (A044).
5. **Peak action falls back to a canonical static pose:** A050 (the ollie never leaves the ground), A011, A032, A012, and upright flames in A033. A010 (grand jeté) is a notable success.
6. **Small attributes are dropped:** a single raised eyebrow and low glasses (A003), a ring (A006), a sticker (A044). Ages drift (A003, A007, A029).

## What correlated with success

- **Length:** neutral. Prompts under 30 words averaged 4.0 (n=6), and so did prompts over 300 words (n=4). Short prompts scored 5 when the content was generic (A015, A023, A039, A046) and failed when they hinged on one count (A007, A031). The 340-word prompts held up well (A010, A025, A036, A048).
- **Positional phrases** for layout were almost always honoured (A009, A020, A036). Light direction on a face was weaker (A001). These were not tallied separately.
- **Illustrated vs photo:** 3.86 (n=7) vs 3.67 (n=43). Vector and gouache were strong (A016, A042). Texture words (craquelure, hatching, underdrawing) came out faint. The illustrated sample is small.
- **Hand descriptions** worked for natural grips (A008, A036) and failed for exact counts or named shapes.

## Advice

- Don't rely on finger counts or named signs. Describe what the hand looks like and expect to try several seeds. The rewording is untested.
- Avoid extreme hand foreshortening when anatomy matters (A014).
- For mirror scenes, show only the reflection (A044) rather than body plus reflection (A022, A024).
- For peak action, ask for visible proof, such as a clear gap under the board, and budget for retries.
- Give each hand one simple job, and verify left and right.
- Long, detailed prompts are safe. Props and setting pass 81%.
- Reinforce age with body cues. This rests on 3 images.
