# MOSS-Image review, set E (text rendering, graphic design, layout)

50 images, 365 checks. Mean score **4.52** (5: 32, 4: 13, 3: 4, 2: 1). Checks: **92% pass**, 5% partial, 3% fail.
Standouts: E003, E007, E014, E019, E030, E034, E045, E048.

## String accuracy

**284 of 292** quoted strings were exact. The count is approximate: multi-line blocks count as one string. 6 of the 8 misses are spelling errors, all English.

- **1-3 words: 202/204.** Both misses are a label paired with the wrong value (E037).
- **4-10 words: 74/77.** "repliaca" (E012), "Blied" (E015), "KESTRL" on an arc (E021).
- **11-30 words: 7/8.** An inserted "BY" in the billing block (E036).
- **30+ words: 1/3.** The 8-line menu was exact (E004). The letter had two errors (E011). The 60-word book paragraph collapsed into pseudo-glyphs (E023).

Excluding E023 there were **9 character errors** in total. Continuous prose fails; volume alone does not (E014 got 14 strings right, E025 got 40). Accents were always right (Ê é Í Č É ¢).

## English vs Chinese vs bilingual

- **Chinese: 26/26 strings, 127/127 hanzi correct.** That covers neon (E031), brush couplets (E030), calligraphy (E027) and metro signage (E028). Mean 4.83 (n=6).
- **Bilingual: mean 4.75 (n=4).** Both scripts were correct, with the hierarchy as asked.
- **English: mean 4.45 (n=40).** It holds all the spelling errors, but also the hardest briefs.

## Line breaks

All 12 prompts with breaks had every requested break honoured. Extra breaks were sometimes added: "NO / PARKING" (E008), performer names wrapped in a narrow column (E001), and a ribbon line split in two (E005).

## Caption vs layout

- **Layout 5.00 (n=8, 98% checks) vs caption 4.43 (91%).** The layout briefs were easier types, so part of the gap is the task mix.
- **All 38 text items landed in their boxes**, typically within about 1.5% of the canvas, slightly inset.
- **The two partials were objects.** The lighthouse sits left in its box and its beam overflows (E043). The backpack spills to the canvas edge (E045).
- **No box was drawn as a border.**
- **One like-for-like pair:** the layout menu right-aligns its prices (E049), but the caption menu's prices float above their dishes (E004).

## Design types

**Strong:** covers (E002, E003, E044, E045), packaging (E006, E007), photoreal signage (E008, E028, E032, E041), tickets (E017), UI (E014, E046, E047), the comic cover (E019) and the labelled map (E018).

**Weak:** anything where the logic behind the strings matters.

## Failure modes

1. **Logic is ignored while the strings are correct.**
   - The calendar starts on the wrong weekday, and the birthday is on the wrong date (E024).
   - The colour groups snap to rows, and the legend is swapped (E025).
   - There are 7 flames, not 5 (E040).
   - A label is paired with the wrong value (E037).
2. **Long prose breaks** (E023 scored 2, E011 scored 3).
3. **Single-letter slips in small or curved text** (E012, E015, E021).
4. **Text attributes are dropped.** The OPEN card is not red (E009), and the double underline is single (E022).
5. **Occasional unrequested text.** There is a gibberish decal (E033), invented billing lines (E036), a status-bar blob (E047) and an unflipped sign "reflection" (E026). Both "no other text" prompts stayed clean (E020, E035).

## Prompting advice

1. **Quote every string and keep each under about 10 words.** Put body copy on short \n-separated lines. Short-line blocks are safe (E004, E029, E049); a 55-60 word paragraph is not (E011, E023).
2. **Use the JSON layout for multi-element designs.** Boxes are followed and never drawn. Size each text box to the extent you want filled.
3. **Don't delegate logic** (calendars, counts, legends). State each item explicitly or composite afterwards, then verify.
4. **Proofread small and curved text, and reroll on slips.** They look random.
5. **Chinese and accented Latin are reliable.** Name the script style and it is followed.
6. **"Nothing else carries text" suppressed filler** in both tries, but this rests on 2 images.
7. **Restate colours and decorations next to the string.** Attributes given in a separate clause were missed twice (E009, E022).
