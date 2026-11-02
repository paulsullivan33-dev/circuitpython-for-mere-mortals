# Meeting the Drive

**Outcome: you can read a CIRCUITPY
drive the way you would read a name
card and a packing list — what board it
is, what firmware it runs, what program
it will run, and which libraries it
carries — and you will have watched a
tool do exactly that reading against a
folder, because a folder is all a drive
looks like from a computer's side of
the cable.**

## How a drive comes to exist

A board becomes a CIRCUITPY drive by
having CircuitPython firmware put on
it. The ceremony, briefly and
documented-only (this lab had no board
to perform it on): most boards enter a
**bootloader** mode — often by pressing
their reset button twice — in which they
appear as a small drive with a name like
`RPI-RP2` or a board-specific label. You
download the firmware file (a `.uf2` for
many boards, other forms for others)
for *your exact board* from
circuitpython.org, and copy it onto that
drive. The board restarts, and the drive
that comes back is named **CIRCUITPY**.
That is the whole installation of
CircuitPython itself, and it is redone
only when you choose to change firmware
versions. The site's per-board pages
carry the exact steps, including the
boards whose entry into bootloader mode
involves a button combination rather
than a double press.

## The name card: boot_out.txt

Every start, the firmware writes
`boot_out.txt` afresh. A real one names
its board; the lab's imitation board —
a folder built for this guide, since
Circup needed a drive and a folder is
what a drive is — carries an invented
but faithfully shaped one:

```text
Adafruit CircuitPython 9.2.8 on 2025-01-01; Generic Board with samd51
Board ID:generic_board
UID:0123456789ABCDEF
```

Line one is the firmware version
(**9.2.8**) and the chip family. Line
two is the **board ID**, the string the
whole ecosystem uses to mean *this exact
board model*. The UID is the individual
chip's serial — on the lab's card it is
invented digits, as befits an invented
board, and the guide flags it so because
chapter 1 promised that nothing here
pretends to be real hardware.

## A folder stands in, and a tool is fooled honestly

Here is the chapter's small, genuine
discovery, and it is verified, not
theoretical. Circup does not demand a
USB device. Given a folder containing
`code.py`, an empty `lib/`, and that
`boot_out.txt`, it addresses the folder
as a device:

```bash
circup --path drive1 freeze
```

```text
Found device generic_board at drive1, running CircuitPython 9.2.8.
A newer version of CircuitPython (10.3.1) is available.
Get it here: https://circuitpython.org/board/generic_board
No modules found on the device.
```

(Transcript
`circuitpython-lab/transcripts/t01-a-drive-that-is-a-folder.txt`.)

Three facts fall out of that one run.
First, `--path` lets you aim Circup at
any drive-shaped folder — which is how
you can prepare, stock, and audit a
project *before* a board is connected,
a trick chapter 11 turns into recipes.
Second, Circup reads the name card and
nothing more mystical: board identity,
in this ecosystem, is a text file's
say-so. Third, Circup checks the
firmware version against the project's
latest — and reported **10.3.1** as
available for this board — which tells
you the current CircuitPython release
line as the lab met it, and reminds you
that the imitation board's 9.2.8 is a
version behind. (`generic_board` is an
invented ID; that its page address
prints so confidently is Circup forming
the URL from the pattern, not evidence
the board exists. The guide is happy to
laugh at this, once, and then move on.)

## The rest of the drive

Chapter 2 introduced the cast; here is
their state on a fresh drive. `code.py`
may be absent (a brand-new board runs a
default or nothing), `lib/` may be
absent (Circup and the board both cope,
and Circup creates it when installing),
`boot.py` and `settings.toml` exist
only when someone creates them. The
drive is small — boards offer from a
few hundred kilobytes to a few megabytes
— which is a real design pressure
chapter 13 names: libraries are chosen,
not hoarded, and the compiled `.mpy`
form of chapter 8 is smaller than its
source. Everything on the drive is an
ordinary file, copyable by ordinary
means: backing up a board is copying a
folder, and chapter 11's recipes lean
on exactly that unglamorous fact.
