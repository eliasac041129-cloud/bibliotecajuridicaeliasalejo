# -*- coding: utf-8 -*-
"""Genera el libro en FORMATO DE IMPRENTA (PDF paginado real) con WeasyPrint.

A diferencia de build_libro.py —que produce un HTML para leer en pantalla— este
script produce un PDF con caja tipográfica de libro: medida real de página,
márgenes espejeados (interior/exterior), cabeceras corridas, folios, capítulos
que abren en página impar y partición silábica española.

Uso:
    python3 tools/build_impreso.py --formato lectura --tomos 3
    python3 tools/build_impreso.py --listar-formatos
    python3 tools/build_impreso.py --calibrar          # mide sin generar todo

Salida: IMPRENTA/*.pdf
"""
import os, re, sys, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
os.chdir(ROOT)

TITULO = "Manual para Ejercer el Derecho Corporativo"
AUTOR = "Elias Alejo"
SALIDA = "IMPRENTA"

# build_libro.py aporta el contenido ya convertido a HTML (capítulos, anexos,
# preliminares). Solo escribe archivos cuando se ejecuta directamente.
import build_libro as BL
FECHA = BL.FECHA
BL_ESCUDO = BL.escudo("grande")

# ---------------------------------------------------------------------------
# FORMATOS
# ---------------------------------------------------------------------------
# ancho/alto  : medida final del libro cerrado (mm)
# cols        : columnas del cuerpo de texto
# pt / leading: cuerpo tipográfico y interlínea (múltiplo del cuerpo)
# int/ext     : margen interior (lomo) y exterior (para anotar), mm
# sup/inf     : margen superior e inferior, mm
FORMATOS = {
    "lectura": dict(
        nombre="Lectura y anotación",
        descripcion="Una columna, cuerpo grande y margen exterior ancho para subrayar y anotar. "
                    "Las tablas y los diagramas caben a todo lo ancho.",
        ancho=155, alto=230, cols=1, pt=10.5, leading=1.36,
        interior=18, exterior=26, superior=17, inferior=20,
    ),
    "academico": dict(
        nombre="Tratado académico",
        descripcion="Una columna con medida más apretada. Menos páginas que 'lectura', "
                    "conservando legibilidad; margen exterior suficiente para notas breves.",
        ancho=155, alto=230, cols=1, pt=10.0, leading=1.30,
        interior=17, exterior=19, superior=16, inferior=18,
    ),
    "manual": dict(
        nombre="Manual de cátedra",
        descripcion="Formato de libro de texto, dos columnas. El más compacto en número de "
                    "páginas, pero las tablas anchas sufren y el margen para anotar es escaso.",
        ancho=170, alto=240, cols=2, pt=10.0, leading=1.32,
        interior=19, exterior=17, superior=17, inferior=20,
    ),
    "compacto": dict(
        nombre="Compacto",
        descripcion="Dos columnas, cuerpo pequeño, casi papel biblia. Mínimo grosor, "
                    "pero se subraya mal y se anota peor.",
        ancho=140, alto=210, cols=2, pt=8.8, leading=1.22,
        interior=15, exterior=13, superior=13, inferior=16,
    ),
}

# Calibre real por hoja (mm). Fuente: fichas técnicas de papel de librería.
PAPELES = [
    ("Papel biblia 40 g (alta opacidad)", 0.050, "No — el marcador traspasa"),
    ("Offset ahuesado 60 g",              0.078, "Sí, con lápiz y bolígrafo fino"),
    ("Offset ahuesado 70 g",              0.092, "Sí — recomendado"),
    ("Offset ahuesado 80 g",              0.105, "Sí, incluso con marcador"),
    ("Bond blanco 90 g (print on demand)", 0.114, "Sí, pero abulta"),
]
TAPA_MM = 6.0  # tapa dura: 2 cartones de 2 mm + guardas + redondeo de lomo


def css_impreso(F):
    """Construye la hoja de estilo de imprenta para un formato dado."""
    cuerpo_cols = ""
    if F["cols"] > 1:
        cuerpo_cols = f"column-count:{F['cols']}; column-gap:6mm; column-fill:auto;"

    return f"""
@page {{
  size: {F['ancho']}mm {F['alto']}mm;
  margin: {F['superior']}mm {F['exterior']}mm {F['inferior']}mm {F['interior']}mm;
}}
/* márgenes espejeados: el interior siempre pegado al lomo */
@page :right {{
  margin-left: {F['interior']}mm; margin-right: {F['exterior']}mm;
  @top-right   {{ content: string(captitulo); font-size:7.6pt; font-variant:small-caps;
                 letter-spacing:.06em; color:#5d5344; }}
  @bottom-right{{ content: counter(page); font-size:8pt; color:#3d3629; }}
}}
@page :left {{
  margin-left: {F['exterior']}mm; margin-right: {F['interior']}mm;
  @top-left    {{ content: "{TITULO}"; font-size:7.6pt; font-variant:small-caps;
                 letter-spacing:.06em; color:#5d5344; }}
  @bottom-left {{ content: counter(page); font-size:8pt; color:#3d3629; }}
}}
/* páginas sin cabecera ni folio: portada, portadillas, colofón, blancas */
@page limpia {{ @top-right{{content:none}} @top-left{{content:none}}
                @bottom-right{{content:none}} @bottom-left{{content:none}} }}

html {{ font-size: {F['pt']}pt; }}
/* Noto Serif para el texto; DejaVu Serif cubre ⟳ (U+27F3, 1,581 apariciones)
   y los símbolos del semáforo, que Noto Serif no trae. */
body {{
  font-family: "Noto Serif","DejaVu Serif","Noto Sans Symbols 2","Noto Emoji",serif;
  font-size: {F['pt']}pt; line-height: {F['leading']};
  color:#14110c; margin:0; text-align:justify;
  hyphens:auto; -webkit-hyphens:auto;
}}
p {{ margin:0 0 .30em; text-indent:1.1em; orphans:2; widows:2; }}
p.dropcap, h1+p, h2+p, h3+p, h4+p, blockquote p, td p, li p {{ text-indent:0; }}

h1,h2,h3,h4 {{ font-weight:700; line-height:1.16; break-after:avoid-page; }}
h2 {{ font-size:1.06em; margin:.95em 0 .28em; }}
h3 {{ font-size:.97em; margin:.75em 0 .22em; color:#6b1420;
      font-variant:small-caps; letter-spacing:.03em; }}
h4 {{ font-size:.92em; margin:.6em 0 .18em; font-style:italic; font-weight:600; }}

/* --- capítulo --- */
.page {{ }}
section.cap {{ break-before: right; page: normal; }}
.cap-num {{ font-variant:small-caps; letter-spacing:.14em; font-size:.78em;
            color:#6b1420; margin:0 0 .2em; text-align:left; }}
h1.cap-titulo {{ font-size:1.5em; margin:.05em 0 .8em; padding-bottom:.22em;
                 border-bottom:.6pt solid #b9b2a4; text-align:left;
                 string-set: captitulo content(); }}
.cuerpo {{ {cuerpo_cols} }}

/* --- tablas: reglas horizontales, a todo el ancho de la caja --- */
table {{ border-collapse:collapse; width:100%; margin:.55em 0;
         font-size:.83em; line-height:1.22;
         border-top:.9pt solid #14110c; border-bottom:.9pt solid #14110c;
         break-inside:avoid; }}
th,td {{ padding:.24em .45em; text-align:left; vertical-align:top; border:0; }}
thead th {{ border-bottom:.5pt solid #14110c; font-variant:small-caps; }}
tbody tr {{ border-bottom:.3pt solid #cdc7ba; }}
tbody tr:last-child {{ border-bottom:0; }}

blockquote {{ margin:.45em 0 .45em .8em; padding-left:.7em;
              border-left:1.2pt solid #6b1420; font-size:.93em;
              line-height:1.28; text-align:left; break-inside:avoid; }}
/* Los 201 diagramas son arte ASCII: NO deben ajustar línea, o el dibujo se
   destruye. Cada bloque recibe su propio cuerpo, calculado para que su línea
   más larga quepa en la medida (ver ajustar_diagramas). */
pre {{ border:.5pt solid #cdc7ba; background:#f4f1ea; padding:1.2mm 1.4mm;
       margin:.6em 0; font-family:"DejaVu Sans Mono","Liberation Mono",monospace;
       line-height:1.2; white-space:pre; break-inside:avoid; }}
code {{ font-family:"DejaVu Sans Mono","Liberation Mono",monospace; font-size:.86em; }}
/* párrafo formado solo por fragmentos de código: sin justificar (evita ríos) */
p.solo-codigo {{ text-align:left; hyphens:none; }}
pre code {{ font-size:inherit; }}
ul,ol {{ margin:.25em 0 .45em 1.15em; padding:0; }}
li {{ margin:.06em 0; text-align:justify; }}
hr {{ border:0; border-top:.5pt solid #cdc7ba; margin:.7em 0; }}
a {{ color:inherit; text-decoration:none; }}
strong {{ font-weight:700; }}
img, svg {{ max-width:100%; }}

/* --- preliminares y páginas de aparato --- */
section.preliminar {{ break-before: right; page: limpia; }}
.seccion-titulo {{ text-align:center; font-variant:small-caps; letter-spacing:.1em;
                   font-size:1.32em; margin:.2em 0 1em; border:0; }}
.carta {{ font-size:1.0em; line-height:1.48; }}
.firma {{ text-align:right; font-style:italic; margin-top:1.1em; text-indent:0; }}
.frase-vida {{ text-align:center; font-style:italic; font-size:1.02em; color:#6b1420;
               border-top:.5pt solid #cdc7ba; border-bottom:.5pt solid #cdc7ba;
               padding:.7em .4em; margin:1.1em 0; text-indent:0; }}
.dropcap:first-letter {{ float:left; font-size:2.4em; line-height:.82;
                         padding:.02em .09em 0 0; color:#6b1420; font-weight:700; }}
.ornamento {{ text-align:center; color:#6b1420; margin:.6em 0;
              font-size:.8em; letter-spacing:.5em; }}
.filete {{ width:38%; height:0; border-top:.6pt solid #6b1420; margin:.8em auto; }}

section.portada, section.parte-portada, section.colofon {{
  break-before: right; page: limpia; text-align:center;
  hyphens:none; -webkit-hyphens:none; }}
section.portada {{ padding-top:14%; }}
.portada .univ {{ font-variant:small-caps; letter-spacing:.16em; font-size:.95em; }}
.portada .facultad {{ font-variant:small-caps; letter-spacing:.1em; font-size:.82em;
                      color:#4a4133; margin-bottom:1.4em; }}
.portada .titulo {{ font-size:2.05em; line-height:1.12; margin:.3em 0; font-weight:700; }}
.portada .subtitulo {{ font-size:.95em; font-style:italic; margin:.8em 0 0;
                       text-align:center; text-indent:0; }}
.portada .especialidad {{ font-variant:small-caps; letter-spacing:.05em; color:#6b1420;
                          font-size:.9em; margin:1em 0 0; }}
.portada .edicion {{ font-variant:small-caps; letter-spacing:.05em; color:#4a4133;
                     font-size:.8em; margin:.7em 0 0; line-height:1.4; }}
.portada .autor {{ margin-top:2.4em; font-size:1.15em; font-variant:small-caps;
                   letter-spacing:.08em; }}
.portada .sello {{ font-size:.86em; color:#4a4133; }}
.portada .fecha {{ font-style:italic; color:#4a4133; font-size:.9em; margin-top:.3em; }}
.parte-portada {{ padding-top:32%; }}
.parte-portada .plabel {{ font-variant:small-caps; letter-spacing:.24em;
                          color:#6b1420; font-size:1em; }}
.parte-portada .ptitulo {{ font-size:1.6em; margin-top:.25em; font-weight:700; }}
.escudo svg {{ display:block; margin:0 auto; }}
.escudo.grande svg {{ width:78px; }}
.escudo.mediano svg {{ width:54px; }}

/* --- índice --- */
.toc {{ font-size:.94em; }}
.toc h3 {{ color:#6b1420; font-variant:small-caps; margin-top:.9em; }}
.toc ul {{ list-style:none; margin-left:0; }}
.toc li {{ border-bottom:.3pt dotted #cdc7ba; padding:.1em 0; text-align:left; }}
#barra {{ display:none; }}
"""


# ---------------------------------------------------------------------------
import html as _html

# Anchura de avance de DejaVu Sans Mono, en fracción del cuerpo (em).
AVANCE_MONO = 0.6023
CUERPO_MINIMO_PRE = 5.0   # pt: por debajo de esto un diagrama deja de leerse


def medida_pt(F):
    """Ancho útil de la columna de texto, en puntos."""
    ancho_mm = F["ancho"] - F["interior"] - F["exterior"]
    if F["cols"] > 1:
        ancho_mm = (ancho_mm - 6 * (F["cols"] - 1)) / F["cols"]
    return ancho_mm * 72 / 25.4


def ajustar_diagramas(s, F):
    """Da a cada <pre> el cuerpo tipográfico con que su línea más larga cabe.

    Un tamaño global no sirve: la mediana de los diagramas mide 74 caracteres de
    ancho pero el más grande mide 123. Con un cuerpo único, o los estrechos salen
    ridículamente pequeños o los anchos se desbordan.
    """
    disponible = medida_pt(F) - 2 * (1.4 * 72 / 25.4) - 2   # padding y borde
    techo = F["pt"] * 0.80

    def uno(m):
        cuerpo_txt = _html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        largo = max((len(l) for l in cuerpo_txt.split("\n")), default=1) or 1
        pt = disponible / (largo * AVANCE_MONO)
        pt = max(CUERPO_MINIMO_PRE, min(techo, pt))
        return f'<pre style="font-size:{pt:.2f}pt"{m.group(1)}>{m.group(2)}</pre>'

    return re.sub(r"<pre([^>]*)>(.*?)</pre>", uno, s, flags=re.S)


def marcar_parrafos_codigo(s):
    """No justifica los párrafos que son mayoritariamente <code>.

    Justificar monoespaciado abre ríos blancos enormes, porque la fuente no puede
    condensar. Se marcan los párrafos en que el código pesa 60% o más del texto.
    """
    limpio = lambda x: re.sub(r"<[^>]+>|\s", "", x)

    def uno(m):
        interior = m.group(1)
        if interior.count("<code>") < 2:
            return m.group(0)
        en_codigo = sum(len(limpio(c)) for c in
                        re.findall(r"<code>(.*?)</code>", interior, flags=re.S))
        total = len(limpio(interior))
        if total and en_codigo / total >= 0.60:
            return f'<p class="solo-codigo">{interior}</p>'
        return m.group(0)

    return re.sub(r"<p>(.*?)</p>", uno, s, flags=re.S)


def preparar(secciones, F):
    """Adapta el HTML de pantalla al HTML de imprenta (clases de página)."""
    out = []
    for s in secciones:
        s = ajustar_diagramas(s, F)
        s = marcar_parrafos_codigo(s)
        s = s.replace('class="page nueva-pagina toc"', 'class="preliminar toc"')
        s = s.replace('class="page portada"', 'class="portada"')
        s = s.replace('class="page nueva-pagina parte-portada"', 'class="parte-portada"')
        s = s.replace('class="page nueva-pagina colofon portada"', 'class="colofon"')
        s = s.replace('class="page nueva-pagina"', 'class="preliminar"')
        # los capítulos llevan id="cap-N": esos sí son cuerpo del libro
        s = re.sub(r'class="preliminar" id="(cap-\d+)"', r'class="cap" id="\1"', s)
        out.append(s)
    return out


def documento(secciones, F, titulo=TITULO):
    html = (f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
            f'<title>{titulo}</title></head><body>{"".join(secciones)}</body></html>')
    from weasyprint import HTML, CSS
    return HTML(string=html, base_url=ROOT).render(stylesheets=[CSS(string=css_impreso(F))])


def grosor(paginas):
    hojas = (paginas + 1) // 2
    filas = []
    for nombre, calibre, subrayable in PAPELES:
        lomo = hojas * calibre
        filas.append((nombre, lomo, lomo + TAPA_MM, subrayable))
    return hojas, filas


def repartir(caps, n):
    """Reparte los capítulos en n tomos minimizando el tomo más gordo.

    Partición lineal por programación dinámica: conserva el orden de la obra
    (indispensable, la escalera I→VI supone cada nivel anterior) y equilibra por
    volumen de texto. El reparto ingenuo por 'partes' completas dejaba un tomo
    con 741 páginas frente a otro de 499, porque el Nivel I tiene 13 capítulos
    y el Nivel II solo 4.
    """
    if n <= 1:
        return [list(caps)]
    peso = [len(re.sub(r"<[^>]+>", " ", c[4])) for c in caps]
    m = len(caps)
    n = min(n, m)
    # acumulado para sumar rangos en O(1)
    ac = [0]
    for w in peso:
        ac.append(ac[-1] + w)
    rango = lambda i, j: ac[j] - ac[i]

    INF = float("inf")
    # mejor[k][i] = mínimo del máximo al partir caps[i:] en k tomos
    mejor = [[INF] * (m + 1) for _ in range(n + 1)]
    corte = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(m + 1):
        mejor[1][i] = rango(i, m)
    for k in range(2, n + 1):
        for i in range(m - k + 1, -1, -1):
            for j in range(i + 1, m - k + 2):
                peor = max(rango(i, j), mejor[k - 1][j])
                if peor < mejor[k][i]:
                    mejor[k][i] = peor
                    corte[k][i] = j
    tomos, i = [], 0
    for k in range(n, 1, -1):
        j = corte[k][i]
        tomos.append(list(caps[i:j])); i = j
    tomos.append(list(caps[i:]))
    return tomos


def portada_tomo(romano, subtitulo, n_caps):
    return f"""<section class="portada">
 {BL_ESCUDO}
 <div class="univ">Universidad Nacional Autónoma de México</div>
 <div class="facultad">Facultad de Estudios Superiores Aragón</div>
 <div class="filete"></div>
 <div class="titulo">{TITULO.replace('para Ejercer', 'para Ejercer<br>')}</div>
 <div class="especialidad">Tomo {romano}</div>
 <div class="subtitulo">{subtitulo}</div>
 <div class="edicion">{n_caps} capítulos · Edición Final, voz consolidada</div>
 <div class="autor">{AUTOR}</div>
 <div class="sello">Biblioteca Jurídica AJE</div>
 <div class="fecha">{FECHA}</div>
 <div class="filete"></div>
</section>"""


def indice_tomo(caps_t, romano):
    """Índice del tomo: solo sus capítulos, agrupados por parte."""
    partes = []
    for plabel, ptitle, t, a, hh, first in caps_t:
        if not partes or partes[-1][0] != ptitle:
            partes.append((ptitle, plabel, []))
        partes[-1][2].append(t)
    out = [f'<section class="preliminar toc">'
           f'<h2 class="seccion-titulo">Índice del Tomo {romano}</h2>']
    for ptitle, plabel, titulos in partes:
        out.append(f"<h3>{plabel} — {ptitle}</h3><ul>")
        out += [f"<li>{t}</li>" for t in titulos]
        out.append("</ul>")
    out.append("</section>")
    return "".join(out)


def informe(etiqueta, paginas, F):
    hojas, filas = grosor(paginas)
    print(f"\n  {etiqueta}")
    print(f"    páginas: {paginas:,}   hojas: {hojas:,}   "
          f"medida: {F['ancho']}×{F['alto']} mm")
    for nombre, lomo, total, sub in filas:
        print(f"      {nombre:38s} lomo {lomo/10:5.2f} cm  "
              f"con tapa {total/10:5.2f} cm   subrayable: {sub}")


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--formato", default="lectura", choices=list(FORMATOS))
    ap.add_argument("--tomos", type=int, default=3,
                    help="en cuántos volúmenes repartir la obra (1 = un solo tomo)")
    ap.add_argument("--listar-formatos", action="store_true")
    ap.add_argument("--calibrar", action="store_true",
                    help="mide todos los formatos sobre una muestra y extrapola")
    ap.add_argument("--muestra", type=int, default=0,
                    help="usar solo los primeros N capítulos (pruebas)")
    args = ap.parse_args()

    if args.listar_formatos:
        for k, F in FORMATOS.items():
            print(f"\n{k}  —  {F['nombre']}  ({F['ancho']}×{F['alto']} mm, "
                  f"{F['cols']} col., {F['pt']} pt)")
            print(f"    {F['descripcion']}")
        return

    if args.calibrar:
        # mide 6 capítulos representativos y extrapola al total
        muestra = [BL.capitulo(p, t, a, h)
                   for p, pt, t, a, h, f in BL.chapters[::9]][:6]
        import html as _h
        chars_muestra = len(re.sub(r"\s+", " ", _h.unescape(
            re.sub(r"<[^>]+>", " ", "".join(muestra)))))
        chars_total = sum(
            len(re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", " ",
                BL.capitulo(p, t, a, hh)))))
            for p, pt, t, a, hh, f in BL.chapters)
        print(f"Calibración sobre {len(muestra)} capítulos "
              f"({chars_muestra:,} de {chars_total:,} caracteres)")
        for k, F in FORMATOS.items():
            doc = documento(preparar(muestra, F), F)
            pag_m = len(doc.pages)
            estimado = round(pag_m * chars_total / chars_muestra)
            print(f"\n{k:11s} {F['nombre']:24s} "
                  f"muestra {pag_m:4d} pág.  →  obra completa ≈ {estimado:,} pág.")
            informe(f"un solo tomo ({k})", estimado, F)
        return

    F = FORMATOS[args.formato]
    os.makedirs(SALIDA, exist_ok=True)
    caps = BL.chapters[:args.muestra] if args.muestra else BL.chapters

    print(f"Formato: {args.formato} — {F['nombre']} "
          f"({F['ancho']}×{F['alto']} mm, {F['cols']} col., {F['pt']} pt)")
    print(f"Tomos: {args.tomos}")

    tomos = repartir(caps, args.tomos)

    total_pag = 0
    for i, caps_t in enumerate(tomos, 1):
        romano = ["", "I", "II", "III", "IV", "V", "VI"][i]
        # las partes que ese tomo contiene, en orden de aparición
        nombres = list(dict.fromkeys(c[1] for c in caps_t))
        subtitulo = " · ".join(nombres)
        sec = []
        if len(tomos) == 1:
            sec.append(BL.portada())
        else:
            sec.append(portada_tomo(romano, subtitulo, len(caps_t)))
        if i == 1:
            sec += [BL.pagina_legal(), BL.dedicatoria(),
                    BL.consideraciones(), BL.finalidad(), BL.estructura()]
        sec.append(indice_tomo(caps_t, romano))
        cur = None
        for plabel, ptitle, t, a, hh, first in caps_t:
            if ptitle != cur:
                sec.append(BL.parte_portada(plabel, ptitle)); cur = ptitle
            sec.append(BL.capitulo(plabel, t, a, hh))
        if i == len(tomos):
            if BL.anexo:
                sec.append(BL.parte_portada("Anexo A", "Banco de Formatos"))
                for t, a, hh in BL.anexo:
                    sec.append(BL.capitulo("Anexo A", t, a, hh))
            if BL.anexo_juris:
                sec.append(BL.parte_portada("Anexo B", "Banco de Jurisprudencia"))
                for t, a, hh in BL.anexo_juris:
                    sec.append(BL.capitulo("Anexo B", t, a, hh))
        sec.append(BL.colofon())

        etiq = TITULO if args.tomos == 1 else f"{TITULO} — Tomo {romano}"
        doc = documento(preparar(sec, F), F, etiq)
        pag = len(doc.pages); total_pag += pag
        slug = "Manual-Completo" if args.tomos == 1 else f"Tomo-{romano}"
        destino = os.path.join(SALIDA, args.formato)
        os.makedirs(destino, exist_ok=True)
        ruta = os.path.join(destino, f"{slug}.pdf")
        doc.write_pdf(ruta)
        informe(f"{etiq}  ({len(caps_t)} capítulos)  →  {ruta}", pag, F)

    if len(tomos) > 1:
        print(f"\n  CONJUNTO: {len(tomos)} tomos, {total_pag:,} páginas en total")
        hojas, filas = grosor(total_pag)
        for nombre, lomo, tot, sub in filas:
            print(f"      {nombre:38s} suma de lomos {(lomo+TAPA_MM*len(tomos))/10:5.2f} cm")


if __name__ == "__main__":
    main()
