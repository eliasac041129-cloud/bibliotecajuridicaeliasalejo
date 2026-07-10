#!/usr/bin/env python3
"""Voltea ⚠️→✅ SOLO en citas de artículo cuyo número se confirma vigente en el texto oficial.
Seguro: exige que la cita nombre una ley con fuente en fuentes-legales/; nunca toca datos sin fuente.
Uso: tools/semaforo.py <archivo.md> [--apply]   (sin --apply = simulación)
"""
import sys, re, glob, os

W = "\u26a0\ufe0f"; OK = "\u2705"
FL = "fuentes-legales"

# abreviatura de cita -> patrón del nombre de archivo de la fuente
ABBR = {
 "CFF":"CFF-","LISR":"LISR-","LIVA":"LIVA-","LGSM":"LGSM-","LGTOC":"LGTOC-","LMV":"LMV-",
 "CCF":"CCF-","CPF":"CPF-","CPEUM":"CPEUM-","CCom":"CCom-","LFCE":"LFCE-","LFPPI":"LFPPI-",
 "LCM":"LCM-","LIC":"LIC-","LIE":"LIE-","CNPP":"CNPP-","CNPCF":"CNPCF-","LFPDPPP":"LFPDPPP-",
 "LGRA":"LGRA-","LGEEPA":"LGEEPA-","LFPC":"LFPC-","LFPCA":"LFPCA-","LFDA":"LFDA-","LSS":"LSS-",
 "CFPC":"CFPC-","LAmp":"LAmp-","LA":"LAmp-","LFT":"LFT-",
}
HDR = re.compile(r"^\s*ART[\u00cdI\u00edi]CULO\s+(\d{1,4})\s*[\u00bao\u00b0]?\s*[.\-]*\s*(?:-\s*([A-Z]))?", re.IGNORECASE)

def load(pat):
    fs = glob.glob(os.path.join(FL, pat + "*.txt"))
    if not fs: return None
    valid=set(); derog=set()
    for line in open(fs[0], encoding="utf-8"):
        m = HDR.match(line)
        if not m: continue
        num = m.group(1); suf = (m.group(2) or "").upper()
        key = num + ("-"+suf if suf else "")
        low = line.lower()
        if "se deroga" in low or "derogad" in low or "abrogad" in low:
            derog.add(key); derog.add(num)
        else:
            valid.add(key)
    return valid, derog

SRC = {a: load(p) for a,p in ABBR.items()}
LAWS = sorted(ABBR, key=len, reverse=True)
LAWRE = "|".join(re.escape(l) for l in LAWS)

# ley por defecto para citas SIN sigla, según el tratado
DEFAULT = {
 "01-Derecho-Fiscal":"CFF", "02-Derecho-Constitucional":"CPEUM", "05-Derecho-Laboral":"LFT",
 "06-Derecho-Penal":"CPF", "07-Propiedad-Intelectual":"LFPPI", "09-Proteccion-de-Datos":"LFPDPPP",
 "10-Derecho-Ambiental":"LGEEPA", "12-Derecho-Procesal-Penal":"CNPP",
 "13-Derecho-Familiar":"CCF",
 "02-Sociedades-Mercantiles":"LGSM", "03-Titulos-y-Operaciones":"LGTOC", "05-Mercado-de-Valores":"LMV",
 "06-Concurso-Mercantil":"LCM",
 "05-Personas":"CCF","06-Bienes":"CCF","07-Obligaciones":"CCF","08-Contratos-Parte-General":"CCF",
 "01-Teoria-General-de-las-Obligaciones":"CCF","02-Contratos-Civiles":"CCF","03-Responsabilidad-Civil":"CCF",
}
def default_law(fp):
    b=os.path.basename(fp)
    for k,v in DEFAULT.items():
        if b.startswith(k): return v
    return None

CITE = re.compile(
    r"(?P<pre>(?:arts?\.|art[\u00edi]culos?)\s+)"
    r"(?P<num>\d{1,4})(?P<o>[\u00bao\u00b0]?)(?:-(?P<suf>[A-Z0-9]+))?"
    r"(?P<mid>(?:\s*,\s*(?:fr(?:acc)?\.?|fracci[o\u00f3]n)\s*[IVXLCDM0-9\u00ba.,\sy]*?)?"
    r"(?:(?:\s*,\s*|\s+y\s+)\d{1,4}[\u00bao\u00b0]?(?:-[A-Z0-9]+)?)*)"
    r"(?:\s*\*\*)?"
    r"(?:\s+(?:de\s+la\s+|del\s+|de\s+)?(?P<law>" + LAWRE + r")\b)?"
    r"(?P<b1>(?:\s*(?:\*\*|\u27f3))*)(?P<warn>\s*" + W + r")(?P<b2>(?:\s*\u27f3)?)",
    re.IGNORECASE)

def confirmed(law, num, suf):
    data = SRC.get(law)
    if not data: return None
    valid, derog = data
    key = num + ("-"+suf.upper() if suf else "")
    if key in derog or num in derog: return "DEROGADO"
    if key in valid or num in valid: return "OK"
    return None

def process(text, deflaw=None):
    stats={"ok":0,"derog":0,"nomatch":0}
    def repl(m):
        law = m.group("law") or deflaw
        if not law: 
            stats["nomatch"]+=1; return m.group(0)
        lk = next((l for l in LAWS if l.lower()==law.lower()), law)
        st = confirmed(lk, m.group("num"), m.group("suf"))
        if st=="OK":
            stats["ok"]+=1
            return m.group(0).replace(W, OK, 1)  # solo cambia el ⚠️ de esta cita
        if st=="DEROGADO": stats["derog"]+=1
        else: stats["nomatch"]+=1
        return m.group(0)
    new = CITE.sub(repl, text)
    return new, stats

if __name__=="__main__":
    path=sys.argv[1]; apply="--apply" in sys.argv
    o=open(path,encoding="utf-8").read()
    n,st=process(o, default_law(path))
    if apply:
        open(path,"w",encoding="utf-8").write(n)
        print(f"APPLIED  ✅+{st['ok']:3d}  (derogados intactos:{st['derog']}, sin confirmar:{st['nomatch']})  {os.path.basename(path)}")
    else:
        shown=0
        for a,b in zip(o.split("\n"),n.split("\n")):
            if a!=b and shown<8:
                print("  +", b[:140]); shown+=1
        print(f"DRY  ✅+{st['ok']}  derog:{st['derog']}  sinConf:{st['nomatch']}  {os.path.basename(path)}")
