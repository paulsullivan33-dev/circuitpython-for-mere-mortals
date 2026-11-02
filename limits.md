# Limits

What CircuitPython cannot do, stated
plainly. The desk-verified limits are
this lab's own findings; the hardware
ones are the project's documented
shape, labelled as such.

**It is a subset, and the subset is
not marked on the tin.** CircuitPython
is Python's language core with a
fraction of the standard library, plus
hardware modules desktop Python lacks.
Some of the missing is easy to guess —
no operating system to speak of, no
threads — and some is a tripwire: the
lab's `match` statement, valid modern
Python, runs under CPython and is
refused by CircuitPython's own compiler
as a syntax error (transcript
`t05-mpy-cross.txt`). There is no single
page in the language that draws the
whole line; the working rule is chapter
7's — let the strict witness, mpy-cross
in the firmware's own version, be the
judge, and never let a desktop's
"it ran" stand as evidence.

**One program, while it runs, is the
whole machine.** `code.py` is not an
application among others; it is the
board's occupation. There is no
switching to a second program, no
background task the firmware keeps for
you, no shell to fall back to — the
REPL is a prompt into the same single
interpreter. Projects that need several
occupations are one program with
several duties, written that way.

**Saving is executing.** The loop that
defines the tool defines its sharpest
limit: any save of `code.py` — yours,
an editor's autosave, a sync tool's —
restarts the program, in whatever state
the text was in at that moment. And the
symmetric fact deserves its sentence:
a board plugged into any computer runs
whatever it finds, immediately. Treat
found boards and found code accordingly.
Chapter 1 said it as a caution; here it
is as a limit, because it cannot be
configured away into something else.

**The desk cannot verify the world.**
This guide's whole second half was a
study of this limit, so it belongs in
the chapter: pin names, wiring, sensor
addresses, a display's behaviour —
physical claims, every one beyond the
reach of compilers and compatibility
libraries. The lab has the receipts for
the negative space: Blinka on a plain
computer has no `board.LED` to claim,
and its I2C bus fails to open with an
ImportError from the generic platform
(transcript `t06-blinka-headless.txt`).
A board is not a formality at the end
of the process; it is where half the
truths live.

**Space is small, and speed is traded
away.** The drive is kilobytes-to-
megabytes; the interpreter spends the
chip's modest power on friendliness.
Projects that grow into the ceiling —
a `lib/` that no longer fits, a loop
that must run faster than interpreted
Python on a small chip allows — meet
the honest end of the tool, and
chapter 12 names where they go next:
MicroPython's leanness at one side,
compiled Arduino code at the other.
Staying is also a choice; the `.mpy`
form of chapter 8 exists precisely to
buy room and time inside the tool.

**Secrets are plain text, and that is
a property, not a bug to be patched
by optimism.** Chapter 11's file holds
Wi-Fi passwords readably, on a drive
any computer can mount. There are
boards and builds with better stories,
and there is no setting in this guide's
scope that turns `settings.toml` into
a vault. The limit is managed by
habits — the real file unshared, the
board wiped before it leaves your
hands — and by never asking the tool
to guard what it was not built to
guard.

**Versions are a braid, not a line.**
Firmware version, bundle date, library
versions, and the `.mpy` edition move
at different speeds, and the system
keeps them compatible by the name-card
reading and bundle matching of chapters
4 and 6 — mostly. The mismatches that
remain (a `lib/` stocked for 9.x kept
across a move to 10.x, a library whose
new release expects a newer firmware)
present as ordinary, confusing errors
on the board. The freeze file of
chapter 11 is the braid written down;
projects that keep it can always say
exactly what they were running when
they worked.
