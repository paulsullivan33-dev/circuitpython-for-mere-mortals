# CircuitPython for Mere Mortals

Programming a microcontroller used to
mean a compiler on your computer, a
special cable ritual, and a chip that
did nothing until the ritual succeeded.
**CircuitPython** removes the ritual.
It is a version of **Python** — the
ordinary, readable programming language —
rebuilt to run on a small board itself.
You plug the board into any computer and
it appears as a small USB drive called
**CIRCUITPY**. You save a text file named
`code.py` onto that drive, and the board
runs it. Save an edit, and the board runs
the new version. That is the whole loop:
no compiler step for your own code, no
flashing tool, no vendor program.

This guide explains how that loop works,
what lives on the drive, how the library
manager **Circup** stocks the board with
other people's code, and how to check
your programs at your desk before they
ever meet hardware. Then it does
something most microcontroller guides
skip: it is exact about the boundary of
its own lab. **The lab that wrote this
guide had no microcontroller board.**
That is not hidden in a footnote; it is
the organising fact of the second half
of the guide, because it turns out a
great deal of CircuitPython life — the
libraries, the compiled files, the
syntax checks, the project layout —
happens on an ordinary computer, and
that part was run for real.

What the lab ran, it ran properly:
**Circup 3.1.0** managing libraries
against a folder standing in for the
CIRCUITPY drive (Circup found it, read
its `boot_out.txt`, and reported the
board and firmware version it claimed);
the official **mpy-cross 9.2.8**
compiler turning the guide's example
programs into `.mpy` files and refusing
the ones a board would refuse; example
programs checked by a small script the
lab wrote; and Adafruit **Blinka
10.1.0** — the library that lends
CircuitPython's names to ordinary
Python — imported under CPython, where
its pure-Python libraries ran and its
hardware claims failed in ways the guide
shows you verbatim.

What the lab could not do, it did not
fake. Flashing firmware onto a board,
watching a light blink, typing at the
board's serial REPL, reading a real
sensor, seeing a display light up: none
of that hardware was in the room, so
those parts are taught from the
project's documentation and labelled
documented-only wherever they appear.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What CircuitPython is**](what-circuitpython-is.md) —
  the mental model: Python living on the
  board, the drive that is the editor's
  save button, and why beginners and
  tired experts both like it
- [**The moving parts**](the-moving-parts.md) —
  the firmware, the drive and its four
  named files, the `lib` folder, the
  serial REPL, and which part does what
- [**Installing the tools**](installing-the-tools.md) —
  the desk-side kit: Python, Circup,
  Blinka, and the mpy-cross compiler,
  each with its version check
- [**Meeting the drive**](meeting-the-drive.md) —
  what a CIRCUITPY drive contains, what
  `boot_out.txt` says about the board,
  and how a folder can stand in for one
- [**Your first program**](your-first-program.md) —
  the blinking light in `code.py`, taken
  apart line by line, and what a desk can
  and cannot prove about it
- [**Libraries with Circup**](libraries-with-circup.md) —
  the bundles, installing by name and by
  requirements file, dependencies found
  for you, and the freeze that pins them
- [**Checking code without a board**](checking-code-without-a-board.md) —
  the two witnesses a desk has: ordinary
  Python's compiler, and mpy-cross, the
  stricter one that knows the subset
- [**Compiled files and mpy-cross**](compiled-files-and-mpy-cross.md) —
  what an `.mpy` file is, its two telling
  first bytes, why its version must match
  the firmware, and why Circup's default
  is compiled
- [**Blinka — CircuitPython ideas on a computer**](blinka.md) —
  the same module names under ordinary
  Python: what genuinely runs headless,
  and the exact errors where the desk
  runs out
- [**Settings and secrets**](settings-and-secrets.md) —
  `settings.toml`, Wi-Fi credentials held
  in plain text on a removable drive, and
  the care that fact demands
- [**Recipes**](recipes.md) — desk-check
  a project before a trip, pin a library
  set, prepare a drive for a board you
  will meet later, and test the pure
  logic under ordinary Python
- [**The neighbours**](the-neighbours.md) —
  MicroPython the parent, Arduino the
  compiled elder, ESPHome the no-code
  cousin, and ordinary Python waiting on
  the big machine: what each does that
  CircuitPython doesn't, and vice versa
- [**Limits**](limits.md) — a subset of
  Python, one program at a time, hardware
  a desk cannot verify, plain-text
  secrets, and code that runs the moment
  it is saved, whether you meant it or not
- [**Troubleshooting**](troubleshooting.md) —
  the board Circup cannot find, the
  misspelt library that "installs"
  nothing and reports success, the `-y`
  flag that does not exist, and the traps
  this guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Designing circuits, choosing components,
or soldering — this guide starts at the
software side of a board that already
exists. Building CircuitPython firmware
from source, writing native C modules,
and porting to a new chip are likewise
projects of their own. Driving a
specific sensor, display, or motor is
taught by shape (one sensor library is
installed and read here) rather than by
catalogue: the library collection is
hundreds strong, and each carries its
own examples.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before touching anything —
knowing which file holds what turns
later confusion into a named problem.
Chapters 3 and 4 set up the desk tools
and the drive; chapter 5 writes the
first program. If you own a board, you
can follow along in hardware from there.
If you don't — yet — chapters 6 to 10
are still fully yours: libraries, code
checks, compiled files, and Blinka all
run on a plain computer, and the guide
says plainly at each step where the desk
ends and the board begins. The lab's
transcripts live in
`circuitpython-lab/transcripts/`; its
example programs and checker script are
in `circuitpython-lab/` beside them.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [MicroPython for Mere Mortals](https://paulsullivan33-dev.github.io/micropython-for-mere-mortals/)
- [ESP32 for Mere Mortals](https://paulsullivan33-dev.github.io/esp32-for-mere-mortals/)
- [Arduino for Mere Mortals](https://paulsullivan33-dev.github.io/arduino-for-mere-mortals/)
- [PlatformIO for Mere Mortals](https://paulsullivan33-dev.github.io/platformio-for-mere-mortals/)
- [ESPHome for Mere Mortals](https://paulsullivan33-dev.github.io/esphome-for-mere-mortals/)
- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/circuitpython-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/circuitpython-for-mere-mortals/blob/main/LICENSE-CODE).
