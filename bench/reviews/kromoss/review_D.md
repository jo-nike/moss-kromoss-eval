# Kromoss review, set D (cartoon, anime and art-style range)

50 images, 296 checks. Mean score **4.3** (5: 23, 4: 19, 3: 7, 2: 1). Checks: **85% pass**, 14% partial, 1% fail.
Standouts: D003, D006, D008, D013, D020, D035, D037, D042.

## Style fidelity by family

Craft/3D 4.5 (n=8) · print/graphic 4.42 (12) · painting/drawing 4.33 (9) · cartoon/comic 4.25 (4) · anime from captions 4.0 (5) · **pixel art and flat vector 3.0 (5)**

- **Period and physical media land.** Art nouveau (D013), ukiyo-e (D012), stained glass (D020), manuscript (D035), embroidery (D021) and 90s cel (D004, D042) avoid a generic digital look. The crayon drawing stays naive (D036).
- **Pixel art and flat vector get the surface right but the content collapses.** D015's frog knight is human, D030's cat is awake among stray sprites, D045's knight is a speck in a black frame, and D034 repeats one cloud nine times.
- **SLG over-bloom was rare.** Only D049's cyan centre is near blown (no no-SLG control).

## Caption vs tags

Tags scored 4.7 (n=10, 98% pass) and captions 4.17 (n=40, 82%). This is confounded: tag prompts had simpler checks on anime subjects. In same-style pairs, tags won for 90s cel (D004 4 vs D042 5) and chibi (D005 3 vs D043 5). They tied for manga (D006/D044, both 4), modern anime (D003/D041, both 5) and pixel art (3s throughout). Tags bound three hair colours to three props correctly (D049), and they overrode the cel default for watercolour (D046) and graphite (D048).

## Multi-panel and text

- **Panel counts were exact in 3 of 3 specified layouts.** D006 has 5 panels in the requested right-to-left order; D008 and D040 have 4 each. The cast stays consistent across panels.
- **Quoted strings were exact in 53 of 56**, including "LUMIÈRE", "CAFÉ" and "PARIS · 1897".
- The misses: "finished et!" (D040), SKRRT read as roughly "SKARRT" (D006), and a title cropped at "MK" (D027).
- Unquoted bubbles fill with gibberish (D044).

## Failure modes

1. **Deliberate anomalies revert.** The dog has four legs, not three (D018). The pie-cut eyes are ordinary (D002), the frog knight is human (D015) and the tanuki is unreadable (D012).
2. **Attributes bind to the wrong character or prop.** Beard and hijab are shuffled (D024), the wrench is in the wrong hand (D014), and the candle is fused onto the panther (D025). Also D028, D029.
3. **Short captions underdeliver.** Captions of 30 words or fewer averaged 3.0 (n=5). D023's hands and watch are malformed (score 2), and D005's chibi face is a void mask.
4. **Light direction is weak** (D011, D022).
5. **Literal rendering.** "Fingerprint marks" became inked prints (D038). One image only.

## What correlated with success

- **Length helped captions.** 30 words or fewer: 3.0 (n=5). 31-160: 4.4 (n=35). Over 160: 4.5 (n=4).
- **Naming the medium's physical traits** (gouge marks, lead lines) produced the most convincing images.
- **Composition notes mattered.** D045 had 16 tags and no framing, and the subject vanished. This is one image.

## Prompting advice

1. Write 80+ word captions for non-anime styles, and describe the medium's physical traits.
2. For anime characters, tags work at least as well as prose. Add a framing tag so the subject fills the frame (tested on D045 only).
3. Quote every line of dialogue. Proofread the first bubble.
4. State the panel count, reading order and each panel's position.
5. Expect unusual traits to revert. Restating them is untested; run seeds.
6. Avoid pixel art and icon sets where accuracy matters (n=5).
7. Put each character's attributes in one sentence of their own.
