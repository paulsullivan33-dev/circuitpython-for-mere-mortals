# A sensor readout with invented numbers.
# The reading function is pure Python so it can be tested anywhere;
# on a real board the numbers would come from a sensor over I2C or SPI.

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

def describe_reading(label, celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{label}: {celsius:.1f} C ({fahrenheit:.1f} F)"

# Invented sample readings, as if sampled once a minute.
SAMPLES = [
    ("air", 21.5),
    ("air", 21.7),
    ("air", 22.0),
    ("water", 18.25),
]

if __name__ == "__main__":
    for label, value in SAMPLES:
        print(describe_reading(label, value))
