# Kromoss review, set B (groups, counting, interaction, crowds)

50 images, 301 checks. Mean score **3.94** (5: 12, 4: 25, 3: 11, 2: 2). Checks: **76% pass**, 16% partial, 8% fail.
Standouts: B001, B004, B005, B020, B022, B036, B048, B050.

## Pass rate by check type

Requested text 100% (n=16) · position/order 90% (52) · setting/style/props 85% (46) · attributes 84% (31) · counts 70% (61) · hands/anatomy/faces 68% (38) · interactions/actions 58% (57)

## Count accuracy (exact, 63 counted quantities)

2: 11/12 · 3: 15/15 · 4: 11/16 · 5: 6/7 · 6: 4/7 · 7: 2/3 · larger: 1/3. Overall 79%.
Digits 10/14 (71%) vs words 40/49 (82%), but confounded: the digit misses are the egg carton (B033) and ducklings (B021), while people and balloons were perfect (B036, B042). No evidence either way.

## Failure modes

1. **Off-by-one extras at the frame edge or in a row.** 6 of 13 count misses are exactly +1: a fifth band member (B007), a seventh duckling (B021), a third rabbit (B026), a fifth bar (B029), a fifth child (B034), a sixth middle-row singer (B041). Undercounts were rarer (B006, B015 towers, B030).
2. **Structured objects ignore the stated count.** The carton has 18 cups and 11 brown eggs (B033). The "six elites" front row is a 15-wide pack (B039).
3. **Interactions become a generic version.** The arm-wrestle grip is a knot and nobody is losing (B010). Oars run along the hull (B044). The spiker misses the ball (B027). The tango hold is a plain dip (B013). The hug goes to the shoulders, not the waist (B014). The nibbling goat is dropped (B038).
4. **Secondary vignettes get approximated:** wrong hat (B016), dolphin for penguin (B040), one ice-cream cone (B017).
5. **Mirrors and stray parts.** The stylist's reflection is a different person (B023). Also a floating wine glass (B008), an unowned hand (B010) and a second hockey stick (B031).

## What correlated with success

- **Binding attributes to many people is the strength.** Seven people in the specified order with no leakage worked twice (B005, B022), and five worked once (B004). No clothing colour was swapped anywhere in the set. Position checks passed 90%. Body-relative sides still slipped: the dog in B009, the baton hand in B041.
- **Long prompts did well:** over 300 words averaged 4.5 (n=4). 90-170 words averaged 3.9 (n=41), and 30 words or fewer averaged 3.8 (n=5).
- **Text is reliable:** 16/16, including "CAFÉ LUNA" with its accent, "SKEWERS 3 FOR 10" and "NEXT TRAIN 2 MIN". Unrequested background text is gibberish (B015, B032).
- **Illustration slightly beat photo:** 4.14 (n=7) vs 3.91 (n=43). The medium was always honoured.
- **Sports and physical contact were weakest.** Sports prompts averaged 3.4 (B011, B015, B027, B030-B032, B039, B044). Static ordered groups averaged 4.6.

## Prompting advice

1. Describe a group as an ordered list with one distinctive colour or garment per person. The model binds this well.
2. Expect a stray extra person or object at the edges. Say "only N people, nothing else in the frame" (untested here). Otherwise, check the count and regenerate.
3. For grids and containers (cartons, choir rows, desks), give the total and the structure. Even then, expect failures and run several seeds. The evidence is 3 images (B006, B033, B041).
4. Avoid depending on a precise grip, contact point or sports mechanic. Make the main action the point of the prompt and accept a generic version of anything else.
5. Quoted text is safe to rely on, including several signs in one scene.
6. For mirror shots, plan to reroll (only 1 image).
