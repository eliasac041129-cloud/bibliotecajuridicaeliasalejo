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
MD = markdown.Markdown(extensions=["tables","fenced_code","sane_lists","attr_list","toc"])
def md2html(text):
    # quitar el H1 (lo usamos como título de capítulo aparte)
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
:root{ --ink:#211c15; --paper:#fbf7ee; --gold:#8a6d23; --burgundy:#6e1420; --rule:#c9b98f; }
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#4a4137;color:var(--ink);
 font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Palatino,Georgia,"Times New Roman",serif;
 font-size:12.5pt;line-height:1.62;}
.page{background:var(--paper);width:18.5cm;min-height:26cm;margin:26px auto;padding:2.4cm 2.6cm;
 box-shadow:0 10px 40px rgba(0,0,0,.45);position:relative;}
p{ text-align:justify; hyphens:auto; margin:0 0 .7em; }
h1,h2,h3,h4{ font-weight:600; line-height:1.25; color:#1b1610; }
h2{ font-size:1.45rem; margin:1.6em 0 .5em; border-bottom:1px solid var(--rule); padding-bottom:.2em;}
h3{ font-size:1.18rem; margin:1.3em 0 .4em; color:var(--burgundy);}
h4{ font-size:1.02rem; margin:1.1em 0 .3em; font-variant:small-caps; letter-spacing:.02em;}
a{ color:var(--burgundy); }
blockquote{ margin:1em 0; padding:.6em 1em; border-left:3px solid var(--gold);
 background:#f3ecd9; font-style:italic; color:#3a3226;}
blockquote p{ text-align:left; }
table{ border-collapse:collapse; width:100%; margin:1em 0; font-size:.92em;}
th,td{ border:1px solid var(--rule); padding:.4em .6em; text-align:left; vertical-align:top;}
th{ background:#efe6cf; font-variant:small-caps;}
code{ font-family:"Courier New",monospace; font-size:.9em; background:#efe7d3; padding:.05em .3em;border-radius:3px;}
pre{ background:#2b2419; color:#f3ecd9; padding:1em; overflow:auto; border-radius:4px; font-size:.82em;}
pre code{ background:none; color:inherit;}
hr{ border:0; height:1px; background:var(--rule); margin:1.4em 0;}
ul,ol{ margin:.4em 0 .9em 1.3em;}
li{ margin:.2em 0;}
.escudo svg{ display:block; margin:0 auto; }
.escudo.grande svg{ width:150px; height:auto; }
.escudo.mediano svg{ width:96px; height:auto; }
.ornamento{ text-align:center; color:var(--gold); font-size:1.3rem; letter-spacing:.5em; margin:1.2em 0;}
.ornamento:after{ content:"❧"; }

/* PORTADA */
.portada{ text-align:center; display:flex; flex-direction:column; justify-content:center; min-height:25cm;}
.portada .univ{ font-variant:small-caps; letter-spacing:.14em; font-size:1rem; color:#463b28; margin:.2em 0;}
.portada .facultad{ font-variant:small-caps; letter-spacing:.1em; font-size:.86rem; color:#6b5b3e; margin-bottom:1.5em;}
.filete{ width:60%; height:2px; background:linear-gradient(90deg,transparent,var(--gold),transparent); margin:1.4em auto;}
.portada .titulo{ font-size:2.55rem; line-height:1.15; margin:.3em 0; color:#1b1610; font-weight:700; letter-spacing:.01em;}
.portada .subtitulo{ font-size:1.12rem; font-style:italic; color:#4d4130; max-width:24em; margin:.8em auto 0;}
.portada .especialidad{ font-variant:small-caps; letter-spacing:.08em; color:var(--burgundy); font-size:1.05rem; margin-top:1.2em;}
.portada .autor{ margin-top:auto; font-size:1.25rem; font-variant:small-caps; letter-spacing:.08em;}
.portada .sello{ font-size:.95rem; color:#5b4c33; margin-top:.2em;}
.portada .fecha{ font-style:italic; color:#5b4c33; margin-top:.4em;}

/* Secciones preliminares */
.seccion-titulo{ text-align:center; font-variant:small-caps; letter-spacing:.1em; font-size:1.7rem;
 margin:.2em 0 1.2em; color:#1b1610;}
.carta{ font-size:12.8pt; }
.carta p{ margin-bottom:.9em;}
.firma{ text-align:right; font-style:italic; margin-top:1.4em;}
.frase-vida{ text-align:center; font-style:italic; font-size:1.28rem; color:var(--burgundy);
 border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); padding:1em .5em; margin:1.6em 0;}
.dropcap:first-letter{ float:left; font-size:3.4rem; line-height:.8; padding:.05em .1em 0 0; color:var(--burgundy); font-weight:700;}

/* Portadilla de Parte */
.parte-portada{ text-align:center; min-height:24cm; display:flex; flex-direction:column; justify-content:center;}
.parte-portada .plabel{ font-variant:small-caps; letter-spacing:.24em; color:var(--gold); font-size:1.2rem;}
.parte-portada .ptitulo{ font-size:2.1rem; margin-top:.3em; color:#1b1610;}

/* Índice */
.toc h3{ color:var(--gold); font-variant:small-caps; letter-spacing:.06em; border:0; margin-top:1.2em;}
.toc ul{ list-style:none; margin-left:0;}
.toc li{ display:flex; justify-content:space-between; border-bottom:1px dotted var(--rule); padding:.15em 0;}
.toc a{ text-decoration:none; color:var(--ink);}
.cap-num{ color:var(--gold); font-variant:small-caps; letter-spacing:.1em; font-size:.9rem;}
.cap-titulo{ font-size:1.75rem; color:#1b1610; margin:.1em 0 1em; }

/* Botón */
#barra{ position:fixed; right:22px; bottom:22px; z-index:99; display:flex; gap:10px;}
#barra button{ font-family:inherit; background:var(--burgundy); color:#f7efdc; border:1px solid #4a0d15;
 padding:12px 20px; border-radius:8px; font-size:1rem; cursor:pointer; box-shadow:0 6px 18px rgba(0,0,0,.35);}
#barra button:hover{ background:#8a1a28;}

@media print{
 @page{ size:letter; margin:2cm 2.1cm; }
 body{ background:#fff; font-size:11pt;}
 .page{ width:auto; min-height:auto; margin:0; padding:0; box-shadow:none; }
 #barra{ display:none !important; }
 .parte-portada,.portada,.colofon{ min-height:92vh; }
 .nueva-pagina{ break-before:page; }
 h2,h3,h4{ break-after:avoid; }
 table,blockquote,pre,figure{ break-inside:avoid; }
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
            f'<h1 class="cap-titulo">{cap_title}</h1>{html}</section>')

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
