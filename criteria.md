# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's board, network, and sensor readings are invented.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: a Python subset whose edges a desktop compiler
   cannot see, one program owning the whole board, saving as
   executing whether you meant it or not, hardware truth that
   no desk check can reach, small space and traded speed,
   plain-text secrets, and a braid of versions kept compatible
   by a name card and a freeze file rather than by nature.
8. **The ethics rule is in the text, early.** CircuitPython's
   line is credential care, and chapters 1 and 11 state it
   before any procedure depends on it: `settings.toml` holds
   Wi-Fi passwords in plain text on a drive any computer can
   read, so real credentials never appear in examples,
   repositories, or shared project folders — every credential
   in this guide is invented and labelled so — and a board
   runs whatever code it finds the moment it is plugged in,
   so found boards and found code get the scrutiny any
   auto-running program deserves.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran. **The lab had no
microcontroller board of any kind attached, and none was
emulated.** That absence is the guide's organising fact, not
an apology appended to it: everything the lab claims as run
happened on an ordinary computer, and everything that needs a
board — flashing firmware, the drive appearing over a real
USB cable, the save-and-rerun loop as a physical event, a
light blinking, pins and buses carrying signals, the serial
REPL, a real sensor answering — is documented-only and is
labelled so in the text wherever it appears.

The desk tools were installed and run unmodified: **Python
3.12.3**, with **Circup 3.1.0** and **Adafruit-Blinka 10.1.0**
(and their dependency sets) installed from PyPI into a venv,
and the project's official **mpy-cross** static binary for
CircuitPython **9.2.8** (emitting mpy v6.3) downloaded from
the project's own storage. Circup worked against two folders
built to a real drive's shape (`code.py`, `lib/`, and a
`boot_out.txt` claiming invented board `generic_board`
running 9.2.8); Circup accepted the folders as a device
purely on the name card's evidence, which the guide states
openly — the imitation is the method, and fooling no reader
about it is the point. All transcripts live in
`circuitpython-lab/transcripts/`; the example programs,
`settings.toml`, requirements file, and checker script are in
`circuitpython-lab/`.

Run for real, with transcripts as evidence:

- Tool versions end to end: Python 3.12.3, the full installed
  package list, `circup --version` 3.1.0, mpy-cross 9.2.8
  stating its mpy edition, and Circup's command list (t00).
- The folder-drive accepted as a device: `Found device
  generic_board at drive1, running CircuitPython 9.2.8`, the
  newer-version notice (10.3.1 available), and the two default
  bundles with their dates (Adafruit 20261031, Community
  20261008) (t01).
- Library management against the folder-drive: installing
  `adafruit_ticks` 1.1.7 in source form; installing from a
  requirements file brought `adafruit_bme280` 2.6.32 with its
  dependency `adafruit_bus_device` 5.2.17 resolved and named
  by Circup; `install --auto` on `code.py` finding no external
  imports to add; `freeze` printing the three pinned versions;
  `list` reporting all modules up to date; the default install
  form landing as `adafruit_ticks.mpy`; uninstall requiring a
  typed confirmation, then reinstalling (t02, t03).
- Code checked two ways: the lab's `check-code.py` compiling
  all example files and verifying the sensor example's
  temperature conversion at 0, 100, and −40 degrees; the
  sensor example's pure-Python half running under CPython and
  printing its converted invented readings (t04).
- mpy-cross as the strict witness: both example programs
  compiled (414 to 195 bytes; 662 to 319 bytes); the `.mpy`
  header read byte by byte (marker `0x43` "C", edition byte
  6); a deliberately broken file refused by both compilers;
  and a `match`-statement program that CPython runs and
  mpy-cross 9.2.8 refuses with `SyntaxError: invalid syntax`,
  the guide's demonstrated proof of the language subset (t05).
- Blinka under CPython on a generic x86 PC: the modules
  import, `board_id` reports GENERIC_LINUX_PC, the `board`
  module carries only bus names, claiming `board.LED` fails
  with AttributeError, opening an I2C bus fails with
  ImportError beside Blinka's own GENERIC_X86 warning; the
  pure-Python `adafruit_ticks` (taken from the drive's own
  `lib/`) genuinely ran and timed a counting loop, and
  `adafruit_bme280.basic` imported, with construction of a
  sensor object impossible without a bus (t06).
- Failures as met: no device found (exit 1); an unknown
  library name producing a warning, an empty install list,
  and exit 0; `uninstall -y` rejected (exit 2) because the
  option does not exist; a bad `--path` rejected (exit 2);
  `circup example` finding no examples for the sensor library
  under either name tried (t07).
- `settings.toml` parsed as TOML with its invented values
  returned typed, and `boot.py` compiled — the full extent of
  what a desk can check about either file (t08).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Putting CircuitPython firmware on a board: bootloader
  entry, the `.uf2` (or other) file copy, per-board
  variations, and the CIRCUITPY drive appearing over USB.
- Everything on a live board: `code.py` running and rerunning
  on save, the blink itself, `board.LED` existing and its
  polarity, pins claimed and driven, the serial console and
  REPL, tracebacks as a board prints them, the web workflow,
  and Wi-Fi joining from `settings.toml`.
- Real sensors and displays: the BME280 library was installed,
  imported under CPython, and read as an artefact; no sensor
  was wired, addressed, or read.
- Blinka on the machines it is built for (Raspberry Pi and
  other single-board computers with real pins and buses),
  including the bus device libraries working there.
- The neighbour tools of chapter 12 (MicroPython's own board
  workflows beyond its sibling guide's lab, Arduino and
  ESPHome toolchains, the Mu and Thonny editors) —
  characterised, not run.

Fixtures are this guide's own and deliberately generic: an
invented board (`generic_board`, invented UID), invented
temperature readings for invented air and water, an invented
Wi-Fi network with a password invented to be worthless, and
stock program shapes (a blinking light, a sensor readout). No
real hardware, network, organisation, or project appears
anywhere in the lab.
