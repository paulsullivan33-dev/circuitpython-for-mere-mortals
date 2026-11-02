# Your First Program

**Outcome: the traditional first
program — a blinking light — understood
line by line, with an exact account of
which of its truths a desk can check
and which only a board can.** The file
is the guide's own, kept at
`circuitpython-lab/code.py`, and its
numbers are invented in the plainest
sense: it blinks a light that this lab
has never seen, on a pin chosen because
many boards give their built-in light
that name.

## The program

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

## Line by line

**The three imports.** `time` is the
familiar one — `time.sleep` pauses.
`board` is new: it is the firmware's
description of *this* board, and its
attributes are pin names — `board.LED`,
`board.D13`, `board.SDA`, and so on.
The names differ between boards, which
is the point of the module: the same
program text says "the built-in light,
whatever this board calls it". `board`
exists only on the board side of the
world (and, in translation, under
Blinka, chapter 10). `digitalio` is the
tool for pins as switches: a pin claimed
through it can be an input that reads
the world or an output that drives it.

**Claiming the light.**
`digitalio.DigitalInOut(board.LED)`
takes the pin into the program's care —
pins are claimed, not shared, and a
well-mannered program releases them
(`led.deinit()`) when finished, though
an eternal blink program never reaches
that line. The object is the handle for
everything that follows.

**Direction.** A fresh claimed pin is
an input by default. Setting
`led.direction = digitalio.Direction.OUTPUT`
declares it an output — a pin the
program drives. The ceremony is two
lines because the pin's role in the
physical world genuinely changes:
reading a voltage versus imposing one.

**The loop.** `while True` is not a
lazy shorthand here; it is the honest
shape of microcontroller programs, which
have no desktop to return to. Inside:
`led.value = True` drives the pin high
(the light, on most boards, lights),
half a second passes, `False` drives it
low, half a second passes, forever.
Half a second each way is two changes
per second — slow enough to see, fast
enough to be sure the board is alive
and thinking, which is the entire
historical job of this program: it is
the "hello, world" of hardware, proof
of life before any harder claim.

## What happens on a board (documented)

Save this as `code.py` on a CIRCUITPY
drive and the board restarts it
immediately — that save-runs loop is
chapter 1's whole story. If the code has
an error, the board does not blink; it
prints the traceback to its serial
output and sits at the REPL instead,
which is why a first session usually
pairs the drive with a serial terminal.
Eject or unplug mid-save and the program
can arrive damaged; the ecosystem's
advice is the dull kind: let saves
finish. All of this is the project's
documented behaviour, stated here
because it is true and necessary, and
labelled because this lab watched none
of it happen.

## What the desk proved about this exact file

Three checks, all real, all in the
transcripts. The file **compiles** under
ordinary Python's byte-compiler
(`circuitpython-lab/transcripts/t04-checking-code.txt`,
via the lab's `check-code.py`). It
**compiles under mpy-cross 9.2.8** — the
firmware's own compiler — into a 195-byte
`.mpy` from its 414 bytes of source
(`t05-mpy-cross.txt`). And its imports
are exactly the three built-in modules
it names: chapter 6's Circup, asked to
stock a drive for this program's sake,
finds no external library to add, because
`time`, `board`, and `digitalio` travel
inside the firmware.

And the honest remainder: whether
`board.LED` exists on your board, whether
its light is wired to glow on high or on
low (some boards invert it), and whether
the blink is visible in daylight — the
desk knows none of this. The program is
*grammatically* proven, not *physically*.
Chapter 7 is about widening what the
grammatical witness can say, and
chapter 13 keeps the physical side of
the ledger permanently open, in the
reader's favour: the first thing a board
will teach you is which of this chapter's
sentences needed its light to be true.
