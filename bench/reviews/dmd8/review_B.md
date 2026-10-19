# Kromoss DMD-8 review, set B (groups, counting, interaction, crowds)

50 images, 301 checks. Mean score **3.94** (5: 17, 4: 16, 3: 14, 2: 3). Checks: **78% pass**, 15% partial, 8% fail.
Standouts: B001, B005, B018, B022, B036, B043, B048, B050.

## Pass rate by check type

Scene/style/physics 92% (n=39) · text 88% (17) · position/order 82% (61) · anatomy/faces 81% (32) · attributes 80% (35) · counts 69% (62) · interaction/action 65% (55)

## Exact-count accuracy

48 of 67 counted items were exact (72%). By requested number: 2: 13/16 · 3: 8/13 · 4: 13/18 · 5: 5/7 · 6: 4/7 · 7: 2/3 · 8+: 3/3 (9 balloons, 12 cups, 15 singers). Size barely predicts accuracy; what is counted does:
- **Individually described people: about 25 of 27 right**, up to 7 (B005, B022) and 15 (B041). The misses were B007 (an extra bandmate) and B023 (an extra man in the mirror).
- **Generic groups of people: 3 of 9 right.** B006 6→7, B010 3→4, B012 2→4, B017 5→4, B039 6→~14, and B049 2→4 (the whole scene duplicated).
- **Objects: 12 of 22.** Uniform piles fail: apples and pears (B002), eggs (B033), candles (B034), bars (B029), geraniums (B050). Items split by colour or owner succeed (B025, B035, B036, B042).
- **Errors are mostly overcounts:** 16 too many, 3 too few.
- **Digits vs words:** 10/13 (77%) vs 38/54 (70%). No real difference: only 5 prompts, and the 3 misses were uniform objects.

## Failure modes

1. **Physical force and support become a pose.** Nothing holds the piggybacked girl up (B009), the tango dip is missing (B013), and neither arm wrestler is losing (B010). Also missed: the slide tackle (B011), spike contact (B027) and the shared oar (B026). Light contact works: hugging (B014), holding hands (B024, B040), pouring (B028), the high five (B012).
2. **Unrequested extra people** appear in 8 images (B006, B007, B010, B012, B023, B032, B039, B049).
3. **Body-side handedness is still unreliable**, as in set A (B001, B010, B013). Position in the frame is reliable: every left-to-right order of 4-7 people was correct (B004, B005, B019, B022, B036, B037, B042, B046).
4. **Relational prepositions loosen.** The dachshund lies on the blanket, not under it (B020). The doubles roles are swapped (B032), and all four oars are on one side (B044).
5. **Secondary or edge text drops.** The banner is blank (B042), "10" is cut off (B017), and the sign appears twice (B016). Primary text was exact, including the accent in "CAFÉ LUNA".

Attribute binding was strong: no clothing colour leaked between people.

## What correlated with success

- **Length didn't matter.** Under 30 words: 4.0 (n=5). 100-160: 3.86 (n=36). Over 300: 4.25 (n=4), including B050's ten vignettes.
- **Illustration beat photoreal: 4.57 vs 3.84**, the same gap as set A. Only 7 images were illustrated.
- **Short prompts with a bare count of generic people failed** (B012, B049). Short prompts about objects or teams were exact (B021, B035, B046). This rests on two failures.

## Prompting advice

1. Give every counted person a distinct description and a frame position. This is the strongest count lever in the data.
2. Split object counts by colour or owner ("3 red, 3 blue, 3 yellow"), not "N identical things".
3. Expect overshoot on bare counts. Run several seeds rather than rewording.
4. Describe the visible result of a physical action, not the move's name. This is untested; the evidence only shows that named moves fail.
5. Anchor sides to the frame, not the body.
6. Put critical text on the main object, large and away from the edges.
