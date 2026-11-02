# Settings and Secrets

**Outcome: `settings.toml` understood
as what it is — the firmware's own
settings file, plain text on a removable
drive — with the working habits that
fact deserves.** This is the chapter
where this guide keeps the promise made
in chapter 1: the ethics and care line
for CircuitPython is stated early, in
the text, not saved for a footnote.
The line is about passwords, so here it
is before any procedure: **the Wi-Fi
credentials on a CircuitPython board
sit in a readable file on a drive any
computer can read. Never put a real one
in an example, a screenshot, a repository,
or a shared project folder — and treat
a board that holds your home password
as a key to your home.**

## The file

Boards with Wi-Fi (and boards doing a
few other firmware-level tricks) read
their settings from `settings.toml` in
the drive's root — TOML, the
key-equals-value format, one setting
per line:

```toml
CIRCUITPY_WIFI_SSID = "example-network"
CIRCUITPY_WIFI_PASSWORD = "example-password-not-real"
CIRCUITPY_WEB_API_PORT = 8080
```

That is the lab's copy, kept at
`circuitpython-lab/settings.toml`, with
an invented network and a password
invented to be worthless, labelled as
such in its comments. The check the
desk can run is structural — the file
*parses*, and the values come back with
their types intact (transcript
`t08-settings-and-boot.txt`):

```text
{'CIRCUITPY_WIFI_SSID': 'example-network', 'CIRCUITPY_WIFI_PASSWORD': 'example-password-not-real', 'CIRCUITPY_WEB_API_PORT': 8080}
```

What the desk cannot run is the
firmware reading it: on a board, these
values are consumed at startup, the
Wi-Fi joins using them without your
program asking, and the web workflow —
the board serving a small site from
which code can be edited in a browser —
listens on the port named. Those
behaviours are documented, and labelled
so here.

## Your program reads it too

The same file is the project's proper
home for the values your *program*
needs that should not be hard-coded —
an API key for a weather service, a
device name, a server address. Your
code asks the firmware for them:

```python
import os

ssid = os.getenv("CIRCUITPY_WIFI_SSID")
api_key = os.getenv("MY_SERVICE_API_KEY")
```

`os.getenv` returns the string from
`settings.toml`, or `None` when the
name is absent — a behaviour worth
leaning on, because it lets a project
folder carry a `settings.toml` of
invented example values that runs
(and politely reports what is missing)
anywhere, while the board on the desk
carries the real ones, unshared. That
pattern — example file public, real
file private to the drive — is the
whole security posture available here,
and it is sufficient *if* it is kept.

## boot.py, the neighbour file

One more drive-root file belongs in
this chapter because it shares the
theme of *things the firmware trusts*.
**`boot.py`** runs once at power-up,
before `code.py`, and can alter the
board's own terms: the classic use
makes the drive read-only *to the
board*, so a data-logging program
cannot corrupt its own filesystem while
the computer keeps write access. The
lab's example is deliberately the
plainest possible (it prints a line and
changes nothing), and it compiles under
both of chapter 7's witnesses; its
effects, like the settings' effects,
exist only on hardware and are
documented-only here. The care line
for `boot.py` is the same shape as for
`code.py`: a board runs the files it
finds, immediately and without asking,
so a drive's contents deserve the
scrutiny you would give any program
someone hands you on a stick — because
that is, exactly, what they are.

## The habits, collected

- Example files carry invented values
  and say so, in comments, in the file.
- The real `settings.toml` lives on the
  board's drive and in your private
  backup of it — not in the project's
  git repository, not in a shared
  folder, not in a screenshot.
- A project shared with the world
  ships `settings.toml` *described*
  (the README lists the keys) and a
  template of invented values, and
  chapter 11's recipes keep it so.
- A board leaving your hands — sold,
  lent, given — gets its drive wiped or
  its settings replaced first, the way
  you would wipe a phone.

None of this is CircuitPython being
careless; a removable drive with a
readable settings file is the same
simplicity that makes the whole system
teachable. The trade was made openly by
the design. Keeping it is made, daily,
by the habits.
