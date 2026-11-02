# The Moving Parts

CircuitPython feels like one thing — a
board that runs Python. It is actually
five parts doing five jobs, and nearly
every surprise in this guide, including
most of the troubleshooting chapter, is
one of these parts behaving exactly as
designed while the reader expected
another part's behaviour. This chapter
names them.

## The firmware: Python itself, resident

On the chip sits the **firmware**: the
CircuitPython interpreter, built for
that specific board and copied onto it
once (chapter 4 describes the ceremony;
it is the one part of this guide that is
wholly documented-only, because flashing
needs a board). The firmware is what
makes the drive appear, what runs your
files, and what decides which Python
constructions exist. Its version matters
more than versions usually do: each
firmware speaks one edition of the
`.mpy` compiled-file format, and a board
will refuse compiled files from another
edition with a version error. The
firmware writes its own name card —
`boot_out.txt` on the drive — every time
it starts, and chapter 4 shows that card
being read by a tool that trusts it
completely.

## The drive: four names that matter

The CIRCUITPY drive is an ordinary small
filesystem, and almost everything about
daily CircuitPython life is four entries
on it:

- **`code.py`** — your program. The
  board runs it after every start and
  every save. (No `code.py`? The board
  also accepts a short list of other
  names, such as `main.py`, but `code.py`
  is the convention, and one program is
  the rule.)
- **`boot.py`** — an optional file that
  runs once, *before* `code.py`, at
  power-up only, and can change how the
  board itself starts — remounting the
  drive read-only to the board, for
  instance. Most projects never need it;
  chapter 11 meets it beside its sibling.
- **`settings.toml`** — settings the
  *firmware* reads, most famously the
  Wi-Fi name and password on boards that
  have Wi-Fi. Your program can read it
  too, through `os.getenv`. Plain text,
  on a removable drive: chapter 11.
- **`lib/`** — a folder, and the subject
  of chapter 6. Libraries — other
  people's code, one file or folder per
  library — live here, and an `import`
  in your program looks here after the
  built-in modules. An empty `lib/` is
  why a program that works on a
  colleague's board fails on yours with
  `ImportError`.

And one entry you never edit:

- **`boot_out.txt`** — the firmware's
  name card: version, build date, board
  name, board ID, and the chip's unique
  ID. Humans read it to answer "what is
  this board running?"; tools read it to
  aim at the right target.

## The REPL: the board, talking back

Over the same USB cable, the board
offers a serial connection carrying two
things: the program's printed output
(and its error tracebacks, in plain
Python style), and — when the program
is stopped with Ctrl-C — the **REPL**,
Python's interactive prompt, live on
the chip. The REPL is CircuitPython's
other half: where `code.py` is the
committed program, the REPL is the
scratch pad where you interrogate a pin
or a sensor before committing. It needs
a serial terminal program on the
computer, and a board on the desk, so
in this guide it is described, not run
(chapter 13 lists it among the honest
gaps).

## Circup: the librarian on your computer

Libraries do not have to be fetched one
file at a time by hand, though they can
be — a library is, in the end, files in
`lib/`. **Circup** is Adafruit's
command-line librarian, running on your
computer. Pointed at a drive (or, as
this lab proves, at any folder wearing
the drive's shape), it reads
`boot_out.txt` to learn the board, then
installs named libraries from the
official **bundles** — the great zip
archives the CircuitPython project
publishes — pulling in each library's
own dependencies as it goes. Chapter 6
is its chapter; the lab used it for
every library in this guide.

## mpy-cross and Blinka: the two bridges

Two more parts live entirely on the
computer side, and chapters 8 and 10 are
theirs. **mpy-cross** is the
cross-compiler: the same compiler that
lives in the firmware, built to run on
a desktop, turning `.py` source into
`.mpy` bytecode of one exact format
edition. It is the strictest witness a
desk has — code it accepts is code the
firmware's own compiler accepts.
**Blinka** is the bridge in the other
direction: a library for ordinary Python
that provides CircuitPython's hardware
module names, so that code written for
a board can be *exercised* — within
limits this guide measures rather than
guesses — on a Raspberry Pi, a Linux
box, or, partially, any computer at all.

## Which part holds what

| Question | The part that answers it |
| --- | --- |
| Why did my edit start running before I finished typing it? | The drive — saving is deploying |
| Why does it say `ImportError` on this board only? | The `lib/` folder — the library is not on it |
| Why did it refuse my `.mpy` file? | The firmware — its format edition differs |
| Why does this desktop program run my sensor code? | Blinka — it supplies the module names |
| Why is the Wi-Fi password readable in a file? | `settings.toml` — the firmware's settings live there, in plain text |
| Why did Circup install three libraries when I asked for one? | Circup — dependencies are installed with their library |
| Why did it run *before* my program and change the drive? | `boot.py` — it runs first, at power-up |

Keep this table in mind. When
CircuitPython surprises you, the
surprise has an address, and the address
is one of these five.
