#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compila toda la Biblioteca en un LIBRO HTML imprimible (estilo Porrúa).
Genera: LIBRO/Manual-para-Ejercer-el-Derecho-Corporativo.html
"""
import os, re, glob, datetime
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FECHA = "Julio de 2026"

# ---------- escudo UNAM inline ----------
svg = open("LIBRO/assets/escudo-unam.svg", encoding="utf-8").read()
svg = re.sub(r"<\?xml.*?\?>", "", svg, flags=re.DOTALL)
svg = re.sub(r"<!--.*?-->", "", svg, flags=re.DOTALL)
svg = svg.strip()
# capturar width/height originales para crear viewBox (el SVG no lo trae)
_m = re.search(r"<svg\b(.*?)>", svg, re.DOTALL)
_tag = _m.group(1)
_w = re.search(r'width="([\d.]+)', _tag); _h = re.search(r'height="([\d.]+)', _tag)
_W = _w.group(1) if _w else "1024"; _H = _h.group(1) if _h else "1151"
# quitar width/height fijos y añadir viewBox para que escale con CSS
_newtag = re.sub(r'\s(width|height)="[^"]*"', "", _tag)
if "viewBox" not in _newtag:
    _newtag = f' viewBox="0 0 {_W} {_H}"' + _newtag
svg = svg[:_m.start()] + "<svg" + _newtag + ">" + svg[_m.end():]
def escudo(cls):
    return f'<div class="escudo {cls}">{svg}</div>'

# ---------- conversión markdown -> HTML ----------
MD = markdown.Markdown(extensions=["tables","fenced_code","sane_lists","attr_list","toc","md_in_html"])
def md2html(text):
    # permitir markdown dentro de los <div align="center"> (títulos de formatos)
    text = text.replace('<div align="center">', '<div align="center" markdown="1">')
    MD.reset()
    html = MD.convert(text)
    # neutralizar enlaces internos (.md, carpetas) -> texto plano; conservar http
    html = re.sub(r'<a href="(?!https?://)[^"]*">(.*?)</a>', r"\1", html, flags=re.DOTALL)
    return html

def first_h1(text):
    for ln in text.split("\n"):
        if ln.startswith("# "):
            return ln[2:].strip()
    return "(sin título)"

def strip_h1(text):
    out=[]; done=False
    for ln in text.split("\n"):
        if not done and ln.startswith("# "):
            done=True; continue
        out.append(ln)
    return "\n".join(out)

# ---------- estructura del libro ----------
PARTES = [
 ("Parte I", "Fundamentos del Derecho", "Nivel-I-Fundamentos"),
 ("Parte II", "Derecho Civil Profundo", "Nivel-II-Derecho-Civil-Profundo"),
 ("Parte III", "Derecho Mercantil", "Nivel-III-Derecho-Mercantil"),
 ("Parte IV", "Derecho Corporativo (Corporate Law)", "Nivel-IV-Corporate-Law"),
 ("Parte V", "Maestría: Negociación, Finanzas y Estrategia", "Nivel-V-Maestria"),
 ("Parte VI", "Ramas Esenciales del Ejercicio", "Ramas-Esenciales"),
]

chapters=[]   # (parte_label, parte_title, cap_title, anchor, html, is_part_start)
cap_n=0
toc=[]        # (parte_label, parte_title, [(cap_title, anchor)])
for plabel, ptitle, folder in PARTES:
    base=os.path.join("Columna-I-Biblioteca", folder)
    files=sorted(glob.glob(os.path.join(base,"*.md")))
    files=[f for f in files if os.path.basename(f).lower()!="readme.md"]
    entries=[]
    first=True
    for f in files:
        txt=open(f,encoding="utf-8").read()
        title=first_h1(txt)
        cap_n+=1
        anchor=f"cap-{cap_n}"
        html=md2html(strip_h1(txt))
        chapters.append((plabel,ptitle,title,anchor,html,first))
        entries.append((title,anchor))
        first=False
    toc.append((plabel,ptitle,entries))

# Anexo: Banco de Formatos
anexo=[]
for f in sorted(glob.glob("Banco-de-Formatos/*.md")):
    if os.path.basename(f).lower()=="readme.md": continue
    txt=open(f,encoding="utf-8").read()
    title=first_h1(txt); cap_n+=1; anchor=f"cap-{cap_n}"
    anexo.append((title,anchor,md2html(strip_h1(txt))))
toc.append(("Anexo A","Banco de Formatos",[(t,a) for t,a,_ in anexo]))

# ---------- CSS estilo Porrúa ----------
CSS = r"""
:root{ --ink:#1a1610; --accent:#6b1420; --paper:#fdfbf6; --rule:#cdc7ba; --tint:#f1eee7; }
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#dedacf;color:var(--ink);
 font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Palatino,Georgia,"Times New Roman",serif;
 font-size:10pt;line-height:1.38;}
.page{background:var(--paper);width:15.6cm;margin:16px auto;padding:1.5cm 1.5cm;
 box-shadow:0 3px 14px rgba(0,0,0,.22);position:relative;}
p{ text-align:justify; hyphens:auto; margin:0 0 .38em; }
h1,h2,h3,h4{ font-weight:700; line-height:1.18; color:var(--ink); }
h2{ font-size:1.08rem; margin:1em 0 .3em; letter-spacing:.01em;}
h3{ font-size:.97rem; margin:.8em 0 .25em; color:var(--accent); font-variant:small-caps; letter-spacing:.03em;}
h4{ font-size:.9rem; margin:.65em 0 .2em; font-style:italic; font-weight:600;}
a{ color:var(--accent); text-decoration:none;}
strong{font-weight:700;} em{font-style:italic;}

/* CUERPO A DOS COLUMNAS (libro real) */
.cuerpo{ column-count:2; column-gap:.85cm; }
.cuerpo table, .cuerpo pre, .cuerpo figure { column-span:all; }

/* blockquote formal: sin caja, solo filete fino */
blockquote{ margin:.5em 0; padding:.05em 0 .05em .7em; border-left:2px solid var(--accent);
 font-size:.9em; line-height:1.32; color:#332c22;}
blockquote p{ text-align:left; margin:.2em 0;}

/* tablas estilo académico (solo reglas horizontales) */
table{ border-collapse:collapse; width:100%; margin:.6em 0; font-size:.8em; line-height:1.26;
 border-top:1.3px solid var(--ink); border-bottom:1.3px solid var(--ink);}
th,td{ padding:.26em .5em; text-align:left; vertical-align:top; border:0;}
thead th{ border-bottom:1px solid var(--ink); font-variant:small-caps; letter-spacing:.02em;}
tbody tr{ border-bottom:.5px solid var(--rule);}
tbody tr:last-child{ border-bottom:0;}

/* diagramas / mapas: figura con forma */
pre{ border:1px solid var(--rule); background:var(--tint); padding:.55em .7em; margin:.7em 0;
 font-family:"Courier New",monospace; font-size:7.4pt; line-height:1.22; overflow-x:auto; white-space:pre;}
code{ font-family:"Courier New",monospace; font-size:.85em;}
pre code{ font-size:inherit;}
hr{ border:0; border-top:1px solid var(--rule); margin:.8em 0;}
ul,ol{ margin:.28em 0 .5em 1.05em;}
li{ margin:.08em 0;}

.escudo svg{ display:block; margin:0 auto;}
.escudo.grande svg{ width:118px; height:auto;}
.escudo.mediano svg{ width:78px; height:auto;}
.ornamento{ text-align:center; color:var(--accent); margin:.7em 0; font-size:.8rem; letter-spacing:.5em;}
.ornamento:after{ content:"\2766";}
.filete{ width:38%; height:0; border-top:1px solid var(--accent); margin:.9em auto;}

/* PORTADA */
.portada{ text-align:center; display:flex; flex-direction:column; justify-content:center; min-height:24cm;}
.portada .univ{ font-variant:small-caps; letter-spacing:.16em; font-size:.92rem; margin:.2em 0;}
.portada .facultad{ font-variant:small-caps; letter-spacing:.1em; font-size:.8rem; color:#4a4133; margin-bottom:1.2em;}
.portada .titulo{ font-size:2.15rem; line-height:1.12; margin:.2em 0; font-weight:700;}
.portada .subtitulo{ font-size:.98rem; font-style:italic; color:#3c342a; max-width:24em; margin:.7em auto 0;}
.portada .especialidad{ font-variant:small-caps; letter-spacing:.06em; color:var(--accent); font-size:.92rem; margin:1em auto 0; max-width:26em;}
.portada .autor{ margin-top:auto; font-size:1.15rem; font-variant:small-caps; letter-spacing:.08em;}
.portada .sello{ font-size:.85rem; color:#4a4133; margin-top:.2em;}
.portada .fecha{ font-style:italic; color:#4a4133; margin-top:.3em; font-size:.9rem;}

/* Preliminares */
.seccion-titulo{ text-align:center; font-variant:small-caps; letter-spacing:.1em; font-size:1.4rem; margin:.2em 0 1em;}
.carta{ font-size:10.4pt; line-height:1.5; max-width:31em; margin:0 auto;}
.carta p{ margin-bottom:.6em;}
.firma{ text-align:right; font-style:italic; margin-top:1.2em;}
.frase-vida{ text-align:center; font-style:italic; font-size:1.08rem; color:var(--accent);
 border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); padding:.8em .5em; margin:1.3em auto; max-width:30em;}
.dropcap:first-letter{ float:left; font-size:2.5rem; line-height:.82; padding:.02em .09em 0 0; color:var(--accent); font-weight:700;}

/* Portadilla de Parte */
.parte-portada{ text-align:center; min-height:23cm; display:flex; flex-direction:column; justify-content:center;}
.parte-portada .plabel{ font-variant:small-caps; letter-spacing:.24em; color:var(--accent); font-size:1rem;}
.parte-portada .ptitulo{ font-size:1.7rem; margin-top:.2em;}

/* Índice */
.toc{ font-size:.95em;}
.toc h3{ color:var(--accent); font-variant:small-caps; letter-spacing:.06em; margin-top:1em;}
.toc ul{ list-style:none; margin-left:0;}
.toc li{ border-bottom:1px dotted var(--rule); padding:.12em 0;}
.toc a{ text-decoration:none; color:var(--ink);}
.cap-num{ color:var(--accent); font-variant:small-caps; letter-spacing:.1em; font-size:.8rem;}
.cap-titulo{ font-size:1.4rem; color:var(--ink); margin:.05em 0 .7em; padding-bottom:.2em; border-bottom:1px solid var(--rule);}

/* Botón */
#barra{ position:fixed; right:20px; bottom:20px; z-index:99;}
#barra button{ font-family:inherit; background:var(--accent); color:#fdfbf6; border:0;
 padding:11px 18px; border-radius:6px; font-size:.95rem; cursor:pointer; box-shadow:0 5px 16px rgba(0,0,0,.3);}
#barra button:hover{ background:#84172a;}

@media print{
 @page{ size:letter; margin:1.5cm 1.5cm; }
 body{ background:#fff; color:#000; font-size:9pt; line-height:1.32;}
 .page{ width:auto; margin:0; padding:0; box-shadow:none;}
 .cuerpo{ column-gap:.7cm;}
 #barra{ display:none !important;}
 .nueva-pagina{ break-before:page;}
 h2,h3,h4{ break-after:avoid;}
 table,pre,blockquote,figure{ break-inside:avoid;}
 .portada,.parte-portada,.colofon{ min-height:90vh;}
}
"""

# ---------- front matter ----------
def portada():
    return f"""<section class="page portada">
 {escudo('grande')}
 <div class="univ">Universidad Nacional Autónoma de México</div>
 <div class="facultad">Facultad de Estudios Superiores Aragón</div>
 <div class="filete"></div>
 <div class="titulo">Manual para Ejercer<br>el Derecho Corporativo</div>
 <div class="especialidad">Especialidad en Derecho Fiscal-Corporativo · Fusiones y Adquisiciones (M&amp;A) · Competencia Económica · Financiamiento y Gobierno Corporativo</div>
 <div class="subtitulo">Obra de doctrina y práctica construida sobre 27 leyes oficiales verificadas <em>verbatim</em>, con disciplina de vigencia&nbsp;⟳.</div>
 <div class="filete"></div>
 <div class="autor">Elias Alejo</div>
 <div class="sello">Biblioteca Jurídica AJE</div>
 <div class="fecha">{FECHA}</div>
</section>"""

def pagina_legal():
    return f"""<section class="page nueva-pagina">
 <div style="margin-top:60%;font-size:.95rem;color:#4d4130;">
 <p><strong>Manual para Ejercer el Derecho Corporativo.</strong> Primera edición, {FECHA}.</p>
 <p>Autor: <strong>Elias Alejo</strong>. Obra formativa de la <em>Biblioteca Jurídica AJE</em>, elaborada
 durante la formación del autor en la Facultad de Estudios Superiores Aragón, UNAM.</p>
 <p>Esta obra es un <strong>instrumento de estudio y ejercicio profesional</strong>. Todo fundamento legal
 fue cotejado contra su texto oficial vigente a la fecha de edición; no obstante, el Derecho cambia: el
 símbolo <strong>⟳</strong> recuerda al lector que debe <strong>reverificar la vigencia</strong> de cada
 norma, tasa, monto o criterio en su fuente oficial (DOF, Cámara de Diputados, SJF) antes de aplicarla a
 un caso real. Semáforo de confianza: <strong>✅</strong> dato cotejado &nbsp;·&nbsp; <strong>⚠️</strong> dato
 volátil por reverificar.</p>
 <p>El escudo de la UNAM se reproduce con fines identificatorios y académicos.</p>
 </div>
</section>"""

def dedicatoria():
    return """<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Al Elias del futuro</h2>
 <div class="carta">
 <p class="dropcap">Si estás leyendo esto, es porque el muchacho de veintiún años que empezó con más
 errores que méritos decidió no rendirse. Te escribo desde el principio del camino para recordarte lo que
 no debes olvidar cuando ya lo hayas recorrido.</p>
 <p>Nadie nos regaló nada. Lo que tienes en las manos no nació del talento ni de la suerte: nació de
 <strong>sentarse todos los días</strong>, sobre todo los días en que no había ganas. Recuerda esto: la
 motivación es un invitado que llega tarde y se va temprano; la <strong>disciplina</strong> es la que se
 queda a trabajar contigo de madrugada. No confíes en cómo te sientes. Confía en lo que haces cada día.</p>
 <p>Venimos de abajo, y eso —que un día pareció una condena— es en realidad nuestra ventaja: sabemos lo
 que cuesta. El <strong>trabajo duro es el único ascensor que no pregunta de dónde vienes, solo hasta
 dónde estás dispuesto a subir</strong>. No naciste para quedarte en el estanque donde otros se conforman.
 Estudiar te saca la cabeza del agua; <strong>ejercer, verificar y crear</strong> te sacan del estanque
 entero.</p>
 <p>No te conformes con ser un buen estudiante. El buen estudiante <em>sabe</em>; el jurista <em>hace</em>,
 <em>decide</em> y <em>responde</em>. Leer es el comienzo, no la meta. Cada página de este manual existe
 para que dejes de acumular información y empieces a <strong>tener criterio</strong>. Duda, cotéjalo,
 discútelo, redáctalo, defiéndelo. Ahí, y solo ahí, se forma el abogado que decidiste ser.</p>
 <p>Y cuando llegues —porque vas a llegar— no te ablandes. Sé humilde para verificar y ambicioso para
 exigirte. Que nunca se te olvide de dónde saliste ni a costa de qué.</p>
 <div class="frase-vida">«El que estudia, sabe; el que verifica y ejerce, manda.<br>
 A la disciplina no le importa de dónde vienes: solo hasta dónde estás dispuesto a llegar.»</div>
 <div class="firma">Con todo lo que soy y lo que seré,<br><strong>Elias Alejo</strong><br>""" + FECHA + """</div>
 </div>
</section>"""

def consideraciones():
    return """<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Consideraciones para el lector</h2>
 <p class="dropcap">Este no es un libro para leerse de corrido y olvidarse. Es un <strong>sistema de
 trabajo</strong>. Léelo con la ley al lado, con un cuaderno abierto y con la disposición de discutir cada
 afirmación. Antes de comenzar, comprende sus tres reglas.</p>
 <h3>1. El semáforo de confianza</h3>
 <p>Cada dato duro lleva una marca: <strong>✅</strong> significa que fue <em>cotejado palabra por palabra</em>
 contra el texto oficial vigente a la fecha de edición. <strong>⚠️</strong> significa que es un dato
 <em>volátil</em> —una fecha de reforma, una tasa, un monto, una cifra— que <strong>cambia con el tiempo</strong>
 y que debes reverificar en su ejercicio correspondiente. La marca ⚠️ no es un defecto: es una advertencia honesta.</p>
 <h3>2. La apóstrofe de vigencia (⟳)</h3>
 <p>Tras cada artículo citado verás el símbolo <strong>⟳</strong>. Es la regla de oro de este manual:
 <em>«¿sigue vigente y con este mismo número hoy? Reitéralo en su código antes de citarlo.»</em> El Derecho
 cambia sin avisar —lo comprobamos: artículos derogados e incluso un código entero (el CFPC) en vías de
 abrogación. <strong>Jamás cites de memoria.</strong> La última palabra la tiene el código, no el libro.</p>
 <h3>3. De la lectura a la práctica</h3>
 <p>Al final encontrarás un <strong>Banco de Formatos</strong> (term sheet, acta de asamblea, pagaré,
 contrato de compraventa de acciones, aviso de privacidad, demanda de amparo). No los leas: <strong>llénalos,
 negócialos, defiéndelos</strong>. El conocimiento que no se ejerce se evapora.</p>
 <div class="ornamento"></div>
</section>"""

def finalidad():
    return """<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Finalidad de esta obra</h2>
 <p class="dropcap">La finalidad de este manual es <strong>formar criterio, no memoria</strong>. No busca que
 el lector sepa recitar artículos —esos caducan—, sino que <strong>piense como jurista</strong>: que entienda
 la estructura permanente del sistema jurídico mexicano y que desconfíe por método de todo dato que no pueda
 verificar.</p>
 <p>En concreto, esta obra persigue tres objetivos:</p>
 <ul>
 <li><strong>Comprender cada punto</strong> del Derecho aplicable al ejercicio corporativo, desde sus raíces
 romanas y civiles hasta la ingeniería de una fusión o una adquisición.</li>
 <li><strong>Dar lo necesario para ejercer</strong> el Derecho corporativo y la rama que el lector elija:
 doctrina verificada, fuentes primarias, formatos reales y criterios jurisprudenciales por materia.</li>
 <li><strong>Cerrar la brecha entre la universidad y el despacho</strong>: convertir al estudiante en el
 profesional que se sienta en la mesa donde se decide la estructura de una operación, y no en el que
 únicamente redacta lo ya decidido.</li>
 </ul>
 <p>Dicho de otro modo: que quien la domine sea reconocido, en el menor tiempo posible, como una
 <strong>promesa real del Derecho</strong>, y llegue a ser <strong>el jurista más solicitado</strong> de su rama.</p>
 <div class="ornamento"></div>
</section>"""

def estructura():
    return """<section class="page nueva-pagina">
 <h2 class="seccion-titulo">Cómo está estructurado</h2>
 <p class="dropcap">La obra avanza como una escalera: de los cimientos a la maestría, y de la teoría a la
 práctica. Cada parte supone la anterior.</p>
 <ul>
 <li><strong>Parte I — Fundamentos:</strong> el sistema operativo del jurista (derecho romano, teoría del
 derecho y del Estado, acto jurídico, personas, bienes, obligaciones, contratos, argumentación y lógica).</li>
 <li><strong>Parte II — Derecho Civil Profundo:</strong> obligaciones, contratos en particular,
 responsabilidad civil y garantías.</li>
 <li><strong>Parte III — Derecho Mercantil:</strong> sociedades, títulos de crédito, mercado de valores,
 concursos y gobierno corporativo.</li>
 <li><strong>Parte IV — Derecho Corporativo:</strong> el corazón del ejercicio: M&amp;A, due diligence,
 estructuras, documentación (term sheet, SPA, SHA), financiamiento, private equity, compliance, fiscal
 corporativo y competencia económica.</li>
 <li><strong>Parte V — Maestría:</strong> negociación de alto nivel, finanzas y contabilidad para abogados,
 valuación de empresas y estrategia corporativa.</li>
 <li><strong>Parte VI — Ramas Esenciales:</strong> las materias transversales que todo abogado debe dominar
 (fiscal, constitucional y amparo, laboral, penal económico, propiedad intelectual, datos, ambiental, etc.).</li>
 <li><strong>Anexo A — Banco de Formatos:</strong> plantillas reales listas para practicar.</li>
 </ul>
 <p>Cada capítulo conserva sus marcas de verificación (✅ / ⚠️ / ⟳) para que el estudio nunca se separe de la
 disciplina de la fuente.</p>
 <div class="ornamento"></div>
</section>"""

def indice():
    parts=['<section class="page nueva-pagina toc"><h2 class="seccion-titulo">Índice general</h2>']
    romano={"Parte I":"","Parte II":"","Parte III":"","Parte IV":"","Parte V":"","Parte VI":"","Anexo A":""}
    for plabel,ptitle,entries in toc:
        parts.append(f'<h3>{plabel} — {ptitle}</h3><ul>')
        for i,(t,a) in enumerate(entries,1):
            parts.append(f'<li><a href="#{a}"><span class="cap-titulo-toc">{t}</span></a></li>')
        parts.append("</ul>")
    parts.append("</section>")
    return "".join(parts)

def parte_portada(plabel,ptitle):
    return f'<section class="page nueva-pagina parte-portada">{escudo("mediano")}<div class="plabel">{plabel}</div><div class="ptitulo">{ptitle}</div><div class="ornamento"></div></section>'

def capitulo(plabel,cap_title,anchor,html):
    return (f'<section class="page nueva-pagina" id="{anchor}">'
            f'<div class="cap-num">{plabel}</div>'
            f'<h1 class="cap-titulo">{cap_title}</h1>'
            f'<div class="cuerpo">{html}</div></section>')

def colofon():
    return f"""<section class="page nueva-pagina colofon portada">
 {escudo('grande')}
 <div class="filete"></div>
 <p style="font-variant:small-caps;letter-spacing:.1em;">Fin de la obra</p>
 <div class="frase-vida">«No naciste para quedarte en el estanque.<br>Trabaja en silencio; deja que el resultado haga el ruido.»</div>
 <div class="autor">Elias Alejo</div>
 <div class="sello">Biblioteca Jurídica AJE — Manual para Ejercer el Derecho Corporativo</div>
 <div class="fecha">{FECHA}</div>
 <div class="filete"></div>
 <p style="font-size:.85rem;color:#6b5b3e;">Universidad Nacional Autónoma de México · Facultad de Estudios Superiores Aragón</p>
</section>"""

# ---------- ensamblado ----------
body=[portada(), pagina_legal(), dedicatoria(), consideraciones(), finalidad(), estructura(), indice()]
cur_part=None
for plabel,ptitle,cap_title,anchor,html,is_first in chapters:
    if is_first:
        body.append(parte_portada(plabel,ptitle))
    body.append(capitulo(plabel,cap_title,anchor,html))
# Anexo formatos
if anexo:
    body.append(parte_portada("Anexo A","Banco de Formatos"))
    for t,a,h in anexo:
        body.append(capitulo("Anexo A", t, a, h))
body.append(colofon())

barra = ('<div id="barra"><button onclick="window.print()">📖 Generar PDF / Imprimir</button></div>')

HTML = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Manual para Ejercer el Derecho Corporativo — Elias Alejo</title>
<style>{CSS}</style></head>
<body>
{barra}
{''.join(body)}
</body></html>"""

os.makedirs("LIBRO", exist_ok=True)
open("LIBRO/Manual-para-Ejercer-el-Derecho-Corporativo.html","w",encoding="utf-8").write(HTML)
print(f"OK libro generado. Capítulos: {cap_n}. Tamaño: {len(HTML)//1024} KB")
