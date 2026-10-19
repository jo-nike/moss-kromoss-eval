# MOSS-Image review, set F (lighting, technique, products, food, animals, weather, materials)

50 images, 302 checks. Mean score **4.1** (5: 16, 4: 26, 3: 7, 2: 1). Checks: **82% pass**, 14% partial, 5% fail.
Standouts: F003, F007, F015, F017, F018, F024, F029, F048.

## Pass rate by check type

Depth of field 100% (n=16) · motion/long exposure 100% (14) · requested text 100% (4) · objects and placement 88% (96) · animals 85% (20) · film/lens effects 85% (26) · materials 84% (45) · weather 76% (17) · lighting direction and shadows 64% (59) · named lighting pattern 20% (5)

## Failure modes

1. **The light source lands on the requested side, but the subject is lit evenly anyway.**
   - Backlit subjects get a contradicting front fill (F006, F037, F047, F036).
   - Light stops at the subject: blind stripes miss the man (F013), the neon lights nothing (F010), the farmhouse is front-lit, not silhouetted (F012).
   - Cast shadows go missing (F016, F005, F006), and one candle lights a whole kitchen (F009).
2. **Named lighting patterns are approximated or drawn as objects.** Butterfly lighting became a glowing white heart under the nose (F004, the only 2). The Rembrandt triangle sits by the ear (F001). Split light is a straight mask that also splits the backdrop (F002). Rim light worked (F003). Only 5 checks.
3. **Figurative wording renders literally.** "Like handprints" drew hand prints on the velvet (F044), and "butterfly-shaped shadow" drew a butterfly-shaped light (F004). Two images.
4. **Event physics break while surfaces look right.** The strawberry floats above the milk line (F049); the ring's shadow has no hole (F014).
5. **Named sub-types fall back to defaults.** Beech became birch (F042), the helter-skelter a tent (F021), the tri-spoke wheel spoked (F019) and the carton a bottle (F050).
6. **Directions flip.** Snow slants the wrong way (F038), and the collie is on the girl's left instead of her right (F006).

## What worked

- **Camera technique had no failed checks.** Focus on the named third jar (F017), light trails (F018), panning (F019), tilt-shift (F021), macro (F020).
- **Materials read physically correct**: soap film (F048), ice (F046), crystal (F029), brushed metal (F043), wet asphalt (F045), knit and suede (F030).
- **Genre looks land**: infrared (F025), flash snapshot (F024), double exposure (F023).
- **All 9 animals had clean anatomy.** The misses were pose (F020, F034).
- **All 4 quoted strings were exact**: "18", "AUTOMATIC", "NOCTURNE", "3:07". Unasked text is gibberish (F028).

## What correlated with success

- **Category mattered more than length.**
  - Products and food: 4.67 (n=3 each)
  - Materials: 4.38
  - Technique: 4.36
  - Lighting setups: 3.81 (n=16)
  - Weather: 3.80 (n=5)
- **Length barely mattered.** 30 words or fewer: 4.0 (n=6). 31-160: 4.24 (n=37). Over 160: 3.71 (n=7), mostly multi-source lighting scenes, so confounded with category.
- **Light acting on the environment landed; light acting on the subject failed.** God rays (F015), trails (F018) and water reflections (F007) worked. Stripes on a shirt (F013) and neon on a face (F010) did not.

## Prompting advice

1. Describe the visible result, not the pattern name ("a small dark shadow under the nose"). Untested; the evidence only shows names fail.
2. Avoid similes and shape metaphors. They become objects.
3. For backlight, state the consequence ("her face is darker than the sky"). Still expect fill; run several seeds.
4. Name the body parts a light pattern must cross. Otherwise the default is that it lands only on the wall.
5. Request cast shadows explicitly, with direction, and check them.
6. Spell out uncommon sub-types (beech bark, tri-spoke wheel).
