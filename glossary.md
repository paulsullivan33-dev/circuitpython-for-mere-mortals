# Glossary

**Blinka** — Adafruit's compatibility
library for ordinary Python (CPython).
It provides CircuitPython's hardware
module names — `board`, `digitalio`,
`busio` — on bigger machines, fully on
single-board computers with real pins,
partially (and honestly, with warnings)
on a generic PC.

**board (module)** — the firmware's
description of the specific board:
attributes naming its pins (`board.LED`,
`board.SDA`). Boards differ; the module
is how a program says "this board,
whatever it is".

**Board ID** — the string naming one
exact board model, printed in
`boot_out.txt` and used by tools and by
circuitpython.org's per-board pages to
mean that model.

**boot.py** — an optional file in the
drive's root, run once at power-up
before `code.py`. It can change how the
board starts, including the drive's
read-only terms. Most projects never
need one.

**boot_out.txt** — the firmware's name
card, rewritten at every start: version,
board name and ID, and the chip's
unique ID. Read by humans and by Circup
alike.

**Bundle** — the project's release
archive of libraries, published by
date, in flavours: source (`.py`) and
compiled (`.mpy`) per firmware major
version. Circup downloads and caches
bundles.

**busio** — the module for the serial
buses boards speak to chips with,
chiefly I2C and SPI: one shared pair
of wires, many devices, each with an
address.

**Circup** — the command-line librarian
on your computer. It reads a drive's
`boot_out.txt`, then installs, lists,
updates, freezes, and removes libraries
in the drive's `lib/` folder from the
bundles, resolving dependencies.

**CIRCUITPY** — the name of the USB
drive a board running CircuitPython
presents when plugged into a computer.
The drive is the board's whole
filesystem, and saving to it deploys.

**code.py** — the program file in the
drive's root. The board runs it after
every start and every save.

**digitalio** — the module for pins as
switches: claiming a pin, setting its
direction (input or output), reading or
driving its value.

**Firmware** — the CircuitPython
interpreter itself, built per board and
copied onto the chip once (and again
when you choose to change versions).
It makes the drive, the REPL, and the
language subset.

**.mpy** — the compiled form of a
CircuitPython file: bytecode with a
two-byte signature (marker `C`, then a
format-edition byte). Smaller than
source, loadable only by firmware of
the matching edition.

**mpy-cross** — the cross-compiler: the
firmware's own compiler built to run on
a desktop, turning `.py` into `.mpy` of
one firmware line's edition. The
strictest check a desk can run.

**REPL** — Python's interactive prompt
(`>>>`), offered by the board over its
USB serial connection when the program
is stopped: lines typed are carried out
by the chip at once.

**settings.toml** — the firmware's
settings file in the drive's root: TOML
key-value pairs including Wi-Fi
credentials and the web workflow port,
readable by programs through
`os.getenv`. Plain text, on a removable
drive: handle with care.

**Subset** — what CircuitPython's
Python is: the language core, a
fraction of the standard library, and
hardware modules the desktop lacks.
Some desktop constructions (the lab
demonstrated `match`) are simply not
in it.
