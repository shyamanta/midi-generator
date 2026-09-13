# MIDI Generator

A professional, browser-based MIDI composition generator that creates genre-aware musical parts with proper phrasing, harmony, and arrangement-ready exports.

## Features

- **15+ Genres:** Pop, EDM (8 sub-genres), Ambient, Hip-hop, Lo-fi, Cinematic, R&B, Rock
- **6 Musical Parts:** Melody, Harmony, Chords, Bass, Arpeggiator, Drums
- **Smart Composition:** Motif development, phrase structure, chord tone targeting, leap resolution
- **Unusual Chords:** Maj9, 7#11, quartal voicings, chromatic mediants, clusters
- **Individual Downloads:** Export each part as separate MIDI files
- **Folder Export:** Save all parts into organized folders with drums subfolder
- **Deterministic:** Seed-based RNG for reproducible compositions
- **Zero Dependencies:** Pure HTML/CSS/JavaScript, no server required

## Quick Start

1. Open `index.html` in any modern browser
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
| Harmony | Strings (48) | Simple counter-melody, contrary motion |
| Chords | Electric Piano (4) | Extended voicings, genre-specific |
| Bass | Fingered Bass (33) | Root-driven, genre patterns |
| Arpeggiator | Synth Lead (81) | Rhythmic chord sequence |
| Drums | GM Percussion (Ch.9) | Kick, snare, clap, hats, crash, ride |

## Roadmap

### Phase 1: Core (Complete)
- [x] Basic MIDI generation
- [x] Multiple genres with unique patterns
- [x] Melody with motif development
- [x] Harmony counter-melody
- [x] Extended chord voicings
- [x] Bass patterns per genre
- [x] Arpeggiator
- [x] Full drum kit
- [x] Individual track downloads
- [x] Folder export with subfolders
- [x] Seed-based reproducibility
- [x] Professional dark UI

### Phase 2: Enhanced Composition
- [ ] **Swing/Groove** — Add humanized timing with swing percentage
- [ ] **Velocity Curves** — More expressive dynamic shaping
- [ ] **Chord Progression Editor** — Custom progression input (I-V-vi-IV, etc.)
- [ ] **Scale Extensions** — Pentatonic, blues, whole tone, diminished, chromatic
- [ ] **Tempo Automation** — BPM changes within a composition
- [ ] **Time Signature** — 3/4, 6/8, 5/4 support

### Phase 3: Arrangement
- [ ] **Song Structure** — Intro, verse, chorus, bridge, outro templates
- [ ] **Section Markers** — Label and navigate sections
- [ ] **Arrangement View** — Visual timeline of all parts
- [ ] **Part Muting** — Toggle individual parts on/off
- [ ] **Volume Mixer** — Per-track volume control
- [ ] **Pan Control** — Stereo positioning per track

### Phase 4: Advanced Features
- [ ] **Undo/Redo** — History stack for edits
- [ ] **Preset System** — Save and load favorite configurations
- [ ] **Import MIDI** — Load existing MIDI files for reference
- [ ] **Quantization** — Snap notes to grid with configurable strength
- [ ] **Humanize** — Add random timing/velocity variation
- [ ] **Transposition** — Shift key without regenerating

### Phase 5: Collaboration & Export
- [ ] **Share Links** — URL-encoded settings for sharing
- [ ] **Export WAV** — Render audio using Web Audio API
- [ ] **Export PDF** — Sheet music notation
- [ ] **Collaborative Editing** — Real-time multi-user (WebSocket)
- [ ] **Version History** — Save and compare versions

### Phase 6: Desktop & Mobile
- [ ] **PWA Support** — Install as Progressive Web App
- [ ] **Offline Mode** — Full functionality without internet
- [ ] **Mobile Optimized** — Touch-friendly interface
- [ ] **Electron Wrapper** — Desktop app for Windows/Mac/Linux
- [ ] **Audio Preview** — Built-in synth for instant playback

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
