# Troubleshooting

The failures the lab met for real, in
roughly the order a new user meets
them, then the board-side failures this
guide can only point at. Transcripts:
`circuitpython-lab/transcripts/t07-failures.txt`
unless another is named.

## "Could not find a connected CircuitPython device"

```text
Auto locating USB Disk based device failed. Please specify --path argument
or ensure your device is connected and mounted under the name CIRCUITPY.
Could not find a connected CircuitPython device.
(exit 1)
```

Circup went looking for a drive named
CIRCUITPY and there was none — in the
lab, because there was no board; in
life, because the board is unplugged,
on a charge-only cable, or mounted
under a different name after a firmware
hiccup. The error names both exits:
plug the board in and let the drive
appear, or stop asking Circup to hunt
and tell it where the drive is with
`--path`. Every Circup command in this
guide carries `--path` for exactly this
reason — a named target fails clearly,
a hunted one fails vaguely.

## The library that installed nothing, successfully

```text
WARNING:
        adafruit_no_such_module_xyz is not a known CircuitPython library.
Ready to install: []
(exit 0)
```

Chapter 6's trap, filed here where a
troubleshooter looks: a misspelt or
invented library name is a *warning*,
an empty install list, and an exit code
of 0. The board-side symptom arrives
later and elsewhere — `ImportError` in
`code.py`, on hardware, in front of an
audience — which is why the check
belongs at install time: read the
`Ready to install` line, and run
`circup --path <drive> freeze` after
installing to see the set the drive
actually holds. If the library is not
in the freeze, it is not on the board,
whatever the install said.

## "No such option: -y"

Uninstall asks before removing, and
Circup offers no flag to pre-answer:

```text
Error: No such option '-y'.
(exit 2)
```

The lab reached for `-y` out of habit
from other tools; habits are not
documentation. In a terminal, answer
the prompt. In a script, pipe the
answer — `echo y | circup ... uninstall
<name>` — and know that you have done
deliberately what the tool made
slightly awkward on purpose: removals
are confirmed because `lib/` is the
board's whole library, and a silent
mass removal would be a strange feature
to want.

## "Directory ... does not exist", from --path

```text
Error: Invalid value for '--path': Directory 'no-such-folder' does not exist.
(exit 2)
```

`--path` is taken literally, from the
folder you are standing in — the lab
produced this error in bulk by running
a drive-relative command from the wrong
directory (its first, discarded set of
transcripts is a museum of it). It is
the most honest error in this chapter:
the folder is not there. `pwd`, `ls`,
and an absolute path cure it.

## `circup example` finds nothing

```text
Error: bme280 was not found in any local bundle examples.
(exit 0)
```

Not every bundle module carries
examples in the flavour Circup
downloaded, and its lookup is by the
bundle's example names, not by the
library's PyPI name; the lab tried the
module's name and a plausible example
name and found neither. The fallback is
the library's own repository, where its
examples live in an `examples/` folder —
or chapter 6's working set, which
never depended on this command. Noted
here because the feature is real, its
silence is confusing, and the guide
promises its failures a home.

## On the board, described and not witnessed

The desk chapters end; these are the
failures a board adds, from the
project's documentation, and this guide
labels them as read, not met:

- **The traceback on the serial
  console, and the REPL prompt instead
  of your program.** `code.py` raised;
  the board prints the error and waits.
  Read the last line first — it is
  Python's own error, in Python's own
  words, and it names the line.
- **`ImportError` for a library that is
  "installed".** It is not in *this*
  board's `lib/`, or it is there as a
  `.mpy` of the wrong edition after a
  firmware change. `circup freeze`
  against the real drive is the audit;
  chapter 8 is the edition's story.
- **The board keeps restarting, or the
  drive keeps vanishing.** The program
  may be crashing the interpreter
  itself, or the cable or power is
  marginal — USB hubs and long cables
  are the usual suspects in the
  project's own support lore. A board
  that cannot stay mounted cannot be
  reasoned with; feed it properly
  first.
- **It ran the old version.** An editor
  with the file open overwriting your
  fix, or two `code.py`-shaped files in
  play. The drive holds what ran; look
  at the drive, not at your memory of
  saving.
