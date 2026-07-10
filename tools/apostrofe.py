#!/usr/bin/env python3
"""Añade el marcador de 'apóstrofe de vigencia' (⟳) tras cada citación de artículo.
Idempotente y seguro: no toca bloques de código ``` ni citas ya marcadas.
Uso:  _apostrofe.py <archivo.md> [--apply]   (sin --apply = dry-run)
"""
import sys, re

MARK = "⟳"
LEYES = (r"CFF|LISR|LIVA|LGSM|LGTOC|LMV|CCF|CComercio|LFT|CPF|CPEUM|LFPDPPP|"
         r"LFPPI|LGEEPA|LA|LGCG|CNPP|CNPCF|LGRA|LFCE|LConcursos|LSC")

# citación: (art.|arts.|artículo|artículos) N [º/o] [-A] [bis/ter] [, M | y M]* [LEY]?
CITE = re.compile(
    r"(?P<head>\b(?:arts?\.|artículos?)\s+\d{1,4}[ºo°]?(?:-[A-Z0-9]+)?"
    r"(?:\s+(?:bis|ter|quáter))?"
    r"(?:\s*,\s*\d{1,4}[ºo°]?(?:-[A-Z0-9]+)?|\s+y\s+\d{1,4}[ºo°]?(?:-[A-Z0-9]+)?)*"
    r"(?:\s*,?\s*(?:fr(?:acc)?\.?|fracci[oó]n(?:es)?)\s*[IVXLCDM0-9º.,\sy]*?)?"
    r"(?:\s+(?:del?\s+)?(?:" + LEYES + r"))?)"
    r"(?P<tail>\s*(?:✅|⚠️))?",
    re.IGNORECASE)

def process(text):
    # separar en segmentos dentro/fuera de bloques de código ```
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    n = 0
    for idx, seg in enumerate(parts):
        if seg.startswith("```"):
            continue  # no tocar bloques de código
        def repl(m):
            nonlocal n
            whole = m.group(0)
            after = seg[m.end():m.end()+2]
            if MARK in whole or after.strip().startswith(MARK):
                return whole
            n += 1
            return whole + " " + MARK
        parts[idx] = CITE.sub(repl, seg)
    return "".join(parts), n

if __name__ == "__main__":
    path = sys.argv[1]
    apply = "--apply" in sys.argv
    with open(path, encoding="utf-8") as f:
        original = f.read()
    new, n = process(original)
    if apply:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"APPLIED  {n:4d} marcas  {path}")
    else:
        # dry-run: mostrar hasta 12 líneas que cambian
        shown = 0
        for o, w in zip(original.split("\n"), new.split("\n")):
            if o != w and shown < 12:
                print("  -", o[:150])
                print("  +", w[:150])
                shown += 1
        print(f"DRY-RUN  {n:4d} marcas se añadirían en {path}")
