# Checking Code Without a Board

**Outcome: two desk witnesses for a
CircuitPython program, one lenient and
one strict, and a worked example of the
strict one catching what the lenient one
waved through.** A board is a fine
teacher but a slow correspondent, and
some of its lessons (`ImportError`,
`SyntaxError`) can be had at a desk for
free. This chapter is the desk's method,
run on the guide's own files.

## The first witness: does it compile at all

Ordinary Python byte-compiles a file
without running it:

```bash
python -m py_compile code.py
```

Exit 0 is silent success; a broken file
answers with the traceback and the
caret under the fault. The lab wrapped
that check, and the sensor maths of
chapter 5's sibling example, into a
small script — `circuitpython-lab/check-code.py`
— which compiles each file named to it
and then verifies the conversion
function at the three points anyone can
check in their head (freezing, boiling,
and the −40 where the scales meet):

```bash
python check-code.py code.py boot.py sensor_readout.py
```

```text
code.py: compiles
boot.py: compiles
sensor_readout.py: compiles
celsius_to_fahrenheit(0.0) = 32.0 (expected 32.0) OK
celsius_to_fahrenheit(100.0) = 212.0 (expected 212.0) OK
celsius_to_fahrenheit(-40.0) = -40.0 (expected -40.0) OK
ALL CHECKS PASSED
```

And the pure part of the sensor example
does more than compile — it *runs*,
because it is ordinary Python wearing
no hardware imports. Its invented
readings (label, temperature) print
converted, which is the shape a real
sensor loop's reporting half will take:

```text
air: 21.5 C (70.7 F)
air: 21.7 C (71.1 F)
air: 22.0 C (71.6 F)
water: 18.2 C (64.8 F)
```

(Transcript `t04-checking-code.txt`.)
Writing the number-handling half of a
project so it can be exercised like
this — sensor readings in as plain
values, decisions and formatting out —
is the single most useful habit this
guide can teach a reader whose board
is elsewhere. The hardware half stays
thin; the testable half carries the
weight.

## The lenient witness's blind spot

Ordinary Python's compiler is a witness
to *Python*, not to CircuitPython's
subset. The lab built the demonstration
on purpose, a three-line program using
a `match` statement:

```python
value = 2
match value:
    case 1:
        print("one")
    case _:
        print("other")
```

Ordinary Python runs it and prints
`other` — exit 0, no complaint.
`py_compile` accepts it. And a board
would refuse it, because `match` is not
in CircuitPython's language. A desk that
stops at the first witness will ship
that file with confidence it has not
earned.

## The second witness: the firmware's own compiler

mpy-cross *is* CircuitPython's compiler,
built for the desktop (chapter 3). Feed
it the same file:

```bash
mpy-cross-9.2.8 match_demo.py
```

```text
Traceback (most recent call last):
  File "match_demo.py", line 2
SyntaxError: invalid syntax
(exit 1)
```

(Transcript `t05-mpy-cross.txt`.) And
feed it the genuinely broken file — a
colon in the wrong place — and both
witnesses agree, as they should:

```text
  File "broken.py", line 1
SyntaxError: invalid syntax
```

The discipline this chapter proposes is
therefore two-staged, in order: compile
with the strict witness (the mpy-cross
build that matches your firmware), and
run the pure parts with the ordinary
one. What survives both has earned the
statement "this code is as ready as a
desk can make it" — no stronger
statement is available without a board,
and chapter 13 keeps it that way.

## What neither witness can say

Neither compiler knows your board.
`board.LED` compiles beautifully whether
or not your board has an `LED` pin;
an import of a library that is not in
`lib/` compiles fine and fails only on
the board; a sensor's address, a
display's wiring, a pin already claimed
by something else — all physical, all
silent at a desk. The witnesses check
*grammar and arithmetic*. The world is
checked by the board. Knowing which of
those two your bug belongs to is most
of what experience in this craft is.
