#!/usr/bin/env python3
"""
MIDI Generator - Python backend using music21
Generates professional MIDI files with advanced music theory.
"""
import sys, os, random, argparse
from music21 import stream, note, chord, tempo, meter, key, instrument, metadata, interval

GENRES = {
    "pop": {"prog": ["I","V","vi","IV"], "scale": "major", "ext": "add9", "tempo": 120,
            "melody_range": (60,84), "chord_tone": .8, "step": .75, "contour": "arch"},
    "hiphop": {"prog": ["i","III","VII","VI"], "scale": "minor", "ext": "m7", "tempo": 90,
               "melody_range": (48,76), "chord_tone": .4, "step": .55, "contour": "flat"},
    "rnb": {"prog": ["I","vi","IV","V"], "scale": "major", "ext": "maj9", "tempo": 85,
            "melody_range": (55,84), "chord_tone": .7, "step": .72, "contour": "wave"},
    "ambient": {"prog": ["I","vi","IV","V"], "scale": "major", "ext": "sus4", "tempo": 70,
                "melody_range": (48,72), "chord_tone": .88, "step": .9, "contour": "flat"},
    "rock": {"prog": ["I","IV","V","IV"], "scale": "major", "ext": "power", "tempo": 130,
             "melody_range": (48,79), "chord_tone": .65, "step": .58, "contour": "arch"},
    "lofi": {"prog": ["ii","V","I","VI"], "scale": "major", "ext": "maj7", "tempo": 80,
             "melody_range": (55,72), "chord_tone": .78, "step": .82, "contour": "flat"},
    "cinematic": {"prog": ["I","vi","IV","V"], "scale": "major", "ext": "maj7#11", "tempo": 75,
                  "melody_range": (40,84), "chord_tone": .72, "step": .7, "contour": "dramatic"},
    "house": {"prog": ["I","vi","ii","V"], "scale": "major", "ext": "dom7", "tempo": 128,
              "melody_range": (60,84), "chord_tone": .76, "step": .72, "contour": "build"},
    "trance": {"prog": ["I","vi","ii","V"], "scale": "major", "ext": "maj9", "tempo": 138,
               "melody_range": (60,84), "chord_tone": .86, "step": .82, "contour": "build"},
    "techno": {"prog": ["i","II","III","iv"], "scale": "minor", "ext": "dom7", "tempo": 135,
               "melody_range": (55,79), "chord_tone": .65, "step": .6, "contour": "flat"},
    "dnb": {"prog": ["i","VI","III","VII"], "scale": "minor", "ext": "dom7", "tempo": 174,
            "melody_range": (60,84), "chord_tone": .72, "step": .68, "contour": "build"},
}

RHYTHM_POOLS = [
    [4,2,2,4,2,2], [2,2,4,2,2,4], [4,4,2,2,4], [6,2,4,2,2],
    [3,3,2,2,2,4], [2,2,2,4,2,4], [4,2,4,2,2,2], [6,2,2,2,2,4],
    [8,4,4], [10,4,2], [4,2,2,2,4,2], [2,4,4,2,2,4],
]

ROMAN_TO_SEMITONE = {
    "I":0, "II":2, "III":4, "IV":5, "V":7, "VI":9, "VII":11,
    "i":0, "ii":2, "iii":4, "iv":5, "v":7, "vi":9, "vii":11,
}

def snap_to_scale(midi_note, scale_pitches):
    pc = midi_note % 12
    best = min(scale_pitches, key=lambda s: min(abs(pc-s), 12-abs(pc-s)))
    octave = midi_note - pc
    return octave + best

def make_scale(root_pc, scale_name):
    intervals = {"major":[0,2,4,5,7,9,11], "minor":[0,2,3,5,7,8,10],
                 "dorian":[0,2,3,5,7,9,10], "mixolydian":[0,2,4,5,7,9,10]}
    return [(root_pc + i) % 12 for i in intervals.get(scale_name, intervals["major"])]

def build_chord(root_midi, ext, scale_pitches):
    notes = [root_midi, root_midi+4, root_midi+7]
    if ext == "add9": notes.append(root_midi+14)
    elif ext == "m7": notes[1] = root_midi+3; notes.append(root_midi+10)
    elif ext == "maj9": notes.append(root_midi+11); notes.append(root_midi+14)
    elif ext == "maj7": notes.append(root_midi+11)
    elif ext == "sus4": notes[1] = root_midi+5; notes.append(root_midi+10)
    elif ext == "maj7#11": notes.append(root_midi+11); notes.append(root_midi+17)
    elif ext == "power": notes = [root_midi, root_midi+7, root_midi+12]
    elif ext == "dom7": notes.append(root_midi+10)
    elif ext == "7sus4": notes[1] = root_midi+5; notes.append(root_midi+10)
    return notes

def generate_melody(scale_pitches, profile, bars, rng, base_octave=60):
    s = stream.Stream()
    pos = 0.0
    prev = base_octave
    for bar in range(bars):
        rhy = rng.choice(RHYTHM_POOLS)
        for d in rhy:
            dur = d * 0.25
            if rng.random() < profile["step"]:
                step = rng.choice([-1, 0, 1])
                n = snap_to_scale(prev + step, scale_pitches)
            elif rng.random() < (1 - profile["chord_tone"]):
                leap = rng.choice([-3,-2,2,3])
                n = snap_to_scale(prev + leap, scale_pitches)
            else:
                n = rng.choice([snap_to_scale(base_octave + i, scale_pitches)
                                for i in range(-5, 6)])
            n = max(profile["melody_range"][0], min(profile["melody_range"][1], n))
            note_obj = note.Note(n, quarterLength=dur)
            note_obj.volume.velocity = rng.randint(60, 100)
            s.append(note_obj)
            prev = n
    return s

def generate_chords(prog, ext, bars, rng):
    s = stream.Stream()
    for bar in range(bars):
        roman = prog[bar % len(prog)]
        root = ROMAN_TO_SEMITONE[roman.upper()] if roman.upper() in ROMAN_TO_SEMITONE else 0
        root_midi = 60 + root
        chord_notes = build_chord(root_midi, ext, [])
        c = chord.Chord(chord_notes, quarterLength=4.0)
        c.volume.velocity = rng.randint(55, 70)
        s.append(c)
    return s

def generate_bass(prog, bars, rng):
    s = stream.Stream()
    for bar in range(bars):
        roman = prog[bar % len(prog)]
        root = ROMAN_TO_SEMITONE[roman.upper()] if roman.upper() in ROMAN_TO_SEMITONE else 0
        root_midi = 48 + root
        n = note.Note(root_midi, quarterLength=2.0)
        n.volume.velocity = rng.randint(85, 100)
        s.append(n)
        n2 = note.Note(root_midi + 7, quarterLength=2.0)
        n2.volume.velocity = rng.randint(75, 90)
        s.append(n2)
    return s

def generate_drums(bars, rng):
    s = stream.Stream()
    s.insert(0, instrument.UnpitchedPercussion())
    for bar in range(bars):
        for beat in range(4):
            k = note.Unpitched()
            k.name = 'kick'
            k.quarterLength = 0.5
            k.volume.velocity = rng.randint(95, 115)
            s.append(k)
            if beat % 2 == 1:
                sn = note.Unpitched()
                sn.name = 'snare'
                sn.quarterLength = 0.5
                sn.volume.velocity = rng.randint(85, 105)
                s.append(sn)
    return s

def generate(style, key_name, bars, seed, output_dir):
    rng = random.Random(seed)
    cfg = GENRES.get(style, GENRES["pop"])
    root_pc = {"C":0,"C#":1,"D":2,"D#":3,"E":4,"F":5,"F#":6,"G":7,"G#":8,"A":9,"A#":10,"B":11}.get(key_name, 0)
    scale_pitches = make_scale(root_pc, cfg["scale"])

    parts = {}
    parts["melody"] = generate_melody(scale_pitches, cfg, bars, rng, cfg["melody_range"][0])
    parts["chords"] = generate_chords(cfg["prog"], cfg["ext"], bars, rng)
    parts["bass"] = generate_bass(cfg["prog"], bars, rng)
    parts["drums"] = generate_drums(bars, rng)

    os.makedirs(output_dir, exist_ok=True)
    for name, part in parts.items():
        part.insert(0, tempo.MetronomeMark(number=cfg["tempo"]))
        part.insert(0, key.Key(key_name, cfg["scale"]))
        part.insert(0, meter.TimeSignature("4/4"))
        part.metadata = metadata.Metadata(title=f"{style}_{name}", composer="MIDI Generator")
        path = os.path.join(output_dir, f"{style}_{name}_seed{seed}.mid")
        part.write("midi", path)
        print(f"  Written: {path}")

def main():
    parser = argparse.ArgumentParser(description="MIDI Generator - Python backend")
    parser.add_argument("--style", default="pop", choices=list(GENRES.keys()))
    parser.add_argument("--key", default="C", help="Key (C, D, E, F, G, A, B)")
    parser.add_argument("--bars", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="output")
    args = parser.parse_args()
    print(f"Generating {args.style} in {args.key}, {args.bars} bars, seed={args.seed}")
    generate(args.style, args.key, args.bars, args.seed, args.output)
    print("Done.")

if __name__ == "__main__":
    main()
