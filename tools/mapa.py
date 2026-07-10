#!/usr/bin/env python3
"""Genera MAPA-DE-ARTICULOS.md: tablero de artículos citados -> ley -> tratados -> estado."""
import glob, os, re, collections

LAWNAMES = {
 "CPEUM":"Constitución (CPEUM)","CFF":"Código Fiscal (CFF)","LISR":"Ley del ISR","LIVA":"Ley del IVA",
 "CCF":"Código Civil Federal","CCom":"Código de Comercio","LGSM":"Ley Gral. de Sociedades (LGSM)",
 "LGTOC":"Títulos y Op. de Crédito (LGTOC)","LMV":"Ley del Mercado de Valores","LCM":"Ley de Concursos Mercantiles",
 "LIC":"Ley de Instituciones de Crédito","LIE":"Ley de Inversión Extranjera","LFCE":"Ley Fed. de Competencia (LFCE)",
 "LFPPI":"Ley Fed. de Protección a la Propiedad Industrial","LFDA":"Ley Fed. del Derecho de Autor",
 "LFT":"Ley Federal del Trabajo","LSS":"Ley del Seguro Social","CPF":"Código Penal Federal",
 "CNPP":"Código Nal. de Proc. Penales","CNPCF":"Código Nal. de Proc. Civiles y Familiares",
 "CFPC":"Código Fed. de Proc. Civiles (abrogado)","LAmp":"Ley de Amparo","LFPCA":"Ley Fed. de Proc. Contencioso Adm.",
 "LFPDPPP":"Ley Fed. de Protección de Datos (LFPDPPP)","LGRA":"Ley Gral. de Responsabilidades Adm.",
 "LGEEPA":"Ley Gral. del Equilibrio Ecológico","LFPC":"Ley Fed. de Protección al Consumidor",
}
LAWS = sorted(LAWNAMES, key=len, reverse=True)
LAWRE = "|".join(re.escape(l) for l in LAWS)
DEFAULT = {
 "01-Derecho-Fiscal":"CFF","02-Derecho-Constitucional":"CPEUM","05-Derecho-Laboral":"LFT",
 "06-Derecho-Penal":"CPF","07-Propiedad-Intelectual":"LFPPI","09-Proteccion-de-Datos":"LFPDPPP",
 "10-Derecho-Ambiental":"LGEEPA","12-Derecho-Procesal-Penal":"CNPP","13-Derecho-Familiar":"CCF",
 "02-Sociedades-Mercantiles":"LGSM","03-Titulos-y-Operaciones":"LGTOC","05-Mercado-de-Valores":"LMV",
 "06-Concurso-Mercantil":"LCM","05-Personas":"CCF","06-Bienes":"CCF","07-Obligaciones":"CCF",
 "08-Contratos-Parte-General":"CCF","01-Teoria-General-de-las-Obligaciones":"CCF",
 "02-Contratos-Civiles":"CCF","03-Responsabilidad-Civil":"CCF",
}
def default_law(fp):
    b=os.path.basename(fp)
    for k,v in DEFAULT.items():
        if b.startswith(k): return v
    return None
CITE = re.compile(
  r"(?:arts?\.|art[íi]culos?)\s+(?P<num>\d{1,4})(?P<o>[ºo°]?)(?:-(?P<suf>[A-Z0-9]+))?"
  r"(?:(?:\s*\*\*)?\s+(?:de\s+la\s+|del\s+|de\s+)?(?P<law>"+LAWRE+r")\b)?"
  r"(?P<tail>(?:\s*(?:\*\*|⟳|✅|⚠️))*)", re.IGNORECASE)

def treatise(path):
    b=os.path.basename(path).replace('.md','')
    return b

data=collections.defaultdict(lambda: collections.defaultdict(lambda:{"ok":0,"warn":0,"files":set()}))
for p in glob.glob('Columna-I-Biblioteca/**/*.md', recursive=True):
    if os.path.basename(p)=='README.md': continue
    t=open(p,encoding='utf-8').read()
    dl=default_law(p)
    for m in CITE.finditer(t):
        rawlaw=m.group('law') or dl
        if not rawlaw: continue
        law=next((l for l in LAWS if l.lower()==rawlaw.lower()), rawlaw)
        num=m.group('num')+((m.group('o') or '') and 'º') 
        key=m.group('num')+("-"+m.group('suf').upper() if m.group('suf') else "")
        tail=m.group('tail')
        rec=data[law][key]
        rec["files"].add(treatise(p))
        if "✅" in tail: rec["ok"]+=1
        elif "⚠️" in tail: rec["warn"]+=1

def artkey(k):
    m=re.match(r"(\d+)(?:-([A-Z0-9]+))?",k); return (int(m.group(1)), m.group(2) or "")

FUENTE = set(LAWNAMES)  # todas tienen fuente verificada en fuentes-legales/
out=[]
out.append("# 🗺️ Mapa de Artículos Citados\n")
out.append("> **Qué es esto.** Tablero de todos los artículos citados en la biblioteca, agrupados por ley, "
           "con el tratado donde se explican y su estado de verificación. Sirve como **panel de control** "
           "de la verificación y como **herramienta de repaso** (recorre una ley y comprueba que dominas cada artículo).\n")
out.append("> **Leyenda:** ✅ número de artículo cotejado y vigente en el texto oficial · ⚠️ dato por reverificar · "
           "⟳ *apóstrofe de vigencia* (reverifica siempre en el código). Fuente primaria: [`fuentes-legales/`](./fuentes-legales/).\n")
# tabla resumen
out.append("## Resumen por ley\n")
out.append("| Ley | Artículos citados | Fuente verificada |")
out.append("|---|---|---|")
for law in sorted(data, key=lambda l: -len(data[l])):
    n=len(data[law])
    fuente="✅ sí" if law in FUENTE else "—"
    out.append(f"| {LAWNAMES.get(law,law)} | {n} | {fuente} |")
out.append("")
# detalle por ley
out.append("## Detalle por ley\n")
for law in sorted(data, key=lambda l: LAWNAMES.get(l,l)):
    arts=data[law]
    out.append(f"### {LAWNAMES.get(law,law)}  \n")
    out.append("| Artículo | Estado | Tratado(s) |")
    out.append("|---|---|---|")
    for k in sorted(arts, key=artkey):
        rec=arts[k]
        st="✅" if rec["ok"]>0 and rec["warn"]==0 else ("✅/⚠️" if rec["ok"]>0 else "⚠️")
        files=", ".join(sorted(rec["files"])[:3])
        out.append(f"| art. {k} | {st} ⟳ | {files} |")
    out.append("")
open("MAPA-DE-ARTICULOS.md","w",encoding="utf-8").write("\n".join(out))
tot=sum(len(v) for v in data.values())
print(f"MAPA-DE-ARTICULOS.md generado: {len(data)} leyes, {tot} artículos únicos citados con sigla.")
