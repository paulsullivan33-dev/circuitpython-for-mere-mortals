#!/usr/bin/env python3
"""Check the lab's CircuitPython examples without a board.

Two checks, both honest about what they prove:
1. Every .py file byte-compiles under this Python. That proves the
   syntax is valid Python - it does NOT prove the file only uses
   the subset CircuitPython supports (mpy-cross is the stricter
   witness; see transcript t05).
2. The sensor example's conversion maths is right at the three
   points anyone can verify in their head: 0 C = 32 F,
   100 C = 212 F, and -40 is -40 in both scales.
"""
import py_compile
import sys

sys.path.insert(0, ".")
import sensor_readout

failures = 0
for name in sys.argv[1:]:
    try:
        py_compile.compile(name, doraise=True)
        print(f"{name}: compiles")
    except py_compile.PyCompileError as err:
        failures += 1
        print(f"{name}: FAILED - {err.msg.strip()}")

for celsius, expected in [(0.0, 32.0), (100.0, 212.0), (-40.0, -40.0)]:
    got = sensor_readout.celsius_to_fahrenheit(celsius)
    ok = abs(got - expected) < 1e-9
    print(f"celsius_to_fahrenheit({celsius}) = {got} (expected {expected}) {'OK' if ok else 'WRONG'}")
    failures += 0 if ok else 1

print("ALL CHECKS PASSED" if failures == 0 else f"{failures} CHECK(S) FAILED")
sys.exit(1 if failures else 0)
