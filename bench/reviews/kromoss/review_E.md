# Kromoss review, set E (text rendering, graphic design, layout)

50 images, 365 checks. Mean score **4.36** (5: 26, 4: 18, 3: 4, 2: 2). Checks: **89% pass**, 7% partial, 4% fail.
Requested strings: **289 of 301 exact (96%)**.
Standouts: E003, E007, E011, E019, E029, E030, E034, E045.

## String accuracy by length

1-3 words 203/209 (97%) · 4-10 words 83/88 (94%) · 11-30 words 2/2 · 30+ words 1/2

- 30+ words split: the 55-word handwritten letter was exact (E011); the 55-word book paragraph became pseudo-glyphs after about 40 words, ❦ garbled (E023). Two cases only.
- Short and medium misses are single letters: KESSTREL (E021), STEAMSHIPE (E039), "Lake Bed" (E015), Ciabatte (E025), "Latency" (E012), probably "Cull" (E018). All diacritics were right (E007, E016, E039, E049).

## English vs Chinese vs bilingual

- English (n=40): 248/259 exact, mean 4.30.
- Chinese only (n=6): 21/22, mean 4.50. **No wrong or invented characters.** Brush calligraphy, carved type, neon and vertical text were all correct (E027, E029, E030, E031). The one miss is order, not glyphs: "换乘 12号线" was split around the number (E028).
- Bilingual (n=4): 20/20, mean 4.75 (E032, E033, E034, E048).

## Line breaks

All 12 prompts with explicit `\n` kept the breaks. The opposite is common: **the model adds unrequested wraps**: a title asked for on one line (E002), performer names (E001), a note line (E010), a card name (E016). A long title held one line inside a wide layout box (E044).

## Caption vs layout

- Layout (n=8): mean **4.88**, 98% of checks passed, 48/48 strings exact.
- Caption (n=42): mean 4.26, 88% of checks passed.
- **Box adherence was 49/49 items.** Typical offset was ≤0.01-0.02 of the canvas on each edge. The worst was E047's second card, which ran about 0.01 past its box.
- No boxes drawn as borders. One extra sailboat (E043).
- Caveat: layout prompts were also simpler flat designs, so format and difficulty are confounded.

## Design types

- **Strong:** packaging (E005-E007), signage (E008, E032, E041), covers (E003, E044, E045), UI (E046, E047), Chinese calligraphy and posters, usually with professional hierarchy.
- **Weak:** anything where the model has to compute or bind data rather than copy a string:
  - The calendar started on Thursday, and both notes landed on the wrong dates (E024).
  - Colour groups followed rows, not the requested ranges (E025).
  - "Four of five flames filled" came out as all five (E040).
  - Prices drifted off their menu lines (E004).

## Failure modes

1. **Computed or structured content is wrong while the text is right** (E024, E025, E040, E004). This explains most of the 2s and 3s.
2. **Long body copy collapses** (E023). The handwritten letter survived (E011).
3. **One-letter typos in medium strings** (E021, E039, E015, E025).
4. **Small secondary text degrades.** The air-quality "32" was dropped (E014), the ticket serial is illegible (E017), and the billing block ends in "TALLGRASS VFLSIT ULATURES" plus two gibberish lines (E036).
5. **Size ratios and object details are approximate.** The headline is not 2:1 (E001), the bassist is a blob (E001), the spoon is doubled (E005), the key stands instead of hangs (E002), and the red neon became a lightbox (E031).
6. **Unrequested gibberish was rare** (E017, E035, E036).

## Prompting advice

1. **Use the JSON layout whenever placement matters.** Boxes were followed to within about 1-2% here.
2. **Keep each string to about 10 words or fewer.** Split body copy into several items. A single printed paragraph over about 40 words is risky (1 failure, 1 success).
3. **Don't ask the model to derive structure.** Spell out calendar cells, per-tile colours and filled-vs-empty counts item by item, or composite them afterwards.
4. **Give a one-line string a box wide enough for one line.** In prose, "on one line" was ignored (E002).
5. **Put numbers in their own item or quote** when they sit next to other text (E028, E014).
6. **Proofread medium strings for one-letter slips** and reroll; they looked random.
7. **Keep billing blocks and fine print short.** Long runs of condensed small capitals invite gibberish (E036).
