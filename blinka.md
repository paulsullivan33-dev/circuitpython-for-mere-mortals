# Blinka — CircuitPython Ideas on a Computer

**Outcome: an exact map of what Blinka
does on a computer with no
microcontroller attached — which imports
succeed, which pure-Python libraries
genuinely run, and the verbatim errors
at the border where the desk runs out —
so its real home, on single-board
computers, makes sense.**

## The idea

**Blinka** is Adafruit's compatibility
library for ordinary Python — CPython,
the Python on laptops and Raspberry Pis.
It provides the CircuitPython hardware
modules by name: `board`, `digitalio`,
`busio`, `analogio`, and their kin,
implemented on top of whatever the host
machine actually has. The purpose is
reuse in both directions: a library
written for a microcontroller board —
one of chapter 6's hundreds — can be
imported on a bigger machine, and code
learned on a board reads the same on a
Pi wired to the same sensor. On a
Raspberry Pi or a similar single-board
computer, with real pins and buses,
Blinka is a working bridge, and much of
the sensor-library world runs on it
there. That world needs the hardware,
so in this guide it is characterised,
not run.

## What the desk ran

The lab's machine was an ordinary x86
PC, and Blinka knew it. The imports
themselves succeed (transcript
`t06-blinka-headless.txt`):

```text
board_id: GENERIC_LINUX_PC
```

`board.board_id` is Blinka's identity
for the host — and the host is
*generic*, which the `board` module's
own contents admit: instead of a
board's long list of named pins, this
`board` carries only the bus names
(`SDA`, `SCL`, `MISO`, `MOSI`, `SCLK`)
and Blinka's administrative innards.
Ask it for a board pin and the border
appears at once:

```text
claiming board.LED failed: AttributeError module 'board' has no attribute 'LED'
```

Ask it to open the I2C bus those pin
names promise, and the border is an
exact error, printed beside Blinka's
own warning that generic x86 is not
fully supported:

```text
WARNING: GENERIC_X86 is not fully supported. Some features may not work.
opening I2C failed: ImportError cannot import name 'i2cPorts' from 'microcontroller.pin'
```

That pair of sentences is Blinka's
honesty and this chapter's point in one
breath: the *names* are portable, the
*hardware* is not, and on a machine
without the hardware Blinka says so
rather than pretending.

## What genuinely runs: the pure-Python floor

Libraries divide, in practice, into
those that talk to hardware and those
that merely *think*. The thinking kind
runs anywhere Python does, and the lab
proved it with the library chapter 6
installed — taking the copy straight
from the imitation drive's `lib/` so
the artefact tested is the artefact
Circup fetched:

```text
adafruit_ticks 1.1.7 - sum: 4999950000 - ticks elapsed: 1
adafruit_bme280.basic imported: adafruit_bme280.basic
```

`adafruit_ticks` did its real job under
CPython: its millisecond counter timed
a hundred-thousand-step counting loop.
(One to a handful of ticks for that
loop, on a shared machine — a
demonstration of the mechanism, not a
benchmark.) The sensor library
`adafruit_bme280.basic` likewise
*imports* cleanly under CPython: its
code is valid, its dependencies import,
its classes exist. Only *constructing*
one — which needs a live I2C bus —
meets the same ImportError wall as
above. That is the honest shape of the
pure-Python floor: everything up to the
moment the program reaches for the
physical world is checkable on any
computer, and chapter 7's writing
advice (keep the thinking half
hardware-free) is what buys you the
floor.

## Where Blinka truly lives

On a Raspberry Pi, a BeagleBone, a
Jetson, and their relatives, Blinka's
`board` module names real pins,
`busio.I2C` opens a real bus, and the
same `adafruit_bme280` object the lab
could not construct will answer with a
temperature. The code in those projects
is, line for line, the code this guide
has been handling — which is the whole
design. A reader who begins on a board,
or begins here, owns one vocabulary
either way. What this guide will not do
is grade that experience: it did not
run it, and the desktop's failure modes
shown above are offered as the map of
the border, not as a review of what
lies past it.
