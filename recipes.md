# Recipes

Short jobs, each built only from pieces
the earlier chapters verified. Unless a
recipe says otherwise, every command
was run in the lab, against a
folder-drive, on a machine with no
board attached.

## Desk-check a project before you package it

A project is a `code.py`, perhaps a
`boot.py`, a `lib/` folder, and a
requirements list. Before any of it
meets a board, chapter 7's two witnesses
in one sitting:

```bash
python check-code.py code.py boot.py sensor_readout.py
mpy-cross-9.2.8 -o code-check.mpy code.py && echo "mpy-cross accepts code.py"
```

`check-code.py` is the lab's script in
`circuitpython-lab/`; it compiles each
file and verifies the sensor example's
conversion points. mpy-cross is the
strict witness: if it speaks, the
firmware would refuse the file as it
stands. Then chapter 6's receipt,
read *before* you trust the folder:

```bash
circup --path . freeze
```

Run it in the project folder itself —
Circup will treat any drive-shaped
folder as the drive, which a project
folder is.

## Pin a library set, so a board can be rebuilt

The freeze output *is* the pin. Save
it as the project's requirements:

```bash
circup --path drive1 freeze > requirements.txt
circup --path drive2 install --py -r requirements.txt
```

The lab's frozen set — `adafruit_ticks==1.1.7`,
`adafruit_bme280==2.6.32`,
`adafruit_bus_device==5.2.17` — is the
output of the first command, and the
second command is the same install
chapter 6 ran from the hand-written
version of that list, dependency
(`adafruit_bus_device`) arriving with
it. A board lost, wiped, or replaced is
a folder copy and this one command away
from being itself again.

## Prepare a drive for a board you will meet later

The chapter 4 trick, aimed at a trip:
build the folder now, copy it onto the
board when you reach it.

```bash
mkdir field-kit
cp code.py settings.toml field-kit/
circup --path field-kit install -r requirements.txt
```

Note the missing `--py`: for a finished
project travelling to a board, take
Circup's default compiled form — the
drive will be smaller, and the matching
`.mpy` edition comes from the
`boot_out.txt` you place in the folder
copied from the target board, so copy
that file from the real drive first
when you can. With an invented name
card, as in this lab, say plainly in
the folder's README that the card is a
placeholder; chapter 4's lesson is that
tools believe the card completely.

## Test the thinking half under ordinary Python

Shape the project as chapter 7 advises
— readings in as values, decisions out
as code with no hardware imports — and
the thinking half tests at a desk, or
in any automated test run, with nothing
CircuitPython-shaped installed at all:

```bash
python sensor_readout.py
python check-code.py sensor_readout.py
```

```text
air: 21.5 C (70.7 F)
air: 21.7 C (71.1 F)
```

The invented numbers in
`circuitpython-lab/sensor_readout.py`
stand in for a real sensor's stream.
On the board, the same functions
receive the real stream; at the desk,
they receive the invented one — and the
functions cannot tell, which is the
point of the shape.

## Compile a folder of libraries ahead of time

To see exactly what a compiled library
set weighs — or to pre-build `.mpy`
files for a firmware you target — run
mpy-cross over the pieces and compare.
The lab's two files came out at roughly
half their source size (195 and 319
bytes against 414 and 662). For real
libraries, prefer chapter 6's path and
let Circup fetch the bundle's compiled
flavour; hand-compiling is for the
files *you* wrote, and for satisfying
the reasonable curiosity this recipe
began with.

## Share a project without sharing secrets

The chapter 11 habits as one motion:
ship `code.py`, `lib/` (or the
requirements file that rebuilds it),
and a `settings.toml` whose values are
invented and labelled, with the keys
the real file needs listed in the
README. The receiver replaces the
invented values on their own board.
Nothing in this recipe is a tool; it is
three minutes of care, and it is the
difference between a project folder
that can be posted anywhere and one
that quietly contains your house.
