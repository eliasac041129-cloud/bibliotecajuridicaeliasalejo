#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculadora de promedio y techo alcanzable.

Contesta con números lo que el §XIV.4 del prompt maestro exige: promedio actual,
promedio MÁXIMO matemáticamente alcanzable, escenarios intermedios y qué materia
conviene más recuperar. El prompt es explícito: «NO me prometas un promedio que
matemáticamente sea imposible». Este programa existe para que eso no pase.

REGLA DE DISEÑO: no sabe el reglamento. Dos decisiones cambian el resultado y las
dos tienen que venir de `REGLAMENTO EXTRAORDINARIOS.pdf` y del Reglamento General
de Exámenes, no de una suposición:

  1. ¿La calificación reprobada sigue contando en el promedio después de aprobar
     la materia?  -> --reprobadas {ignora,cuenta}
  2. ¿El promedio se pondera por créditos o es media simple?
     -> --ponderacion {creditos,simple}

Mientras no se confirmen, el programa calcula LAS DOS y advierte.

Uso:
    python3 tools/promedio.py historial.csv
    python3 tools/promedio.py historial.csv --meta 8.5
    python3 tools/promedio.py --plantilla > historial.csv
    python3 tools/promedio.py --autotest

Formato del CSV (una fila por asignatura del plan):
    clave,materia,creditos,calificacion,estado,intentos
      estado: acreditada | reprobada | pendiente
      calificacion: número si está acreditada o reprobada; vacío si pendiente
"""
import csv
import sys
import argparse
from dataclasses import dataclass
from typing import List, Optional

CAL_MIN_APROBATORIA = 6.0
CAL_MAX = 10.0

PLANTILLA = """clave,materia,creditos,calificacion,estado,intentos
# Una fila por asignatura del plan 2254. Borra estos comentarios.
# estado: acreditada | reprobada | pendiente
# Ejemplo:
1101,Derecho Romano,8,9,acreditada,1
1102,Introduccion al Estudio del Derecho,8,7,acreditada,1
1203,Obligaciones,10,5,reprobada,2
1204,Sociedades Mercantiles,10,,pendiente,0
"""


@dataclass
class Materia:
    clave: str
    nombre: str
    creditos: float
    calificacion: Optional[float]
    estado: str
    intentos: int

    @property
    def acreditada(self) -> bool:
        return self.estado == "acreditada"

    @property
    def pendiente(self) -> bool:
        return self.estado in ("pendiente", "reprobada")


def leer(ruta: str) -> List[Materia]:
    out, errores = [], []
    with open(ruta, encoding="utf-8") as f:
        lineas = [l for l in f if l.strip() and not l.lstrip().startswith("#")]
    for i, fila in enumerate(csv.DictReader(lineas), start=2):
        try:
            cal = (fila.get("calificacion") or "").strip()
            estado = (fila.get("estado") or "").strip().lower()
            if estado not in ("acreditada", "reprobada", "pendiente"):
                errores.append(f"fila {i}: estado '{estado}' no válido")
                continue
            if estado == "acreditada" and not cal:
                errores.append(f"fila {i}: acreditada sin calificación")
                continue
            out.append(Materia(
                clave=(fila.get("clave") or "").strip(),
                nombre=(fila.get("materia") or "").strip(),
                creditos=float(fila.get("creditos") or 0),
                calificacion=float(cal) if cal else None,
                estado=estado,
                intentos=int(fila.get("intentos") or 0),
            ))
        except ValueError as e:
            errores.append(f"fila {i}: {e}")
    if errores:
        print("⛔ El archivo tiene errores. No se calcula nada sobre datos dudosos:\n")
        for e in errores:
            print("   ", e)
        sys.exit(1)
    return out


def promedio(materias: List[Materia], ponderacion: str,
             reprobadas: str, supuesto: Optional[float] = None) -> Optional[float]:
    """Promedio. `supuesto` = calificación hipotética para las pendientes.

    Si `supuesto` es None, solo promedia lo que ya tiene calificación.
    """
    num = den = 0.0
    for m in materias:
        peso = m.creditos if ponderacion == "creditos" else 1.0
        if peso == 0 and ponderacion == "creditos":
            continue
        if m.acreditada:
            num += m.calificacion * peso
            den += peso
        elif m.estado == "reprobada":
            if reprobadas == "cuenta":          # el 5 queda en el historial
                num += m.calificacion * peso
                den += peso
            if supuesto is not None:            # y además se aprueba después
                num += supuesto * peso
                den += peso
        elif m.estado == "pendiente" and supuesto is not None:
            num += supuesto * peso
            den += peso
    return round(num / den, 4) if den else None


def impacto(materias: List[Materia], ponderacion: str, reprobadas: str,
            supuesto: float) -> list:
    """Cuánto mueve el promedio final subir cada pendiente de `supuesto` a 10."""
    base = promedio(materias, ponderacion, reprobadas, supuesto)
    filas = []
    for i, m in enumerate(materias):
        if not m.pendiente:
            continue
        alt = list(materias)
        alt[i] = Materia(m.clave, m.nombre, m.creditos, CAL_MAX, "acreditada", m.intentos)
        # el resto de pendientes sigue en el supuesto
        resto = [x if j != i else alt[i] for j, x in enumerate(materias)]
        p = promedio(resto, ponderacion, reprobadas, supuesto)
        filas.append((m, round((p - base) * 1000) / 1000))
    return sorted(filas, key=lambda x: -x[1])


def informe(materias: List[Materia], ponderacion: str, reprobadas: str,
            meta: Optional[float]) -> None:
    acred = [m for m in materias if m.acreditada]
    pend = [m for m in materias if m.pendiente]
    repro = [m for m in materias if m.estado == "reprobada"]

    print("=" * 74)
    print(f"  PONDERACIÓN: {ponderacion}    REPROBADAS EN EL PROMEDIO: {reprobadas}")
    print("=" * 74)
    print(f"  Asignaturas en el plan ....... {len(materias)}")
    print(f"  Acreditadas .................. {len(acred)}")
    print(f"  Reprobadas ................... {len(repro)}")
    print(f"  Pendientes / no cursadas ..... {len(pend) - len(repro)}")
    cred_ac = sum(m.creditos for m in acred)
    cred_tot = sum(m.creditos for m in materias)
    if cred_tot:
        print(f"  Créditos ..................... {cred_ac:g} de {cred_tot:g} "
              f"({cred_ac/cred_tot*100:.1f}%)")

    actual = promedio(materias, ponderacion, reprobadas)
    print(f"\n  PROMEDIO ACTUAL .............. {actual if actual else '—'}")

    print("\n  ESCENARIOS (calificación supuesta en todo lo pendiente)")
    print("  " + "-" * 60)
    print(f"  {'supuesto':>10}  {'promedio final':>15}   escenario")
    for sup, nombre in ((6.0, "todo de panzazo"), (7.0, "conservador"),
                        (8.0, "probable si el sistema funciona"),
                        (9.0, "exigente"), (10.0, "TECHO MATEMÁTICO")):
        p = promedio(materias, ponderacion, reprobadas, sup)
        marca = "  <-- imposible superarlo" if sup == CAL_MAX else ""
        print(f"  {sup:>10.1f}  {p:>15}   {nombre}{marca}")

    techo = promedio(materias, ponderacion, reprobadas, CAL_MAX)
    if meta is not None:
        print(f"\n  META DECLARADA: {meta}")
        if techo is not None and meta > techo:
            print(f"  ⛔ IMPOSIBLE. Aun sacando 10 en absolutamente todo lo que "
                  f"falta,\n     el promedio final no puede pasar de {techo}.")
            print("     La meta tiene que bajar. No es pesimismo: es aritmética.")
        else:
            req = requerido(materias, ponderacion, reprobadas, meta)
            if req is None:
                print("  No hay pendientes: el promedio ya está cerrado.")
            elif req <= CAL_MIN_APROBATORIA:
                print(f"  ✅ Alcanzable con holgura: basta promediar {req} en lo que falta.")
            elif req <= CAL_MAX:
                print(f"  ⚠️  Alcanzable, pero exige promediar {req} en TODO lo pendiente.")
                if req >= 9.0:
                    print("     Eso no admite ni un tropiezo. Conviene fijar una meta "
                          "que sí tolere un error.")
            else:
                print(f"  ⛔ Requeriría promediar {req}, y el máximo es {CAL_MAX}.")

    if pend:
        print("\n  QUÉ CONVIENE MÁS RECUPERAR BIEN")
        print("  (cuánto sube el promedio final pasar esa materia de 8 a 10)")
        print("  " + "-" * 60)
        for m, d in impacto(materias, ponderacion, reprobadas, 8.0)[:10]:
            aviso = "  ⚠️ intentos: %d" % m.intentos if m.intentos >= 2 else ""
            print(f"  +{d:<7.3f} {m.nombre[:38]:38s} {m.creditos:g} cr.{aviso}")
        print("\n  Nota: el impacto en el promedio NO es el criterio de orden. El orden")
        print("  lo manda la SERIACIÓN: primero lo que desbloquea más materias, aunque")
        print("  suba menos el promedio. Esto solo dice dónde rinde más el esfuerzo extra.")

    if repro:
        riesgo = [m for m in repro if m.intentos >= 2]
        if riesgo:
            print("\n  ⛔ RIESGO DE OPORTUNIDADES AGOTADAS")
            for m in riesgo:
                print(f"     {m.nombre[:45]:45s} {m.intentos} intentos")
            print("     Verificar el límite reglamentario ANTES de inscribir nada más.")


def requerido(materias: List[Materia], ponderacion: str, reprobadas: str,
              meta: float) -> Optional[float]:
    """Calificación media necesaria en lo pendiente para alcanzar la meta."""
    lo, hi = 0.0, 20.0
    if not any(m.pendiente for m in materias):
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        p = promedio(materias, ponderacion, reprobadas, mid)
        if p is None:
            return None
        if p < meta:
            lo = mid
        else:
            hi = mid
    return round(hi, 2)


# ---------------------------------------------------------------------------
def autotest() -> None:
    """Comprueba la aritmética con casos de resultado conocido."""
    fallos = []
    total = [0]

    def check(nombre, obtenido, esperado, tol=1e-3):
        # tol por defecto 1e-3: promedio() redondea a 4 decimales a propósito,
        # así que comparar con igualdad exacta daría falsos negativos.
        total[0] += 1
        ok = obtenido is not None and abs(obtenido - esperado) < tol
        print(f"  {'✅' if ok else '❌'} {nombre}: {obtenido} "
              f"(esperado {round(esperado, 4)})")
        if not ok:
            fallos.append(nombre)

    # media simple sencilla
    ms = [Materia("1", "A", 10, 8, "acreditada", 1),
          Materia("2", "B", 10, 10, "acreditada", 1)]
    check("media simple de 8 y 10", promedio(ms, "simple", "ignora"), 9.0)

    # ponderación por créditos: 8(2cr) y 10(8cr) -> (16+80)/10 = 9.6
    mp = [Materia("1", "A", 2, 8, "acreditada", 1),
          Materia("2", "B", 8, 10, "acreditada", 1)]
    check("ponderado por créditos", promedio(mp, "creditos", "ignora"), 9.6)

    # una pendiente con supuesto 10 -> techo
    mt = [Materia("1", "A", 10, 8, "acreditada", 1),
          Materia("2", "B", 10, None, "pendiente", 0)]
    check("techo con una pendiente", promedio(mt, "simple", "ignora", 10.0), 9.0)

    # reprobada: 'ignora' no la cuenta, 'cuenta' sí
    mr = [Materia("1", "A", 10, 9, "acreditada", 1),
          Materia("2", "B", 10, 5, "reprobada", 1)]
    check("reprobada ignorada", promedio(mr, "simple", "ignora"), 9.0)
    check("reprobada contada", promedio(mr, "simple", "cuenta"), 7.0)
    # 'cuenta' + se aprueba con 9 -> (9 + 5 + 9)/3
    check("reprobada contada y luego aprobada con 9",
          promedio(mr, "simple", "cuenta", 9.0), (9 + 5 + 9) / 3)
    # 'ignora' + se aprueba con 9 -> (9 + 9)/2
    check("reprobada ignorada y luego aprobada con 9",
          promedio(mr, "simple", "ignora", 9.0), 9.0)

    # requerido: tengo 6 en una, quiero 8 con una pendiente -> necesito 10
    mq = [Materia("1", "A", 10, 6, "acreditada", 1),
          Materia("2", "B", 10, None, "pendiente", 0)]
    check("calificación requerida", requerido(mq, "simple", "ignora", 8.0), 10.0, tol=0.02)

    # meta imposible: techo 8, meta 9
    mi = [Materia("1", "A", 10, 6, "acreditada", 1),
          Materia("2", "B", 10, None, "pendiente", 0)]
    techo = promedio(mi, "simple", "ignora", 10.0)
    total[0] += 1
    print(f"  {'✅' if techo == 8.0 else '❌'} techo detectado = {techo} "
          f"(una meta de 9 debe declararse imposible)")
    if techo != 8.0:
        fallos.append("techo")

    # el impacto debe ser mayor para la materia de más créditos
    mimp = [Materia("1", "A", 20, None, "pendiente", 0),
            Materia("2", "B", 2, None, "pendiente", 0),
            Materia("3", "C", 10, 9, "acreditada", 1)]
    orden = impacto(mimp, "creditos", "ignora", 8.0)
    total[0] += 1
    ok = orden[0][0].nombre == "A"
    print(f"  {'✅' if ok else '❌'} impacto ordena por créditos: primero "
          f"{orden[0][0].nombre} (+{orden[0][1]})")
    if not ok:
        fallos.append("impacto")

    print()
    if fallos:
        print(f"❌ {len(fallos)} de {total[0]} prueba(s) fallida(s): "
              f"{', '.join(fallos)}")
        sys.exit(1)
    print(f"✅ Aritmética verificada: {total[0]} de {total[0]} pruebas correctas.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?", help="historial en CSV")
    ap.add_argument("--meta", type=float, help="promedio que se quiere alcanzar")
    ap.add_argument("--ponderacion", choices=("creditos", "simple", "ambas"),
                    default="ambas")
    ap.add_argument("--reprobadas", choices=("ignora", "cuenta", "ambas"),
                    default="ambas")
    ap.add_argument("--plantilla", action="store_true", help="imprime un CSV de ejemplo")
    ap.add_argument("--autotest", action="store_true", help="verifica la aritmética")
    args = ap.parse_args()

    if args.autotest:
        return autotest()
    if args.plantilla:
        print(PLANTILLA, end="")
        return
    if not args.csv:
        ap.print_help()
        print("\n⛔ Falta el historial. Genera la plantilla con --plantilla y llénala")
        print("   con los datos de SIAE [Panel de Control].pdf.")
        sys.exit(1)

    materias = leer(args.csv)
    ponds = ("creditos", "simple") if args.ponderacion == "ambas" else (args.ponderacion,)
    reprs = ("ignora", "cuenta") if args.reprobadas == "ambas" else (args.reprobadas,)

    if len(ponds) > 1 or len(reprs) > 1:
        print("\n⚠️  Se calculan varias combinaciones porque el reglamento no está")
        print("    confirmado. Las dos preguntas que hay que resolver:")
        print("      1. ¿La reprobada sigue contando en el promedio tras aprobar?")
        print("      2. ¿El promedio se pondera por créditos?")
        print("    Están en REGLAMENTO EXTRAORDINARIOS.pdf y en el Reglamento General")
        print("    de Exámenes. Hasta entonces, ninguna cifra de abajo es definitiva.\n")

    for p in ponds:
        for r in reprs:
            print()
            informe(materias, p, r, args.meta)


if __name__ == "__main__":
    main()
