# What CircuitPython Is

You have a small board — a microcontroller,
a chip with a modest processor, a little
memory, and pins that can sense and switch
the physical world — and you want it to
*do* something: blink a light, read a
sensor, show a number. The traditional
way to give it instructions is to write
code in a compiled language on your
computer, build it into firmware, and
push that firmware onto the chip. Change
one line, and you repeat the whole
ceremony.

**CircuitPython is Python living on the
board instead.** The board runs a Python
interpreter — a program that reads Python
text and carries it out — as its permanent
resident. Plug the board into a computer
and it shows up as a USB drive named
**CIRCUITPY**. On that drive sits a file
called `code.py`. Whatever Python is in
that file is what the board does. Edit
the file in any text editor, save it,
and the board restarts the program with
your edit in it. The save button *is* the
deploy button.

This is worth pausing on, because it is
the reason the tool exists. CircuitPython
was created by Adafruit, a company that
teaches electronics, and it grew out of
**MicroPython** (chapter 12), the earlier
project that first squeezed Python onto
microcontrollers. Adafruit's bet was that
the ceremony was the barrier: a learner
who must install a toolchain before
blinking a light may never blink one.
With CircuitPython the toolchain is a
text editor. The board also offers a
**REPL** — the interactive `>>>` prompt
Python users know — over its USB serial
connection, so you can type a line and
watch the board answer, a tightrope-walk
between experiments that no compile cycle
survives.

## A first taste

On a real board, the famous first program
is a dozen lines. This is the guide's own
version, kept in
`circuitpython-lab/code.py`:

```python
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

Three imports name the three ideas:
`time` for pauses, `board` for "the pins
this particular board has", and
`digitalio` for treating a pin as an
on/off switch. Chapter 5 takes the file
apart line by line. Here, notice only
the shape: this is ordinary-looking
Python, saved as a plain text file, and
on hardware it blinks the board's
built-in light twice a second, forever.

Notice also what this guide can honestly
say about that file. It was written here,
compiled here, and compiled again by the
board's own compiler — chapter 7 shows
both witnesses. It was **not run on a
board** in this lab, because the lab had
no board. The blink itself is
documented-only, and the guide never
pretends otherwise.

## What it is not

CircuitPython is not all of Python. It
is a **subset** — the same language core,
a fraction of the standard library, and
hardware modules (`board`, `digitalio`,
`busio`) that desktop Python does not
have. Some desktop constructions simply
do not exist there: chapter 7 feeds the
same file to both Pythons and watches
CircuitPython's compiler reject a `match`
statement that ordinary Python runs
happily. It is not fast in the way
compiled code is fast — it trades speed
for the edit-save-run loop, gladly. It
is not a general computer: one program,
yours, runs the board; there is no
operating system crowd underneath. And
it is not the only way Adafruit's world
touches a computer: **Blinka** (chapter
10) lends CircuitPython's module names
to ordinary Python on bigger machines,
which is how some of this guide's lab
could run at all.

## Who it is for

The learner meeting a microcontroller
for the first time, whose real subject
is sensors and lights, not toolchains.
The teacher who needs thirty boards
doing the same thing by the end of one
lesson. The experienced builder who is
tired of the compile ceremony for what
is, honestly, a blinking light and a
temperature sensor. And — the reader
this guide quietly assumes — the person
whose board has not arrived yet, or is
in another room, who would like to get
the code *right* at a desk first.
Chapters 6 to 10 are for that reader:
libraries stocked, code checked, logic
tested, all before the board is asked
for anything.

## The honest catches, up front

Two, and chapter 13 returns to both.
First: the convenience cuts both ways.
Code that runs the moment it is saved is
code that also runs in a half-written
state the moment an editor autosaves,
and a board plugged into a computer runs
whatever `code.py` it finds — treat a
stranger's board, and a stranger's
`code.py`, with the respect you would
give any program that executes on sight.
Second: a board is a removable drive,
and one of its files, `settings.toml`,
holds Wi-Fi passwords in plain readable
text (chapter 11). Anyone holding the
board can read them. That is a deliberate
trade for simplicity, and it is yours to
manage — starting with never putting a
real password in an example, a
repository, or this guide. Every
credential in these pages is invented,
and labelled so.
