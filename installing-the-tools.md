# Installing the Tools

**Outcome: a desk with four tools on
it — an ordinary Python, the Circup
librarian, the Blinka bridge, and the
mpy-cross compiler — each able to state
its version.** Nothing in this chapter
needs a board. CircuitPython's unusual
mercy is that the software you install
to *use* a board is the firmware itself,
which arrives by a route chapter 4
describes; everything here is the
supporting cast that lives on your
computer, and it is all the lab needed
for chapters 6 to 10.

## Ordinary Python, kept in a venv

The desk tools are Python programs, so
they begin with Python itself — the
lab's machine had **Python 3.12.3**.
Install the tools into a **venv**
(a private folder of Python packages,
so they neither disturb nor are
disturbed by the system's Python):

```bash
python3 -m venv cpy-tools
source cpy-tools/bin/activate
pip install circup adafruit-blinka
```

That one `pip install` brings the two
named tools and their dependencies —
PlatformDetect and PureIO under Blinka,
among others. The lab's transcript
`circuitpython-lab/transcripts/t00-versions-and-tools.txt`
keeps the full installed list.

## The checks

Each tool states its name and version,
and those four lines are this chapter's
acceptance test:

```bash
circup --version
```

```text
Circup, A CircuitPython module updater. Version 3.1.0
```

Blinka has no `--version` flag of its
own; it is a library, so ask the package
manager, and then ask Python to import
its three headline modules:

```bash
pip list --format=freeze | grep -i blinka
python -c "import board, digitalio, busio; print('imports ok')"
```

The lab's versions: **Circup 3.1.0**,
**Adafruit-Blinka 10.1.0**. The import
line deserves a warning that chapter 10
will cash in: on an ordinary PC it
prints, alongside success, Blinka's own
honest notice —

```text
WARNING: GENERIC_X86 is not fully supported. Some features may not work.
```

— because Blinka's natural home is a
single-board computer with real pins,
and on a desktop it knows its own
limits. Imports succeeding is a desk
result, not a hardware promise.

## mpy-cross: the compiler, from the source

The fourth tool is not a pip package in
this guide. **mpy-cross** — the
cross-compiler that turns `.py` into the
`.mpy` files a board also accepts — is
published by the CircuitPython project
itself, one build per firmware version,
at the project's own storage:

```text
https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/linux-amd64/mpy-cross-linux-amd64-9.2.8.static
```

The lab downloaded the build matching
firmware **9.2.8** (the version its
imitation board claims, chapter 4), made
it executable, and asked it the only
question that matters at install time:

```bash
chmod +x mpy-cross-linux-amd64-9.2.8.static
./mpy-cross-linux-amd64-9.2.8.static --version
```

```text
CircuitPython 9.2.8 on 2025-05-28; mpy-cross emitting mpy v6.3
```

Read that line twice; chapter 8 lives
inside it. The binary *is* CircuitPython
9.2.8's compiler, and it emits **mpy
v6.3** — a format edition, which a board
running that firmware will accept and a
board running a different major firmware
may not. Match the mpy-cross build to
the firmware on your board the way you
would match a key to a lock; Circup,
chapter 6 shows, does this matching for
the libraries it installs, which is one
of the reasons it exists.

Other platforms have their own builds in
the same listing (macOS and Windows
among them), and mpy-cross can also be
built from the CircuitPython source for
the patient. The lab verified only the
Linux amd64 static build above.

## What is deliberately not installed

No board drivers, no serial terminal,
no editor is prescribed by this guide —
a board's serial port appears with
ordinary operating-system support, any
terminal program can read it, and any
text editor can edit `code.py`. The
editors made for this world (Mu and
Thonny are the well-known names) are
characterised in chapter 12, not
installed here. And no firmware is
downloaded in this chapter at all:
firmware belongs to a specific board
and a specific afternoon, and chapter 4
takes it up in its place.
