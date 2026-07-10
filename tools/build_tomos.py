#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la edición en DOS TOMOS (para imprenta) reutilizando la maquinaria de build_libro.
Tomo I  : Fundamentos + Civil Profundo + Mercantil.
Tomo II : Corporate + Maestría + Ramas Esenciales + Anexos (Formatos y Jurisprudencia).
Salida: LIBRO/Tomo-I-...html y LIBRO/Tomo-II-...html
"""
import os
import build_libro as B   # al importar, regenera también el libro completo (ok)

FECHA = B.FECHA

# CSS extra: etiqueta de lomo + saltos de tomo
CSS = B.CSS + r"""
.tomo-label{ font-variant:small-caps; letter-spacing:.14em; color:var(--accent); font-size:1.15rem; margin:.6em 0;}
.lomo-wrap{ text-align:center; margin:1.4em 0;}
.lomo{ display:inline-block; writing-mode:vertical-rl; transform:rotate(180deg);
 border:1.4px solid var(--ink); padding:1.2cm .35cm; height:22cm; font-variant:small-caps;
 letter-spacing:.18em; font-size:.95rem; background:var(--paper);}
.fintomo{ text-align:center; min-height:20cm; display:flex; flex-direction:column; justify-content:center;}
"""

def cover(tomo_rom, tomo_titulo, partes_desc):
    return f"""<section class="page portada">
 {B.escudo('grande')}
 <div class="univ">Universidad Nacional Autónoma de México</div>
 <div class="facultad">Facultad de Estudios Superiores Aragón</div>
 <div class="filete"></div>
 <div class="titulo">Manual para Ejercer<br>el Derecho Corporativo</div>
 <div class="tomo-label">Tomo {tomo_rom} — {tomo_titulo}</div>
 <div class="subtitulo">{partes_desc}</div>
 <div class="filete"></div>
 <div class="edicion">Edición ampliada · con los Suplementos del Consejo Editorial</div>
 <div class="autor">Elias Alejo</div>
 <div class="sello">Biblioteca Jurídica AJE</div>
 <div class="fecha">{FECHA}</div>
</section>"""

def como_usar():
    return """<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Cómo usar este libro con las fuentes digitales</h2>
 <p class="dropcap">Este Manual es la mitad de tu sistema de estudio; la otra mitad vive —y debe vivir— en
 formato digital. La regla que lo gobierna es el símbolo <strong>⟳</strong>: <em>lo estable se imprime; lo
 que cambia se consulta vivo.</em></p>
 <h3>Imprime y conserva en papel</h3>
 <p>Este libro: la <strong>doctrina, el criterio y los Suplementos del Consejo Editorial</strong>. Es
 conocimiento que no caduca; en papel se subraya, se anota al margen y se retiene mejor. Léelo con un lápiz en la mano.</p>
 <h3>Consulta siempre en digital (nunca lo imprimas)</h3>
 <ul>
 <li><strong>Las 27 leyes</strong> (carpeta <code>fuentes-legales/</code>): cambian cada año. Cítalas solo
 desde su <strong>texto vigente</strong> (DOF / Cámara de Diputados). Imprimir la ley es traicionar al ⟳.</li>
 <li><strong>La jurisprudencia:</strong> verifica cada criterio en el <strong>Semanario Judicial de la
 Federación</strong> (sjf.scjn.gob.mx): registro, época y vigencia.</li>
 <li><strong>Los formatos</strong> del Anexo A: en digital los <strong>llenas y editas</strong>; el papel solo se lee.</li>
 </ul>
 <h3>El método</h3>
 <p>Estudia en el sillón con el <strong>libro</strong>; ejerce en el escritorio con la <strong>fuente viva</strong>
 al lado. Cuando un artículo del libro lleve ⟳, ábrelo en el código antes de citarlo. Ese hábito —repetido mil
 veces— es lo que separa al abogado en quien se confía del que cita de memoria.</p>
 <div class="ornamento"></div>
</section>"""

def indice_tomo(labels, titulo):
    parts=[f'<section class="page nueva-pagina toc"><h2 class="seccion-titulo">{titulo}</h2>']
    for plabel,ptitle,entries in B.toc:
        if plabel not in labels: continue
        parts.append(f'<h3>{plabel} — {ptitle}</h3><ul>')
        for t,a in entries:
            parts.append(f'<li><a href="#{a}">{t}</a></li>')
        parts.append("</ul>")
    parts.append("</section>")
    return "".join(parts)

def lomo(tomo_rom, tomo_titulo):
    return f"""<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Etiqueta de lomo</h2>
 <p style="text-align:center;max-width:30em;margin:0 auto;">Para encuadernar: imprime esta página, recorta la
 franja y pégala en el lomo del tomo. Ajusta el largo al grosor real del volumen encuadernado.</p>
 <div class="lomo-wrap"><div class="lomo">MANUAL PARA EJERCER EL DERECHO CORPORATIVO&nbsp;&nbsp;·&nbsp;&nbsp;TOMO {tomo_rom}: {tomo_titulo}&nbsp;&nbsp;·&nbsp;&nbsp;ELIAS ALEJO</div></div>
</section>"""

def fin_tomo(txt):
    return f"""<section class="page nueva-pagina fintomo">{B.escudo('mediano')}<div class="filete"></div>
 <p style="font-variant:small-caps;letter-spacing:.1em;">{txt}</p><div class="ornamento"></div></section>"""

def chapters_of(labels):
    out=[]
    for plabel,ptitle,cap_title,anchor,html,is_first in B.chapters:
        if plabel not in labels: continue
        if is_first: out.append(B.parte_portada(plabel,ptitle))
        out.append(B.capitulo(plabel,cap_title,anchor,html))
    return out

def wrap(title, body):
    barra='<div id="barra"><button onclick="window.print()">📖 Generar PDF / Imprimir</button></div>'
    return (f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title><style>{CSS}</style></head><body>{barra}{"".join(body)}</body></html>')

# ---------- TOMO I ----------
t1 = [cover("I","Fundamentos, Civil y Mercantil",
            "Parte I · Fundamentos del Derecho — Parte II · Derecho Civil Profundo — Parte III · Derecho Mercantil"),
      B.pagina_legal(), B.dedicatoria(), B.consideraciones(), B.finalidad(), B.estructura(), como_usar(),
      indice_tomo(["Parte I","Parte II","Parte III"], "Índice del Tomo I")]
t1 += chapters_of(["Parte I","Parte II","Parte III"])
t1 += [fin_tomo("Fin del Tomo I · continúa en el Tomo II"), lomo("I","Fundamentos, Civil y Mercantil")]
open("LIBRO/Tomo-I-Fundamentos-Civil-Mercantil.html","w",encoding="utf-8").write(
    wrap("Manual para Ejercer el Derecho Corporativo — Tomo I", t1))

# ---------- TOMO II ----------
t2 = [cover("II","Corporate, Maestría y Ramas Esenciales",
            "Parte IV · Derecho Corporativo — Parte V · Maestría — Parte VI · Ramas Esenciales — Anexos"),
      indice_tomo(["Parte IV","Parte V","Parte VI","Anexo A","Anexo B"], "Índice del Tomo II")]
t2 += chapters_of(["Parte IV","Parte V","Parte VI"])
# Anexo A: Formatos
if B.anexo:
    t2.append(B.parte_portada("Anexo A","Banco de Formatos"))
    for t,a,h in B.anexo: t2.append(B.capitulo("Anexo A",t,a,h))
# Anexo B: Jurisprudencia
if B.anexo_juris:
    t2.append(B.parte_portada("Anexo B","Banco de Jurisprudencia"))
    for t,a,h in B.anexo_juris: t2.append(B.capitulo("Anexo B",t,a,h))
t2 += [B.colofon(), lomo("II","Corporate, Maestría y Ramas")]
open("LIBRO/Tomo-II-Corporate-Maestria-Ramas.html","w",encoding="utf-8").write(
    wrap("Manual para Ejercer el Derecho Corporativo — Tomo II", t2))

print("OK tomos generados:",
      os.path.getsize("LIBRO/Tomo-I-Fundamentos-Civil-Mercantil.html")//1024,"KB (I) +",
      os.path.getsize("LIBRO/Tomo-II-Corporate-Maestria-Ramas.html")//1024,"KB (II)")
