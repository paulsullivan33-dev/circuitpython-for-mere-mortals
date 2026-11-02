# Compiled Files and mpy-cross

**Outcome: you can read an `.mpy` file's
identity from its first two bytes, say
why it is smaller than its source, and
say why the wrong edition of one fails
on a board that runs its siblings
happily.** Compiled files are the form
libraries usually arrive in, the form
that saves a small drive's space, and
the one part of the CircuitPython world
where the word "version" carries a
small, sharp edge.

## What an .mpy file is

CircuitPython code can travel two ways.
As **source** — the `.py` text you
wrote, which the board compiles in its
head each time it loads the file. Or as
**`.mpy`** — the same code already
compiled to **bytecode**, the
interpreter's internal instruction
form, by a compiler on a computer. The
board loads bytecode directly: a little
faster, a little less memory, and
noticeably less space on the drive. Your
own `code.py` is nearly always source —
the edit-save-run loop is the point —
but libraries, hundreds of files
written by other people and rarely
edited by you, are natural candidates,
which is why chapter 6 found Circup's
*default* is the compiled form.

The lab compiled both of the guide's
example programs with the mpy-cross
9.2.8 build from chapter 3
(transcript `t05-mpy-cross.txt`):

| Source | Bytes | `.mpy` | Bytes |
| --- | --- | --- | --- |
| `code.py` | 414 | `code.mpy` | 195 |
| `sensor_readout.py` | 662 | `sensor_readout.mpy` | 319 |

Roughly half, at this toy scale:
comments and formatting are gone, names
and structure compressed into the
interpreter's own shorthand. The ratio
is not a promise — it is these two
files, measured — but the direction is
the design's.

## The first two bytes

An `.mpy` file opens with a signature
the lab read byte by byte:

```text
$ od -A x -t x1z sensor_readout.mpy | head -2
000000 43 06 00 1f 0c 08 22 73 65 6e 73 6f 72 5f 72 65  >C....."sensor_re<
000010 61 64 6f 75 74 2e 70 79 00 0f 2b 2a 63 65 6c 73  >adout.py..+*cels<
```

The first byte, `0x43`, is the letter
**C** — CircuitPython's marker (its
parent MicroPython uses `M`; the family
resemblance is deliberate). The second
byte, `06`, is the **format version**:
this file is mpy edition 6, which is
what mpy-cross 9.2.8 reported emitting
(`mpy v6.3`, the point release within
edition 6). After the header comes the
source file's name, embedded — you can
see `sensor_readout.py` spelled out in
the dump — and then the bytecode
itself.

## The edition is a contract

A board accepts `.mpy` files of *its*
firmware's edition and refuses others
with an error naming the version
mismatch. New major CircuitPython
releases may change the edition; the
9.x line speaks edition 6. Three
practical consequences follow, and all
three are the sort of thing that is
obvious exactly once — usually the hard
way:

- **Match mpy-cross to the board.** One
  mpy-cross build per firmware line.
  Keep the 9.2.8 build for a 9.x board;
  a 10.x board wants its own. The binary
  states its allegiance in its
  `--version` line, chapter 3's check.
- **Let Circup do libraries.** Circup
  reads the firmware version from
  `boot_out.txt` and selects the matching
  compiled flavour from the bundle on
  its own — the lab watched it choose
  without being told. This is the
  ordinary path and the safe one.
- **Suspect the edition first** when a
  hand-copied library fails on a board
  that runs everything else: a drive
  stocked under one firmware, kept
  across a firmware upgrade, is a
  library of small mismatches waiting
  its turn. `circup update`, against
  the new firmware's name card, is the
  tidy rescue.

## Source or compiled, chosen honestly

Source in `lib/` is not a mistake to be
corrected on sight. It is readable —
when a library misbehaves, its `.py` is
the explanation — and it is editable,
and on a roomy drive those virtues win.
Compiled is the choice for a full
drive, a finished project, or a library
whose load time is felt. Circup makes
switching cheap (`--py` on install, per
chapter 6), and freeze records names
and versions either way, so the choice
is reversible and recorded. What is not
reversible is a mixed-edition `lib/`
folder made by hand without notes;
that folder is a future troubleshooting
chapter, and this guide would rather
you skipped writing it.
