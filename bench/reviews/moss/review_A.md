# MOSS-Image review, set A (people and anatomy)

50 images, 303 checks. Mean score **4.0** (5: 13, 4: 27, 3: 7, 2: 3). Checks: **78% pass**, 15% partial, 7% fail.
Standouts: A002, A014, A028, A029, A031, A035, A036, A046.

## Pass rate by check type

Attire 100% (n=28) · subject traits 97% (32) · camera 91% (11) · setting 90% (20) · props 81% (53) · expression 75% (16) · style 75% (12) · pose 73% (30) · hands 71% (59) · lighting direction 55% (11) · physics/reflections 50% (20) · left/right 38% (8) · requested text 100% (3)

## Failure modes

1. **Named gestures and techniques become a generic version.** This explains most of the 2s and 3s:
   - the ASL "I love you" became a "4" (A038)
   - "three fingers" came out with about six digits (A007)
   - the G chord is unplayable (A005)
   - the mixed deadlift grip is double overhand (A032)
   - Warrior III became a leg lift (A012)
   - the ollie's feet float above the board (A050)
   - the one-raised-eyebrow look became a frown (A003)
2. **Left/right is unreliable.** Hands were swapped in A004, A049 and A050. Details landed on the wrong side in A001 (upper teeth instead of lower), A017 and A049.
3. **Physics and optics are approximate.** The three-way mirror shows three front views (A024). The two lens reflections differ (A021), the flames do not bend (A033), the skirt has no motion blur (A047), the loom geometry is wrong (A042), and the elevator reflections show her front (A044). One simple mirror worked (A022).
4. **Repeating structures break.** The piano has no 2/3 black-key grouping (A037). Some keycaps are garbled (A009).
5. **Limbs at the frame edge degrade.** A015 has a malformed hand, and A034 has a stretched infant torso.
6. **Lighting is only half followed.** The light comes from the stated side, but the requested shadow side or rim light is weak (A001, A019, A021).

Digit counts were right in about 45 of 50 images, including hard cases (A014, A017, A036, A044).

## What correlated with success

- **Length barely mattered.** Prompts of 30 words or fewer: mean 4.17 (n=6). Prompts of 90-200 words: 3.95 (n=40). Prompts over 300 words: 4.25 (n=4). A036 met 8 of 8 requirements at 340 words, while A031 and A046 were standouts at 23 words. The short and long buckets are small.
- **Illustration beat photoreal:** 4.57 vs 3.91. The medium was always honoured. Only 7 images were illustrated.
- **Attributes beat relations.** Clothing, age and props almost always land. Which hand, which side, and where a reflection or shadow falls fail most.
- **Hand-focused prompts were weakest** (mean 3.29, n=7). Generic hand actions worked (A006, A009, A041). Specific symbolic or technical shapes failed (A005, A037, A038).
- **Quoted text rendered** in all 3 cases: "417", "100" and "R. OKAFOR / RN" (comma dropped). Unrequested background text is gibberish. Only 3 images tested this.

## Prompting advice

1. Describe the visible finger and limb geometry, not the name of a gesture. This is untested here; the evidence only shows that names fail.
2. Don't depend on left/right. Anchor to the frame ("nearest the camera", "on the image's right"), or expect a coin flip.
3. If a shot depends on a mirror, reflection or physics detail, run several seeds.
4. Keep key hands and limbs away from the frame edges.
5. Long, dense prompts are fine for listing what is in the scene. State the critical requirement early and plainly.
6. Keep quoted text short. Expect punctuation to drop.
7. Avoid piano keys and keyboards where correctness matters.
