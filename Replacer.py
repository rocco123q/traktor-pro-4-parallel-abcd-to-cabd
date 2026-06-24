from pathlib import Path

# Dateinamen
file_a = "Traktor Pro 4.exe"
file_b = "Find.txt"
file_c = "Replace.txt"
output_file = "Traktor Pro 4 New.exe"

data_a = Path(file_a).read_bytes()
data_b = Path(file_b).read_bytes()
data_c = Path(file_c).read_bytes()

if len(data_b) != len(data_c):
    raise ValueError(
        f"Datei b ({len(data_b)} Bytes) und Datei c ({len(data_c)} Bytes) "
        "müssen gleich groß sein."
    )

pos = data_a.rfind(data_b)

if pos == -1:
    print("Bytefolge aus Datei b wurde nicht gefunden.")
else:
    patched_data = (
        data_a[:pos]
        + data_c
        + data_a[pos + len(data_b):]
    )

    Path(output_file).write_bytes(patched_data)

    print(f"Bytefolge gefunden bei Offset 0x{pos:X} ({pos} Dezimal)")
    print(f"Ersetzt und gespeichert als: {output_file}")
