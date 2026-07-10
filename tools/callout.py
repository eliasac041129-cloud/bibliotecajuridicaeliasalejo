#!/usr/bin/env python3
"""Inserta el callout 'Apóstrofe de vigencia' bajo el H1 de cada tratado. Idempotente."""
import sys, os, re

def build(path):
    rel = os.path.relpath('fuentes-legales', os.path.dirname(path))
    return (
        f"> ⟳ **Apóstrofe de vigencia — léela cada vez.** El Derecho cambia sin avisar: un artículo "
        f"puede mudar de número, de redacción o quedar **derogado** de un día para otro. El símbolo "
        f"**⟳** que aparece tras cada artículo citado en este libro significa una sola cosa: "
        f"*«¿sigue vigente —y con este mismo número— hoy? No lo cites de memoria ni desde este libro: "
        f"**reitéralo en su código vigente**»* (textos oficiales en [`{rel}/`]({rel}/)). "
        f"Caso real: el **art. 390 del CPF** que este proyecto cotejó aparece hoy como **«Derogado»**. "
        f"Recuerda: un **✅** dice que el dato fue verificado *palabra por palabra a la fecha de su fuente*; "
        f"la **⟳** te avisa que esa fecha ya quedó atrás y que la última palabra la tiene el código, no el libro.\n"
    )

def process(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    if 'Apóstrofe de vigencia' in text:
        return False
    lines = text.split('\n')
    out, inserted = [], False
    for i, ln in enumerate(lines):
        out.append(ln)
        if not inserted and ln.startswith('# '):
            out.append('')
            out.append(build(path))
            inserted = True
    if not inserted:  # sin H1: al inicio
        out = ['', build(path), ''] + lines
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    return True

if __name__ == '__main__':
    done = 0
    for p in sys.argv[1:]:
        if process(p):
            done += 1
    print(f'callout insertado en {done} archivos')
