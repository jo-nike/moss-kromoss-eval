# Kromoss (8-step DMD) review, set E (text rendering, graphic design, layout)

50 images, 365 checks. Mean score **4.4** (5: 27, 4: 18, 3: 3, 2: 2). Checks: **91% pass**, 7% partial, 2% fail.
Requested strings: **245 of 268 exact** (91%). 65 character errors in total, 38 of them in E011.
Standouts: E007, E009, E014, E018, E029, E032, E043, E048.

## String accuracy by length

1-3 words: 165/174 (95%) · 4-10: 78/85 (92%) · 11-30: 2/4 · 30+: 0/5.

The 30+ bucket hides a split. E023's 55-word printed paragraph is word-perfect apart from a doubled drop-cap "T". E011's 60-word cursive letter falls apart after its first sentence ("can can", "cleaings, clee mornings", "Write soon" → "Woon"). The other three are menus and grids that failed on alignment, not spelling. With only two prose samples, handwriting is not proven to be the cause.

## English vs Chinese vs bilingual

- **English:** 205/225 exact, mean score 4.33 (n=40).
- **Chinese-only:** 21/23 exact, mean 4.67 (n=6).
- **Bilingual:** 19/20 exact, mean 4.75 (n=4).

Chinese glyphs were clean everywhere: neon (E031), carved wood (E029), brush (E030). Neither Chinese miss is a malformed glyph. E027 repeats a character (月圆圆人团圆), and E030 mixes traditional 滿/間 into simplified text. The samples are small.

## Line breaks

All 12 prompts with explicit `\n` were honoured. The errors go the other way, as **unrequested wraps**:
- a title asked to sit on one line was split (E002)
- every performer name was wrapped (E001)
- line 3 of the note was wrapped (E010)

"One line" was honoured in E039 and E044.

## Caption vs layout

Layout mean 4.75 (n=8) vs caption 4.33 (n=42). **Box adherence 8/8**: every item sat inside its box, typically within about 1% of the canvas. The worst offset was E048's title, 1.4% past the edge. No box was drawn as a visible border. The layout prompts were also simpler designs, so format and difficulty are confounded.

## Design types

**Strong:**
- packaging (E005-E007, E040)
- signage (E008, E009, E032, E041)
- UI screens (E014, E046, E047)
- covers and posters (E003, E039, E043-E045)
- maps (E018)

**Weak: row and column registration.**
- E024's calendar repeats and skips dates, and puts both notes on the wrong day.
- E004's prices drift half a row from their dishes.
- E037 shifts its field labels by one slot ("Arr 2vr").
- E025 ignores the colour-by-index ranges.
- E049 breaks its dot leaders into fragments.

## Failure modes

1. **Grid and table misregistration** (E004, E024, E037, E025, E049). This cost the most points.
2. **Small unrequested insertions:**
   - ™ (E005)
   - quote marks (E019)
   - an extra "STARRING" and pseudo-credits (E036)
   - a repeated character (E027)
   - a doubled drop cap (E023)
   - a full-width comma (E034)
3. **Per-line styling ignored:** E008's size and colour split, "v2"→"V2" (E012), caps (E019).
4. **Text colliding with objects:** a stray shape over the performer list (E001), a magnet over the "G" (E010).
5. **Long cursive prose degrades** (E011).

Unrequested gibberish was rare (E036 credits, E023 show-through). Diacritics were all correct (E007, E016, E039, E049).

## Prompting advice

1. Quote every string. Strings of up to about 10 words are about 93% exact in either script.
2. Use explicit `\n` for line breaks (12/12 honoured). "On one line" is usually honoured, but not always (E002).
3. Write each table row as one self-contained string ("Tiramisu 11"). Don't rely on separate price columns or calendar grids (E004, E024; the calendar rests on one image).
4. Use JSON layout when position matters: 8/8 boxes respected, with no border artifacts.
5. Describe dot leaders in words rather than typing "...." (E049; untested).
6. Prefer printed type for paragraphs over about 30 words, and proofread them (E023 vs E011, n=2).
7. Say "no other text" where exactness matters. It worked in E020 and E035.
8. Specify "simplified characters" for Chinese (E030).
