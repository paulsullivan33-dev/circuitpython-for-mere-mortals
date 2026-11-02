# The Neighbours

CircuitPython sits in a crowded street —
several other ways to give a small board
instructions, and one big machine
watching from the end of it. These are
characterisations from the projects' own
documentation, not benchmarks; the lab
ran CircuitPython's desk tools only, and
the sibling guide in this series ran
MicroPython itself.

## MicroPython: the parent

CircuitPython is a fork — a descendant,
kept compatible in spirit — of
**MicroPython**, the project that first
put Python on microcontrollers.
MicroPython is leaner, broader in the
boards it reaches (including some with
no USB-drive workflow at all, where
files travel by other tools), and
somewhat closer to the metal: more of
the machine is exposed, a little less
is cushioned. CircuitPython's additions
are mostly about the *approach*: the
drive, the save-and-run loop, the
frozen set of hardware module names
across boards, and the enormous shared
library collection this guide's chapter
6 draws from. The MicroPython guide in
this series is the deeper read; its lab
built the Unix port and ran the same
files under both Pythons, and its
board chapters carry the same honest
documented-only labels this one does.
A learner choosing today usually picks
by board and by library: the sensor you
own has a CircuitPython library, or it
doesn't.

## Arduino: the compiled elder

The Arduino world writes in C++, builds
on the computer, and uploads a finished
program through its own tooling. The
cost is the ceremony chapter 1 described
— an installed toolchain, a compile for
every change. The returns are real:
speed, a vast and older library and
tutorial world, and programs that are
finished artefacts rather than text a
chip interprets. A great many
CircuitPython users arrive from Arduino
for one project and stay for the loop;
a great many go the other way when a
project outgrows Python's pace or a
library exists only in C++. The Arduino
and PlatformIO guides in this series
cover that side of the street from
inside it.

## ESPHome: the cousin who skips code

For one branch of the family — ESP32
and kin, wired into home automation —
**ESPHome** removes the programming
from the other direction: you describe
the device in YAML, and firmware is
generated, compiled, and updated over
the air. No loop, no REPL, no Python at
all. For a house full of sensors that
do standard things, it is often the
right answer, and its guide in this
series builds for a real board. What
you give up is the program itself: when
the device must do something the YAML
does not already know how to say,
CircuitPython's open file of Python is
the more honest tool.

## Ordinary Python, and Blinka between

At the end of the street is the desktop
itself, running CPython with the whole
standard library and no pins at all.
Chapter 10's Blinka is the bridge the
ecosystem built between the two ends:
CircuitPython's names on the big
machine's Python, real on single-board
computers, partial — measurably
partial, the lab showed — on a plain
PC. The neighbour relation matters
because the language is one language:
the reader who learns the subset here
finds the desktop's full Python a
superset waiting, and the Python guide
in this series is written for exactly
that reader.

## The editors: Mu and Thonny

Two editors court this world from the
desk side. **Mu**, from the MicroPython
and education world, speaks to boards
directly — it knows the drive, offers
the REPL in a pane, and is designed for
a first lesson. **Thonny**, a general
beginner's Python editor, likewise
carries board support among its
strengths. Neither is needed —
CircuitPython's editor is any editor,
which is a design decision, not a gap —
but a reader whose board *is* attached
may find their board-awareness worth
the download. The lab installed neither
and characterises them from their
documentation alone.
