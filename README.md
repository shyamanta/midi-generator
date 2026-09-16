# MIDI Generator

A professional, browser-based MIDI composition generator that creates genre-aware musical parts with proper phrasing, harmony, and arrangement-ready exports.

**Live Demo:** [https://shyamanta.github.io/midi-generator/](https://shyamanta.github.io/midi-generator/)

## Features

- **15+ Genres:** Pop, EDM (8 sub-genres), Ambient, Hip-hop, Lo-fi, Cinematic, R&B, Rock
- **6 Musical Parts:** Melody, Harmony, Chords, Bass, Arpeggiator, Drums
- **Smart Composition:** Motif development, phrase structure, chord tone targeting, leap resolution
- **Extended Voicings:** Maj9, 7#11, add9, sus4, quartal voicings, chromatic mediants
- **Individual Downloads:** Export each part as separate MIDI files
- **Folder Export:** Save all parts into organized folders with drums subfolder
- **Deterministic:** Seed-based RNG for reproducible compositions
- **Zero Dependencies:** Pure HTML/CSS/JavaScript, no server required

## Version 2 (index-v2.html)

Enhanced version with advanced composition features:

- **Swing/Groove** — Humanized timing with adjustable swing percentage
- **Velocity Curves** — Expressive dynamic shaping (linear, crescendo, decrescendo, swell)
- **45+ Chord Progressions** — Pre-built progressions organized by genre + custom input
- **Scale Extensions** — Pentatonic, blues, whole tone, diminished, chromatic
- **Tempo Automation** — BPM changes within a composition (start/end BPM)
- **Time Signatures** — 3/4, 4/4, 6/8, 5/4 support
- **Per-bar Melody Variation** — Different rhythm patterns per bar (not identical repeat)

## Quick Start

1. Open `index.html` (v1) or `index-v2.html` (v2) in any modern browser
2. Select genre, key, scale, tempo
3. Click **Generate Parts**
4. Download individual tracks or save all to folder

## Genres

| Genre | Sub-genres |
|-------|------------|
| Pop | - |
| EDM | House, Bass House, Progressive, Dubstep, Trance, Future Bass, Techno, Drum & Bass |
| Ambient | - |
| Hip-hop | - |
| Lo-fi | - |
| Cinematic | - |
| R&B / Soul | - |
| Rock | - |

## Musical Parts

| Part | MIDI Program | Description |
|------|--------------|-------------|
| Melody | Piano (0) | Lead with motif development, phrase structure |
| Harmony | Strings (48) | Counter-melody, contrary motion, leap limits |
| Chords | Electric Piano (4) | Extended voicings, genre-specific inversions |
| Bass | Fingered Bass (33) | Genre-specific: dotted 8th (EDM), walking (R&B), power (rock) |
| Arpeggiator | Synth Lead (81) | Rhythmic chord sequence |
| Pads | Synth Pad (89) | Sustained chord tones, ambient textures |
| Drums | GM Percussion (Ch.9) | Kick, snare, clap, hats, crash, ride |

## Python Backend

CLI tool using music21 for advanced MIDI generation:

```bash
# Interactive mode (double-click or run without args)
python generate.py

# Command line mode
python generate.py --style pop --key C --bars 8 --seed 42 --output output
```

## Research-Based Improvements

Chord progressions and patterns based on analysis of professional songs:

- **Pop:** I-V-vi-IV (Let It Be, Someone Like You), vi-IV-I-V (Zombie, Numb)
- **Hip-hop:** i-VI-III-VII (trap), i-VII-VI-VII (dark) — Travis Scott, J Cole
- **R&B:** I-vi-IV-V, walking bass — Alicia Keys, Daniel Caesar
- **EDM:** i-III-VII-VI (Avicii Levels), i-VI-iv (Calvin Harris)
- **Cinematic:** Chromatic mediants, Lydian mode, pedal tones — Hans Zimmer, John Williams
- **Rock:** I-IV-V-I, power chords — Led Zeppelin, Nirvana
- **Lo-fi:** ii-V-I (jazzy), swing timing

## Technical Details

- **Single HTML file** — No build step, no dependencies
- **Web MIDI API ready** — Can output to hardware MIDI devices
- **File System Access API** — Direct folder export in supported browsers
- **GM MIDI Standard** — Compatible with all DAWs and MIDI software

## Browser Support

- Chrome 86+ (full support)
- Edge 86+ (full support)
- Firefox 111+ (no folder export)
- Safari 15.4+ (no folder export)

## License

© 2026 Shyamanta. All Rights Reserved.

## Contributing

Contributions welcome! Please open an issue first to discuss changes.
