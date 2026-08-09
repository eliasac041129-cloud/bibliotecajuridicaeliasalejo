#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta de apoyo para la disolución de los tres estratos (vacío C-1 de la
Auditoría de la Edición Final).

NO reescribe nada por sí sola: la disolución es trabajo editorial por capítulo.
Esta herramienta hace las tres tareas mecánicas que sí se pueden automatizar sin
riesgo, y que son las que garantizan que no se pierda sustancia:

  1. extraer   → volcar los dos apéndices de un capítulo para poder leerlos.
  2. cortar    → eliminar los apéndices y sellar el capítulo con su nota de voz
                 consolidada (solo después de haber integrado su contenido).
  3. verificar → comparar contra `main`: delta de palabras y presencia de cada
                 concepto clave que el editor declare como obligatorio.

Uso:
    python3 tools/estratos.py estado
    python3 tools/estratos.py extraer  <ruta.md>
    python3 tools/estratos.py cortar   <ruta.md>
    python3 tools/estratos.py verificar <ruta.md> Concepto1 Concepto2 ...

Regla de oro (Auditoría §7.3.bis): si un capítulo pierde más del 10 % de sus
palabras, la disolución está mal hecha y hay que revisarla.
"""
import os, re, sys, glob, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SUP = '## ⚖️ Suplemento del Consejo Editorial'
CAT = '## 🎓 Profundización — Cátedra del Consejo Editorial'
UMBRAL = 0.10  # pérdida máxima tolerada


def _palabras(s):
    return len(s.split())


def _rel(path):
    """Profundidad relativa para los enlaces de la nota de cierre."""
    return '../' * (len(os.path.normpath(path).split(os.sep)) - 1)


def estado():
    """Cuántos tratados de la Columna I siguen con apéndices."""
    tratados = [f for f in glob.glob('Columna-I-Biblioteca/*/*.md')
                if not f.endswith('README.md')]
    con, sin = [], []
    for f in sorted(tratados):
        t = open(f, encoding='utf-8').read()
        (con if (SUP in t or CAT in t) else sin).append(f)
    print(f'Tratados en la Columna I ......... {len(tratados)}')
    print(f'Con voz consolidada (sin apéndices) {len(sin)}')
    print(f'Pendientes de disolución ......... {len(con)}')
    if con:
        print('\nPendientes:')
        for f in con:
            print(f'  · {f}  ({_palabras(open(f, encoding="utf-8").read()):,} palabras)')
    return con


def extraer(path):
    """Vuelca los apéndices para leerlos antes de integrarlos."""
    t = open(path, encoding='utf-8').read()
    i = t.find(SUP)
    if i < 0:
        i = t.find(CAT)
    if i < 0:
        print('Este capítulo ya no tiene apéndices.')
        return
    ap = t[i:]
    print(f'--- APÉNDICES DE {path} ({_palabras(ap):,} palabras) ---\n')
    print(ap)


def cortar(path):
    """Elimina los apéndices y sella el capítulo. Úsese SOLO tras integrar."""
    t = open(path, encoding='utf-8').read()
    antes = _palabras(t)
    i = t.find(SUP)
    if i < 0:
        i = t.find(CAT)
    if i < 0:
        print('Nada que cortar: el capítulo ya está consolidado.')
        return
    j = t.rfind('\n---\n', 0, i)
    cuerpo = (t[:j] if j > 0 else t[:i]).rstrip() + '\n'
    up = _rel(path)
    nota = (
        f'\n---\n\n'
        f'***Voz consolidada (Edición Final).** Este capítulo no lleva apéndices al cierre: la '
        f'doctrina, el análisis económico, el derecho comparado, la jurisprudencia y la mirada del '
        f'socio internacional viven **dentro** del razonamiento, en las secciones donde hacen falta. '
        f'Ver el vacío **C-1** y el método en la '
        f'[Auditoría de la Edición Final]({up}AUDITORIA-EDICION-FINAL.md).*\n'
    )
    open(path, 'w', encoding='utf-8').write(cuerpo + nota)
    despues = _palabras(open(path, encoding='utf-8').read())
    print(f'{path}: {antes:,} -> {despues:,} palabras ({despues - antes:+,})')


def verificar(path, conceptos):
    """Compara contra main y comprueba que no se perdió ningún concepto."""
    orig = subprocess.run(['git', 'show', f'main:{path}'],
                          capture_output=True, text=True).stdout
    new = open(path, encoding='utf-8').read()
    if not orig:
        print(f'{path}: no existe en main (capítulo nuevo).')
        a = None
    else:
        a, b = _palabras(orig), _palabras(new)
        delta = (b - a) / a
        marca = '✅' if delta > -UMBRAL else '❌ PÉRDIDA EXCESIVA'
        print(f'{path}')
        print(f'  main ............ {a:,} palabras')
        print(f'  consolidado ..... {b:,} palabras  ({b - a:+,}, {delta:+.1%})  {marca}')
    faltan = [c for c in conceptos if c.lower() not in new.lower()]
    if conceptos:
        print(f'  conceptos ....... {len(conceptos) - len(faltan)}/{len(conceptos)} conservados')
        for c in faltan:
            print(f'    ❌ PERDIDO: {c}')
    ok = (a is None or (b - a) / a > -UMBRAL) and not faltan
    print(f'  veredicto ....... {"APROBADO" if ok else "REVISAR"}')
    return ok


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd == 'estado':
        estado()
    elif cmd == 'extraer':
        extraer(sys.argv[2])
    elif cmd == 'cortar':
        cortar(sys.argv[2])
    elif cmd == 'verificar':
        verificar(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__)
