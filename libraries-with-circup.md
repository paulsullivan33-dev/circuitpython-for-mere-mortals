# Libraries with Circup

**Outcome: a drive stocked from the
official library bundles by name, with
dependencies resolved for you, and a
freeze file that pins the exact set —
every step run here against the lab's
folder-drive, every version recorded.**
A CircuitPython program that reaches
beyond blinking — reading a sensor,
driving a display, speaking to a
network — almost always stands on
libraries: one per device or idea,
published by the project and its
community. This chapter is the supply
chain, and it is the most fully
desk-runnable chapter in the guide.

## Where libraries live, and what a bundle is

A library, mechanically, is a `.py`
file, or a folder of them (a package),
sitting in the drive's `lib/` folder.
The project collects its hundreds of
libraries into **bundles**: release
archives published on a steady cadence,
in flavours — source (`.py`), and
compiled (`.mpy`) per firmware major
version. Circup downloads the bundles
once, caches them on your computer, and
thereafter works from the cache,
checking for newer ones. The lab's
Circup found two default bundles,
recorded in transcript
`circuitpython-lab/transcripts/t01-a-drive-that-is-a-folder.txt`:

```text
adafruit/Adafruit_CircuitPython_Bundle    version = 20261031
adafruit/CircuitPython_Community_Bundle   version = 20261008
```

(The version numbers are dates — the
bundle's birthday — a convention worth
knowing when two people compare notes.)
`circup show` lists the modules a bundle
carries; the Adafruit bundle's list runs
to hundreds, from sensor drivers to
display helpers to protocol clients.

## Installing by name

```bash
circup --path drive1 install --py adafruit_ticks
```

```text
Searching for dependencies for: ['adafruit_ticks']
Ready to install: ['adafruit_ticks']
Installed 'adafruit_ticks'.
```

`adafruit_ticks` is a small, pure-Python
library for measuring elapsed
milliseconds safely — chosen for this
guide because chapter 10 can run it
outright on a computer. The `--py` flag
asks for the **source** form: readable,
editable, the form you want while
learning. Leave it off and Circup
installs the **compiled `.mpy`** form
instead (transcript `t03-mpy-list-uninstall.txt`
shows `adafruit_ticks.mpy` landing in a
second drive's `lib/`) — smaller, and
the form you want when the drive is
nearly full or the program is finished.
Circup picks the `.mpy` flavour matching
the firmware version it read from
`boot_out.txt`; that matching, silently
correct, is half of Circup's job.

## Dependencies, and installing from a file

Real libraries lean on others. The
guide's sensor library, for a common
environmental sensor, leans on the bus
library beneath it. Ask for it as part
of a **requirements file** — a plain
list, one library per line, at
`circuitpython-lab/requirements.txt`:

```text
adafruit_ticks
adafruit_bme280
```

```bash
circup --path drive1 install --py -r requirements.txt
```

```text
Searching for dependencies for: ['adafruit_bme280', 'adafruit_ticks']
Ready to install: ['adafruit_bme280', 'adafruit_bus_device', 'adafruit_ticks']
Installed 'adafruit_bme280'.
Installed 'adafruit_bus_device'.
'adafruit_ticks' is already installed.
```

Read the middle line as the chapter in
miniature: you named two; three are
ready, because `adafruit_bus_device`
came along as a dependency, named in the
open. Already-present libraries are
reported, not recopied. The resulting
`lib/` (transcript
`t02-installing-libraries.txt`) holds
one single-file library and two
packages, each package a folder with
its own modules inside.

## Freeze, list, update, uninstall

Four verbs keep a stocked drive honest:

```bash
circup --path drive1 freeze
```

```text
adafruit_ticks==1.1.7
adafruit_bme280==2.6.32
adafruit_bus_device==5.2.17
```

**freeze** prints the installed set as
a pinned list — the same shape as the
requirements file, now with exact
versions. Save that output as your
project's requirements and a fresh drive
can be rebuilt to the identical set.
Those three version numbers are this
guide's lab record: ticks 1.1.7, the
sensor library 2.6.32, its bus
dependency 5.2.17.

**list** names only what is out of date
— here, `All modules found on the device
are up to date.` **update** acts on that
list (with `--all` to accept major
version jumps without prompting).
**uninstall** removes a library, and
asks first:

```bash
echo y | circup --path drive1 uninstall adafruit_ticks
```

```text
Uninstalling ('adafruit_ticks',) from drive1
Uninstalled 'adafruit_ticks'.
```

That prompt matters more than it looks:
there is **no `-y` flag** — chapter 13
keeps the lab's discovery of that fact —
so scripts must feed the answer, and
humans must mean it.

## The trap this chapter exists to disarm

Circup is polite about names it does
not know — dangerously polite:

```bash
circup --path drive1 install --py adafruit_no_such_module_xyz
```

```text
WARNING:
        adafruit_no_such_module_xyz is not a known CircuitPython library.
Ready to install: []
(exit 0)
```

(Transcript `t07-failures.txt`.)
Misspell a library and Circup *succeeds*,
exit code and all, having installed
nothing. The `Ready to install` line is
the receipt that tells the truth — read
it the way chapter 6 of the Piper guide
in this series teaches audio checks:
trust the measurement (here, `freeze`
afterwards, or `ls` the `lib/` folder),
never the exit code alone.
